"""
focker.py — Emulación simplificada de Docker en Python puro

Este programa implementa un contenedor Linux básico usando características
del kernel directamente a través de llamadas a libc (via ctypes). Emula el
comportamiento central de Docker mediante tres mecanismos principales:

  1. Namespaces de Linux (unshare): aíslan UTS (hostname), PID, filesystem y red.
  2. chroot: cambia el directorio raíz del proceso hijo al filesystem del contenedor.
  3. cgroups v2: limitan los recursos del contenedor (en este caso, el nº de PIDs).

Uso:
    python focker.py run <imagen> <comando> [args...]
    python focker.py child <comando> [args...]   ← invocado internamente por 'run'

Arquitectura de procesos:
    [proceso padre: run()]
        └── fork → [proceso hijo: child()]
                       └── exec → [comando del usuario]

Requisitos:
    - Linux con cgroups v2 habilitados.
    - Ejecutar como root (necesario para unshare, chroot y mount).
    - Filesystem del contenedor en /home/ubuntu/container_fs.
"""

import os
import sys
import subprocess
import ctypes
from pathlib import Path


# ---------------------------------------------------------------------------
# Utilidades
# ---------------------------------------------------------------------------

def must(condition, mensaje):
    """
    Comprueba una condición y aborta el programa si no se cumple.

    Actúa como un assert con mensaje de error amigable. Se usa para
    verificar el resultado de llamadas al sistema (syscalls) que deben
    tener éxito obligatoriamente.

    Args:
        condition (bool): Expresión booleana a evaluar.
        mensaje (str): Mensaje de error que se imprime antes de salir.

    Returns:
        None

    Ejemplo:
        must(ret == 0, "fallo al crear namespace")
    """
    if not condition:
        msg(mensaje)


def msg(error):
    """
    Imprime un mensaje de error por stdout y termina el proceso con código 1.

    Se usa como punto centralizado de salida ante errores irrecuperables,
    similar al patrón log.Fatal() de Go.

    Args:
        error (str | Exception): Descripción del error o excepción capturada.

    Returns:
        None (no retorna; termina el proceso).
    """
    print(error)
    sys.exit(1)


# ---------------------------------------------------------------------------
# Comando: run
# ---------------------------------------------------------------------------

def run():
    """
    Punto de entrada del comando 'run'. Configura el entorno aislado (namespaces)
    y lanza el proceso hijo dentro de él.

    Esta función es la equivalente al 'runc create' de Docker: prepara el
    contexto de aislamiento del kernel antes de ejecutar el proceso del
    contenedor. Lo hace en dos pasos:

      1. Llama a unshare() para crear nuevos namespaces en el proceso actual.
      2. Ejecuta este mismo script con el argumento 'child', lo que hace que
         el nuevo proceso herede los namespaces recién creados.

    Namespaces creados:
        - CLONE_NEWUTS  (0x04000000): hostname y domainname propios.
        - CLONE_NEWPID  (0x20000000): árbol de PIDs aislado (el hijo será PID 1).
        - CLONE_NEWNS   (0x00020000): tabla de montajes independiente.
        - CLONE_NEWNET  (0x40000000): interfaz de red aislada.

    Flujo:
        focker run <img> <cmd>  →  unshare()  →  focker child <cmd>

    Raises:
        SystemExit: Si unshare() falla o el proceso hijo retorna código != 0.
    """
    print(f"run {os.getpid()}: {sys.argv[:3]}")

    # Construimos el comando que se ejecutará como proceso hijo:
    # re-invocamos este mismo script con el subcomando 'child',
    # pasando los argumentos del usuario (a partir del índice 3).
    cmd = [
        sys.executable,            # intérprete Python actual
        os.path.abspath(__file__), # ruta absoluta a este script
        "child",
        *sys.argv[3:]              # argumentos del usuario tras <imagen>
    ]

    try:
        # Cargamos la libc del sistema para acceder a syscalls no expuestas
        # directamente por el módulo 'os' de Python.
        libc = ctypes.CDLL(None, use_errno=True)

        # Flags de unshare(2): cada constante activa un namespace diferente.
        CLONE_NEWUTS = 0x04000000  # hostname y domainname
        CLONE_NEWPID = 0x20000000  # aislamiento de PIDs
        CLONE_NEWNS  = 0x00020000  # aislamiento de filesystem (mount namespace)
        CLONE_NEWNET = 0x40000000  # aislamiento de red

        # unshare(2): desasocia el proceso de los namespaces compartidos con el padre.
        # A partir de aquí, este proceso (y sus hijos) tienen namespaces propios.
        must(
            libc.unshare(CLONE_NEWUTS | CLONE_NEWPID | CLONE_NEWNS | CLONE_NEWNET) == 0,
            "creación de entorno aislado"
        )

        # Ejecutar el proceso hijo dentro de los namespaces recién creados.
        # Como CLONE_NEWPID ya está activo, el hijo aparecerá como PID 1
        # dentro de su propio namespace de PIDs.
        proc = subprocess.run(
            cmd,
            stdin=sys.stdin,
            stdout=sys.stdout,
            stderr=sys.stderr
        )
        must(proc.returncode == 0, f"comando falla: {proc.returncode}")

    except Exception as e:
        msg(e)


# ---------------------------------------------------------------------------
# Comando: child
# ---------------------------------------------------------------------------

def child():
    """
    Ejecuta el proceso del contenedor tras haber sido aislado por run().

    Esta función es llamada automáticamente por run() en el proceso hijo.
    Completa la configuración del contenedor antes de ejecutar el comando
    del usuario:

      1. Configura cgroups para limitar recursos (via cg()).
      2. Cambia el hostname del namespace UTS a "focker".
      3. Hace chroot al filesystem del contenedor.
      4. Monta /proc y /tmp dentro del contenedor.
      5. Ejecuta el comando del usuario.
      6. Desmonta /proc y /tmp al terminar (limpieza).

    Al usar chroot(), el proceso hijo ve únicamente el filesystem del
    contenedor y no puede acceder al del host, igual que Docker.

    Raises:
        SystemExit: Si cualquier paso de configuración o el comando falla.
    """
    print(f"Running child {sys.argv[2:]} as {os.getpid()} (parent: {os.getppid()})")

    try:
        # Paso 1: configurar cgroups para limitar el número de procesos.
        cg()

        libc = ctypes.CDLL(None, use_errno=True)

        # Paso 2: cambiar el hostname dentro del namespace UTS.
        # Esto equivale al nombre del contenedor en Docker.
        libc.sethostname(b"focker", len("focker"))

        # Paso 3: chroot — cambia el directorio raíz del proceso al
        # filesystem del contenedor. A partir de aquí '/' apunta a
        # container_fs, no al '/' real del host.
        chroot_path = "/home/ubuntu/container_fs"
        libc.chroot(chroot_path.encode())
        os.chdir("/")  # necesario tras chroot para actualizar el cwd

        # Paso 4: montar sistemas de archivos virtuales dentro del contenedor.
        # /proc es indispensable para que herramientas como 'ps' funcionen.
        # /tmp se monta como tmpfs (en memoria) para almacenamiento temporal.
        libc.mount(b"proc", b"/proc", b"proc",  0, None)
        libc.mount(b"tmp",  b"/tmp",  b"tmpfs", 0, None)

        # Paso 5: ejecutar el comando solicitado por el usuario.
        # sys.argv[2:] contiene el comando y sus argumentos,
        # p.ej. ["bash"] o ["/bin/ls", "-la"].
        proc = subprocess.run(
            sys.argv[2:],
            stdin=sys.stdin,
            stdout=sys.stdout,
            stderr=sys.stderr
        )

        # Paso 6: limpiar los montajes antes de salir.
        # Evita que queden montajes huérfanos en el namespace.
        libc.umount2(b"/proc", 0)
        libc.umount2(b"/tmp",  0)

    except Exception as e:
        must(False, str(e))


# ---------------------------------------------------------------------------
# Configuración de cgroups
# ---------------------------------------------------------------------------

def cg():
    """
    Configura un cgroup v2 para limitar los recursos del contenedor.

    Los cgroups (control groups) son la segunda gran tecnología de Linux
    detrás de los contenedores (la primera son los namespaces). Permiten
    acotar CPU, memoria, I/O y el número de procesos de un grupo de tareas.

    Esta función:
      1. Crea el cgroup 'usuario' bajo la jerarquía cgroups v2.
      2. Limita a 25 el número máximo de PIDs dentro del cgroup.
      3. Añade el PID actual al cgroup (y con él, todos sus futuros hijos).

    El límite de PIDs (pids.max) es equivalente a la opción --pids-limit
    de Docker, que previene ataques de tipo fork-bomb dentro del contenedor.

    Raises:
        PermissionError: Si no se tiene acceso de escritura a /sys/fs/cgroup.
        FileNotFoundError: Si el sistema no tiene cgroups v2 montado.
    """
    # Raíz de la jerarquía unificada de cgroups v2 en Linux moderno.
    cgroups = Path("/sys/fs/cgroup/")

    # Subdirectorio que actuará como cgroup del contenedor.
    # Crear el directorio equivale a crear el cgroup en el kernel.
    container_cgroup = cgroups / "usuario"
    container_cgroup.mkdir(exist_ok=True, mode=0o755)

    # Limitamos el número de procesos/hilos activos en este cgroup a 25.
    # Escribir en pids.max es la interfaz del kernel para este control.
    (container_cgroup / "pids.max").write_text("25")

    # Añadimos el PID del proceso actual al cgroup.
    # Todos los procesos hijos heredarán automáticamente esta pertenencia.
    (container_cgroup / "cgroup.procs").write_text(str(os.getpid()))


# ---------------------------------------------------------------------------
# Punto de entrada
# ---------------------------------------------------------------------------

if __name__ == "__main__":
    # Validación mínima de argumentos: se requiere al menos el subcomando
    # ('run' o 'child') y el nombre de la imagen/comando.
    if len(sys.argv) < 3:
        msg("numero insuficiente de argumentos")

    # Despacho de subcomandos, similar al patrón CLI de Docker:
    #   focker run   → configura namespaces y lanza el hijo
    #   focker child → termina de configurar el contenedor y corre el proceso
    if sys.argv[1] == "run":
        run()
    elif sys.argv[1] == "child":
        child()
    else:
        msg("comando no reconocido")

