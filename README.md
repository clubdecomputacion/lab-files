# Archivos para Actividades

Este repositorio contiene los archivos binarios, datasets y recursos necesarios para los laboratorios, talleres, videos y demás actividades ofrecidas por el [Club de Computación](https://github.com/clubdecomputacion). Los archivos están disponibles como *releases* para facilitar su descarga directa sin necesidad de clonar el repositorio completo.

## 1. Configurar Ubuntu 

El documento [Ubuntu Setup](ubuntu_setup.md) contiene los comandos necesarios para instalar los paquetes necesarios para usar [Ubuntu](https://docs.ubuntu.com/) como una estación de aprendizaje para computación, lenguajes de programación, bases de datos, y demás.

## 2. Archivos de Práctica

[Línea de Comandos](https://www.youtube.com/playlist?list=PLdVwAtxG2IU7eOKRqHVLC7DxiozYSICKV) es una serie de videos de YouTube para aprender a utilizar la línea de comandos (Linux, Macos o Windows con WSL). Este archivo contiene los directorios y archivos de ejemplo utilizados en la serie. Es un archivo [`tar`](https://tldr.inbrowser.app/pages/common/tar) comprimido con [`xz`](https://tldr.inbrowser.app/pages/common/xz), utiliza el siguiente comando para descargar (~70Mb, 2026-03-01) e instalar:

```bash
curl -L https://github.com/clubdecomputacion/lab-files/releases/download/cli/home.txz | tar Jxf -
```

---

## Notas

- No es necesario clonar este repositorio, solo debes descargar el archivo que necesitas desde _releases_.
- Los archivos pueden ser grandes, verifica antes de descargar.
- Algunos navegadores pueden requerir confirmación para descargas grandes.

### Descargar manual desde la página de *Releases*

1. Ve a la sección [`Releases`](https://github.com/clubdecomputacion/lab-files/releases) de este repositorio.
2. Encuentra el *release* correspondiente a la actividad que quieres hacer.
3. En la sección `Assets`, haz clic en el archivo que deseas descargar.

