import os
import sys
import subprocess
import ctypes
from pathlib import Path


def must(condicion, mensaje):
    if not condicion:
        msg(mensaje)


def msg(error):
    print(error)
    sys.exit(1)


def run():
    print(f"run {os.getpid()}: {sys.argv[:3]}")

    cmd = [
        sys.executable,
        os.path.abspath(__file__),
        "child",
        *sys.argv[3:]
    ]

    try:
        libc = ctypes.CDLL(None, use_errno=True)
        CLONE_NEWUTS = 0x04000000  # hostname y domainname
        CLONE_NEWPID = 0x20000000  # aislamiento de PIDs
        CLONE_NEWNS  = 0x00020000  # aislamiento de filesystem

        must(libc.unshare(CLONE_NEWUTS | CLONE_NEWPID | CLONE_NEWNS | CLONE_NEWNET) == 0, "creación de entorno aislado")

        # Ejecutar el proceso hijo
        proc = subprocess.run(
            cmd,
            stdin=sys.stdin,
            stdout=sys.stdout,
            stderr=sys.stderr
        )
        must(proc.returncode == 0, f"comando falla: {proc.returncode}")

    except Exception as e:
        msg(e)


def child():
    print(f"Running child {sys.argv[2:]} as {os.getpid()} (parent: {os.getppid()})")

    try:
        cg()

        libc = ctypes.CDLL(None, use_errno=True)
        libc.sethostname(b"focker", len("focker"))

        chroot_path = "/home/ubuntu/container_fs"
        libc.chroot(chroot_path.encode())
        os.chdir("/")

        libc.mount(b"proc", b"/proc", b"proc", 0, None)
        libc.mount(b"tmp", b"/tmp", b"tmpfs", 0, None)

        proc = subprocess.run(
            sys.argv[2:],
            stdin=sys.stdin,
            stdout=sys.stdout,
            stderr=sys.stderr
        )

        libc.umount2(b"/proc", 0)
        libc.umount2(b"/tmp", 0)

    except Exception as e:
        must(False, str(e))


def cg():
    cgroups = Path("/sys/fs/cgroup/")
    container_cgroup = cgroups / "usuario"
    container_cgroup.mkdir(exist_ok=True, mode=0o755)
    (container_cgroup / "pids.max").write_text("25")
    (container_cgroup / "cgroup.procs").write_text(str(os.getpid()))


if __name__ == "__main__":
    if len(sys.argv) < 3:
        msg("numero insuficiente de argumentos")

    if sys.argv[1] == "run":
        run()
    elif sys.argv[1] == "child":
        child()
    else:
        msg("comando no reconocido")

