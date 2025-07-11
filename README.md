# Juego_Ahorcado


**Fecha del proyecto:** Junio de 2025  
**Objetivo:** Desarrollar una versión básica del clásico juego del ahorcado que funcione desde la consola y permita al jugador interactuar mediante un menú, guardar estadísticas de la última partida y reforzar conceptos fundamentales de programación en Python.

---

## ¿De qué trata este proyecto?

Este es un proyecto sencillo en **Python** que simula el tradicional **juego del ahorcado** en consola. El jugador debe adivinar una palabra secreta, letra por letra, antes de quedarse sin intentos. 

El juego incluye un **menú interactivo** y un sistema de **estadísticas** de la última partida jugada.

---

##  Funcionalidades principales del código

### 1. `imprimir_encabezado()`
Imprime el título decorativo del juego en la consola.

### 2. `jugar()`
- Define la palabra secreta (actualmente `"carro"`).
- Permite al usuario ingresar letras una por una.
- Muestra el progreso de la palabra conforme se adivinan letras.
- Gestiona los intentos restantes (máximo 6).
- Guarda la información de la partida en una variable global `ultima_partida`.

### 3. `mostrar_estadisticas()`
- Muestra las estadísticas de la última partida jugada:
  - Palabra secreta
  - Letras adivinadas
  - Número de intentos usados
  - Resultado (ganado o perdido)

### 4. `menu()`
- Muestra un menú con las siguientes opciones:
  - `1. Jugar`
  - `2. Ver estadísticas de la última partida`
  - `3. Regresar al menú principal`
- Usa estructura `match-case` para ejecutar la opción seleccionada.

---

##  ¿Cómo jugar?

1. Ejecuta el programa en un entorno como **PyCharm** o desde la terminal.
2. Se mostrará el menú principal.
3. Selecciona la opción **1** para comenzar a jugar.
4. Ingresa letras hasta adivinar la palabra o quedarte sin intentos.
5. Después de jugar, puedes ver las estadísticas seleccionando la opción **2**.

---

## Objetivo educativo

Este programa es ideal para practicar:
- Estructuras de control (`while`, `if`, `match-case`)
- Uso de listas y cadenas
- Gestión de variables globales
- Entrada y salida de datos desde consola
- Lógica básica de juegos

---
