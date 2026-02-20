
## Actualizar lista de paquetes disponibles

Sincroniza la lista de paquetes y sus versiones disponibles en los repositorios configurados con los servidores de Ubuntu. 

Este comando no actualiza el sistema, sino que refresca la caché local de paquetes para que el gestor de paquetes `apt` conozca las últimas versiones y dependencias disponibles. Es el primer paso esencial antes de instalar o actualizar cualquier software.

```bash
sudo apt update
```

## Actualizar paquetes instalados

Descarga e instala las versiones más recientes de todos los paquetes que ya están instalados en el sistema, utilizando la lista de paquetes actualizada previamente por `apt update`. 

La opción `-y` responde automáticamente "sí" a la confirmación de la instalación, lo que permite que el proceso continúe sin intervención manual, algo útil para scripts o configuraciones automáticas.

```bash
sudo apt upgrade -y
```

## Instalar paquetes específicos

A continuación se presenta una selección de paquetes que proporcionan un entorno de desarrollo completo para aprender múltiples lenguajes, trabajar con diferentes herramientas profesionales, personalizar el entorno de trabajo y desarrollar habilidades con herramientas **CLI** modernas utilizadas en la industria. 

Cada grupo satisface necesidades específicas del flujo de trabajo de desarrollo, desde la escritura de código hasta el monitoreo del sistema y la automatización de tareas.

```bash
sudo apt install -y \
    build-essential manpages-dev just \
    python3 python3-pip python3-venv \
    default-jdk default-jre \
    dotnet-sdk-8.0 aspnetcore-runtime-8.0 \
    ruby lua5.4 \
    rustc nodejs npm \
    golang-go \
    php \
    mycli pgcli litecli \
    ncal zip unzip rar unrar \
    nano joe ne ne-doc jed tilde hexyl vim neovim \
    git duf direnv progress \
    zsh byobu tree \
    lsd eza bat zoxide \
    htop btop bpytop glances gping \
    fortunes fortunes-es figlet toilet cowsay lolcat neofetch \
    tldr hstr fzf fd-find fdclone ripgrep jq \
    wget httpie curl \
    mc khal miller \
    socat pv stress-ng
```

#### Paquetes

- **`build-essential`**: Paquete meta que incluye compiladores C/C++ (`gcc`, `g++`), `make` y otras herramientas esenciales para compilar software desde código fuente.
- **`manpages-dev`**: Páginas del manual para funciones de desarrollo y programación en C.
- **`just`**: Ejecutor de comandos moderno, similar a `make`, para definir y ejecutar tareas de desarrollo.
- **Python** (`python3`, `python3-pip`, `python3-venv`): Intérprete Python, gestor de paquetes Pip y módulo para crear entornos virtuales.
- **Java** (`default-jdk`, `default-jre`): Kit de Desarrollo de Java (JDK) y Entorno de Ejecución (JRE) por defecto.
- **.NET** (`dotnet-sdk-8.0`, `aspnetcore-runtime-8.0`): SDK de .NET 8.0 y runtime para aplicaciones ASP.NET Core.
- **Ruby, Lua, Rust, Node.js, Go, PHP**: Intérpretes/compiladores y herramientas básicas para estos lenguajes populares.
- **`mycli`**, **`pgcli`**, **`litecli`**: Clientes interactivos con autocompletado y resaltado de sintaxis para MySQL, PostgreSQL y SQLite respectivamente.
- **`ncal`**: Calendario en terminal con formato alternativo.
- **`zip`**, **`unzip`**, **`rar`**, **`unrar`**: Herramientas para comprimir y descomprimir archivos en formatos ZIP y RAR.
- **`nano`**, **`joe`**, **`ne`**, **`jed`**, **`tilde`**, **`vim`**, **`neovim`**: Ofrece múltiples opciones de editores en terminal para diferentes preferencias.
- **`hexyl`**: Visor hexadecimal en color, útil para analizar archivos binarios.
- **`git`**: Sistema de control de versiones distribuido, esencial para desarrollo colaborativo.
- **`duf`**: Utilidad para visualizar uso de disco con interfaz amigable.
- **`direnv`**: Carga variables de entorno automáticamente al entrar en directorios.
- **`progress`**: Muestra el progreso de comandos en ejecución (cp, mv, dd, etc.).
- **`zsh`**: Shell poderosa y altamente personalizable (base para frameworks como Oh My Zsh).
- **`byobu`**: Interfaz mejorada para GNU Screen o Tmux, permitiendo múltiples sesiones en una terminal.
- **`tree`**: Muestra el árbol de directorios/archivos.
- **`lsd`**, **`eza`**: Reemplazos modernos para `ls` con iconos y mejor formato.
- **`bat`**: Reemplazo de `cat` con resaltado de sintaxis, numeración y paginación.
- **`zoxide`**: Reemplazo inteligente de `cd` que aprende los directorios más usados.
- **`htop`**, **`btop`**, **`bpytop`**, **`glances`**: Monitores de sistema con interfaces visuales mejoradas.
- **`gping`**: Herramienta de ping con gráficos en tiempo real.
- **`fortunes`**, **`fortunes-es`**: Muestra frases aleatorias al iniciar sesión.
- **`figlet`**, **`toilet`**: Crea letras grandes ASCII a partir de texto.
- **`cowsay`**: Dibuja una vaca (u otros animales) que "dice" un mensaje.
- **`lolcat`**: Añade arcoíris al texto.
- **`neofetch`**: Muestra información del sistema con un logo ASCII.
- **`tldr`**: Páginas de ayuda simplificadas con ejemplos prácticos.
- **`hstr`**: Historial de comandos interactivo y buscable.
- **`fzf`**, **`fd-find`**, **`fdclone`**, **`ripgrep`**: Herramientas de búsqueda rápidas y eficientes.
- **`jq`**: Procesador de JSON desde línea de comandos.
- **`wget`**, **`curl`**: Descargadores de contenido web.
- **`httpie`**: Cliente HTTP amigable con sintaxis simple.
- **`mc`**: Administrador de archivos en modo texto (Midnight Commander).
- **`khal`**: Calendario y agenda en terminal.
- **`miller`**: Procesador de datos tipo CSV/JSON/XML similar a awk/sed.
- **`socat`**: Herramienta multipropósito de red (similar a netcat pero más potente).
- **`pv`**: Monitor de progreso para tuberías de datos.
- **`stress-ng`**: Herramienta avanzada para someter el sistema a estrés (CPU, memoria, disco, red, etc.) y realizar pruebas de estabilidad, resistencia y benchmarking.

## Agregar repositorio externo (PPA) e instalar herramienta

Primero agrega el PPA (Personal Package Archive) de [OneFetch](https://onefetch.dev) a la lista de fuentes de software del sistema, y luego instala la aplicación:

```bash
sudo add-apt-repository ppa:o2sh/onefetch
```

```bash
sudo apt install -y onefetch 
```

## Eliminar paquetes innecesarios.

Elimina automáticamente los paquetes que fueron instalados como dependencias de otros paquetes pero que ya no son necesarios, ya que el paquete principal fue desinstalado o sus dependencias cambiaron. 

Este comando es una buena práctica de mantenimiento del sistema, ya que libera espacio en disco y mantiene el entorno limpio. Nota importante: Pide confirmación antes de proceder, por lo que es seguro ejecutarlo.

```bash
sudo apt autoremove
```

## Limpiar caché de paquetes obsoletos.

Elimina los archivos de paquetes `.deb` descargados que están almacenados en la caché local (`/var/cache/apt/archives/`) y que ya no se pueden descargar de los repositorios (por ejemplo, versiones antiguas de paquetes que han sido actualizadas).

A diferencia de `apt clean` que borra toda la caché, este comando es más conservador y solo elimina lo que es definitivamente innecesario, liberando espacio en disco sin afectar la capacidad de reinstalar versiones actuales de los paquetes.

```bash
sudo apt autoclean
```

## Instalación Manual de Herramientas Adicionales

Estos comandos instalan herramientas que no están disponibles en los repositorios oficiales de **Ubuntu** o que requieren versiones más recientes. Se descargan directamente desde sus fuentes oficiales y se instalan manualmente.

```bash
sudo su -
```

```bash
cd /usr/local/bin
```

#### **croc - Transferencia segura de archivos entre computadores**

Descarga y ejecuta el script de instalación de **croc**, una herramienta de línea de comandos que permite transferir archivos de forma sencilla y segura entre computadores usando un código de par. Es especialmente útil para estudiantes que necesitan compartir proyectos o archivos de configuración sin depender de servicios en la nube.

```bash
curl https://getcroc.schollz.com | bash
```

#### **micro - Editor de texto moderno para terminal**

Instala **micro**, un editor de texto intuitivo y fácil de usar para la terminal, con atajos de teclado similares a editores gráficos (Ctrl+S para guardar, Ctrl+Q para salir). Ideal para estudiantes que están comenzando y encuentran otros editores demasiado complejos.

```bash
curl -L https://getmic.ro | bash
```

#### **Starship - Prompt de terminal personalizable y minimalista**

Instala **starship**, un prompt de terminal altamente personalizable, rápido y que muestra información contextual relevante (rama de Git, versión de Python/Node, etc.). Mejora la experiencia en terminal mostrando solo la información necesaria según el directorio actual.

```bash
curl -sS https://starship.rs/install.sh | sh
```

#### **Oh My Posh - Prompt de shell personalizable para cualquier terminal**

Configura **Oh My Posh**, un motor de prompts para shells que te permite personalizar por completo la apariencia de tu terminal. Muestra información contextual como rama Git, estado de comandos, versiones de lenguajes y más, con soporte para temas y colores en PowerShell, bash, zsh y otros.

```bash
curl -s https://ohmyposh.dev/install.sh | bash -s -- -d /usr/local/bin
```

#### **McFly - Reemplazo inteligente del historial de comandos**

Instala **mcfly**, que reemplaza el historial de comandos tradicional (`history`) con una interfaz de búsqueda tipo "fuzzy finder" y sugerencias inteligentes basadas en frecuencia y relevancia. Aprende de tus comandos más usados para hacer la navegación más eficiente.

```bash
curl -LSfs https://raw.githubusercontent.com/cantino/mcfly/master/ci/install.sh | sh -s -- --git cantino/mcfly
```

#### **cht.sh - Documentación y ejemplos de programación desde terminal**

Descarga el cliente de **cht.sh**, un servicio que proporciona ejemplos de código, "cheat sheets" y documentación accesible directamente desde la terminal. Perfecto para estudiantes que necesitan consultar rápidamente sintaxis o ejemplos de múltiples lenguajes.

```bash
curl -s https://cht.sh/:cht.sh | sudo tee /usr/local/bin/cht.sh
```

```bash
chmod +x cht.sh
```

#### **bottom - Monitor de sistema con interfaz gráfica en terminal**

Descarga e instala **bottom** (`btm`), un monitor de recursos del sistema (CPU, memoria, disco, red, procesos) con una interfaz moderna y personalizable. Ofrece visualizaciones que facilitan entender el rendimiento del sistema.

```bash
curl -LO https://github.com/ClementTsang/bottom/releases/download/0.12.3/bottom_0.12.3-1_amd64.deb
```

```bash
dpkg -i bottom_0.12.3-1_amd64.deb
```

#### **pandoc - Conversor universal de formatos de documentos**

Instala **pandoc**, una herramienta indispensable para convertir documentos entre múltiples formatos (Markdown, HTML, PDF, LaTeX, Word, etc.). Útil para estudiantes que necesitan generar documentación, informes o presentaciones desde archivos de texto plano.

```bash
curl -LO https://github.com/jgm/pandoc/releases/download/3.9/pandoc-3.9-1-amd64.deb
```

```bash
dpkg -i pandoc-3.9-1-amd64.deb
```

#### **fastfetch - Información del sistema minimalista y rápida**

Instala **fastfetch**, una alternativa más rápida y configurable a neofetch para mostrar información del sistema con logos ASCII. Ligero y altamente personalizable para mostrar solo la información que realmente importa.

```bash
curl -LO https://github.com/fastfetch-cli/fastfetch/releases/download/2.59.0/fastfetch-linux-amd64.deb
```

```bash
dpkg -i fastfetch-linux-amd64.deb
```

#### **zellij - Multiplexor de terminal moderno con paneles y pestañas**

Descarga y extrae **zellij**, un multiplexor de terminal con interfaz moderna que permite dividir paneles, crear pestañas y sesiones persistentes. Incluye características como modo "flotante" y plugins, siendo una alternativa contemporánea a tmux y screen.

```bash
curl -L https://github.com/zellij-org/zellij/releases/download/v0.43.1/zellij-x86_64-unknown-linux-musl.tar.gz | tar zxvf -
```

#### **curlie - Interfaz amigable para curl con sintaxis de httpie**

Descarga y extrae **curlie**, que combina la facilidad de uso de `httpie` con el poder y ubicuidad de `curl`. Proporciona una sintaxis más intuitiva para hacer peticiones HTTP, ideal para estudiantes que están aprendiendo APIs web y servicios REST.

```bash
curl -L https://github.com/rs/curlie/releases/download/v1.8.2/curlie_1.8.2_linux_amd64.tar.gz | tar zxvf -
```

#### **usql - Cliente SQL universal con soporte para múltiples bases de datos**

Descarga y extrae **usql**, un cliente de bases de datos que funciona con múltiples sistemas (PostgreSQL, MySQL, SQLite, SQL Server, Oracle, etc.) usando una interfaz unificada. Perfecto para estudiantes que trabajan con diferentes tecnologías de bases de datos.

```bash
curl -L https://github.com/xo/usql/releases/download/v0.19.26/usql-0.19.26-linux-amd64.tar.bz2 | tar jxvf -
```
#### Eliminar archivos de instalación

```bash
rm *.deb README* LICENSE*
exit
```

## Personalizar neofetch con Formato SIXEL

Estos comandos trabajan en conjunto para convertir una imagen al formato SIXEL (un formato de gráficos rasterizados compatible con terminales modernas) y luego utilizarla como logo personalizado en `neofetch`.

#### **Convertir imagen PNG a formato SIXEL**

Utiliza la herramienta `convert` de ImageMagick para transformar una imagen en formato PNG (`image.png`) al formato SIXEL. La opción `sixel:-` especifica el formato de salida SIXEL y el guión (`-`) indica que la salida debe ir a la terminal. El operador `>` redirige esta salida a un archivo llamado `image.six`. El formato SIXEL es especialmente útil para mostrar imágenes en terminales que lo soportan (como XTerm, mlterm, o WezTerm) sin necesidad de aplicaciones gráficas externas.

```bash
convert image.png sixel:- > image.six
```

#### **Usar imagen SIXEL como logo en neofetch**

Ejecuta **neofetch** utilizando la imagen convertida (`image.six`) como logo personalizado en lugar del logo ASCII por defecto del sistema. La opción `--sixel` especifica la ruta del archivo SIXEL a mostrar, y `--size 320px` ajusta el ancho de la imagen a 320 píxeles. Esto permite a los estudiantes personalizar completamente la apariencia de su neofetch con cualquier imagen, logotipo o arte ASCII convertido, añadiendo un toque único a su entorno de terminal.

```bash
neofetch --sixel image.six --size 320px
```

