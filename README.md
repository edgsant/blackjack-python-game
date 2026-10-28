# Blackjack - Paradigmas de Programación (2023-2024)

Este repositorio contiene la implementación de un juego interactivo de **Blackjack** con interfaz gráfica de usuario (GUI), desarrollado como proyecto para la asignatura de **Paradigmas de Programación** durante el curso académico 2023-2024.

**Autores:**
* Edgar Santiesteban Mendo
* Daniel San Miguel Lopez

## 📝 Descripción

El proyecto consiste en un simulador de Blackjack completo desarrollado en Python. La interfaz gráfica ha sido construida utilizando la librería **wxPython** (con apoyo de wxGlade para el diseño inicial de los paneles). 

El juego incluye características avanzadas como:
* Gestión completa de manos (Pedir, Cerrar, Doblar, Separar).
* Sistema de apuestas iniciales y balance de ganancias/pérdidas.
* Temporizador (Timer) con límite de tiempo para tomar decisiones.
* Un modo "Automático" impulsado por un algoritmo de toma de decisiones (Estrategia) basado en las probabilidades del juego.
* Reproductor de medios integrado para música de fondo y efectos de sonido.

## ⚙️ Requisitos del Sistema

Para ejecutar este juego correctamente, necesitas tener instalados los siguientes componentes:

* **Python 3.10 o superior** (requerido por el uso de anotaciones de tipo modernas en la lógica interna).
* Sistema Operativo **Windows** (recomendado para la compatibilidad completa del motor de audio de *wx.media*).
* **wxPython** (Librería gráfica).

## 🚀 Instalación y Ejecución

1. **Clonar el repositorio:**
   ```bash
   git clone <URL_DEL_REPOSITORIO>
   cd <NOMBRE_DE_LA_CARPETA>
   ```

2. **Instalar dependencias:**
   Se recomienda usar un entorno virtual. Instala la librería gráfica ejecutando:
   ```bash
   pip install wxPython
   ```

3. **Ejecutar el juego:**
   Lanza el script principal del programa:
   ```bash
   python MyAppMain.py
   ```

## 🎵 Notas de la Versión y Compatibilidad

* **Rutas Relativas:** Las rutas de las imágenes y los sonidos han sido dinamizadas usando la librería `os` para evitar problemas de ejecución según el directorio de trabajo actual.
* **Audio en Windows:** El reproductor de música hereda de `wx.media.MediaCtrl` e invoca específicamente el backend de *Windows Media Player 10* (`wx.media.MEDIABACKEND_WMP10`). Si ejecutas el código en Linux o macOS, es posible que experimentes problemas con el audio de fondo.
* **Lógica Externa:** El motor de cartas y el mazo base utilizan el esqueleto base propuesto en la asignatura (`Codigo_Externo.py`), extendido y conectado a la interfaz por los autores.