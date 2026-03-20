# Archivos para Actividades

Este repositorio contiene los archivos binarios, datasets y recursos necesarios para los laboratorios, talleres, videos y demás actividades ofrecidas por el [Club de Computación](https://github.com/clubdecomputacion). Los archivos están disponibles como *releases* para facilitar su descarga directa sin necesidad de clonar el repositorio completo.

## 1. Configurar Ubuntu 

El documento [Ubuntu Setup](ubuntu_setup.md) contiene los comandos necesarios para instalar los paquetes necesarios para usar [Ubuntu](https://docs.ubuntu.com/) como una estación de aprendizaje para computación, lenguajes de programación, bases de datos, y demás.

## 2. Archivos de Práctica

[Línea de Comandos](https://www.youtube.com/playlist?list=PLdVwAtxG2IU7eOKRqHVLC7DxiozYSICKV) es una serie de videos de YouTube para aprender a utilizar la línea de comandos (Linux, Macos o Windows con WSL). Este archivo contiene los directorios y archivos de ejemplo utilizados en la serie. Es un archivo [`tar`](https://tldr.inbrowser.app/pages/common/tar) comprimido con [`xz`](https://tldr.inbrowser.app/pages/common/xz), utiliza el siguiente comando para descargar (~70Mb, 2026-03-01) e instalar:

```bash
curl -L https://github.com/clubdecomputacion/lab-files/releases/download/cli/home.txz | tar Jxf -
```

## 3. Videos

#### [Cómo funciona Docker? explicación desde cero con Python](https://www.youtube.com/watch?v=eXnGSGXwfT0)

- Código Python en el Video [`focker.py`](archivos/focker_no_doc.py)
- Código Python documentado [`focker.py`](archivos/focker.py)

Creación del directorio `container_fs` para el `chroot()`:

```
cd /home/usuario
wget https://cloud-images.ubuntu.com/noble/current/noble-server-cloudimg-amd64-root.tar.xz
mkdir container_fs
cd container_fs
tar Jxvf ../noble-server-cloudimg-amd64-root.tar.xz
cd ..
```
Cambia `usuario` si tu usuario se llama diferente.

## Notas

- No es necesario clonar este repositorio, solo debes descargar el archivo que necesitas desde _releases_.
- Los archivos pueden ser grandes, verifica antes de descargar.
- Algunos navegadores pueden requerir confirmación para descargas grandes.

### Descargar manual desde la página de *Releases*

1. Ve a la sección [`Releases`](https://github.com/clubdecomputacion/lab-files/releases) de este repositorio.
2. Encuentra el *release* correspondiente a la actividad que quieres hacer.
3. En la sección `Assets`, haz clic en el archivo que deseas descargar.

