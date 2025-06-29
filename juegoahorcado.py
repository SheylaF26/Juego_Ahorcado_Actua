# Función para imprimir el encabezado del juego
def imprimir_encabezado():
    print("_________")
    print("|  JUEGO DE AHORCADO  |")
    print("|  ADIVINA LA PALABRA |")
    print("-----------------------")


# Variable global para almacenar estadísticas de la última partida
ultima_partida = {
    "palabra_secreta": "",
    "intentos": 0,
    "letras_adivinadas": [],
    "ganada": False,
    "modo": ""
}


# Función para jugar en modo individual (contra la computadora)
def jugar():
    palabra_secreta = "carro"  # Puedes cambiar esto o usar random.choice()
    letras_adivinadas = []
    intentos = 6

    while intentos > 0:
        letra = input("Ingresa una letra: ").lower()

        if len(letra) != 1 or not letra.isalpha():
            print("Por favor, ingresa solo una letra.")
            continue

        if letra in palabra_secreta:
            if letra not in letras_adivinadas:
                letras_adivinadas.append(letra)
                print("¡Bien! La letra está en la palabra.")
            else:
                print("Ya habías adivinado esa letra.")
        else:
            intentos -= 1
            print(f"Letra incorrecta. Te quedan {intentos} intentos.")

        progreso = ""
        for letra_secreta in palabra_secreta:
            if letra_secreta in letras_adivinadas:
                progreso += letra_secreta + " "
            else:
                progreso += "_ "

        print("Palabra:", progreso.strip())

        if all(letra in letras_adivinadas for letra in palabra_secreta):
            print("¡Felicidades! Adivinaste la palabra:", palabra_secreta.upper())
            ultima_partida["palabra_secreta"] = palabra_secreta
            ultima_partida["intentos"] = 6 - intentos
            ultima_partida["letras_adivinadas"] = letras_adivinadas
            ultima_partida["ganada"] = True
            ultima_partida["modo"] = "Individual"
            break

    if intentos == 0:
        print(f"Te quedaste sin intentos. La palabra era: {palabra_secreta.upper()}")
        ultima_partida["palabra_secreta"] = palabra_secreta
        ultima_partida["intentos"] = 6
        ultima_partida["letras_adivinadas"] = letras_adivinadas
        ultima_partida["ganada"] = False
        ultima_partida["modo"] = "Individual"


# Función para jugar en modo multijugador
def jugar_multijugador():
    print("\n--- MODO MULTIJUGADOR ---")
    jugador1 = input("Nombre del jugador 1 (elige la palabra): ")
    jugador2 = input("Nombre del jugador 2 (adivina la palabra): ")

    palabra_secreta = input(f"{jugador1}, ingresa la palabra secreta: ").lower()
    print("\n" * 50)  # Simula limpiar la pantalla

    letras_adivinadas = []
    intentos = 6

    while intentos > 0:
        letra = input(f"{jugador2}, ingresa una letra: ").lower()

        if len(letra) != 1 or not letra.isalpha():
            print("Por favor, ingresa solo una letra.")
            continue

        if letra in palabra_secreta:
            if letra not in letras_adivinadas:
                letras_adivinadas.append(letra)
                print("¡Bien! La letra está en la palabra.")
            else:
                print("Ya habías adivinado esa letra.")
        else:
            intentos -= 1
            print(f"Letra incorrecta. Te quedan {intentos} intentos.")

        progreso = ""
        for letra_secreta in palabra_secreta:
            if letra_secreta in letras_adivinadas:
                progreso += letra_secreta + " "
            else:
                progreso += "_ "

        print("Palabra:", progreso.strip())

        if all(letra in letras_adivinadas for letra in palabra_secreta):
            print(f"¡Felicidades {jugador2}! Adivinaste la palabra: {palabra_secreta.upper()}")
            ultima_partida["palabra_secreta"] = palabra_secreta
            ultima_partida["intentos"] = 6 - intentos
            ultima_partida["letras_adivinadas"] = letras_adivinadas
            ultima_partida["ganada"] = True
            ultima_partida["modo"] = f"Multijugador ({jugador1} vs {jugador2})"
            break

    if intentos == 0:
        print(f"Lo siento, {jugador2}. Te quedaste sin intentos. La palabra era: {palabra_secreta.upper()}")
        ultima_partida["palabra_secreta"] = palabra_secreta
        ultima_partida["intentos"] = 6
        ultima_partida["letras_adivinadas"] = letras_adivinadas
        ultima_partida["ganada"] = False
        ultima_partida["modo"] = f"Multijugador ({jugador1} vs {jugador2})"


# Función para mostrar estadísticas de la última partida
def mostrar_estadisticas():
    if ultima_partida["palabra_secreta"] == "":
        print("Aún no has jugado ninguna partida.")
    else:
        print("\n📊 Estadísticas de la última partida:")
        print(f"Modo: {ultima_partida['modo']}")
        print(f"Palabra secreta: {ultima_partida['palabra_secreta']}")
        print(f"Intentos usados: {ultima_partida['intentos']}")
        print(f"Letras adivinadas: {', '.join(ultima_partida['letras_adivinadas'])}")
        print("Resultado:", "¡Ganaste!" if ultima_partida["ganada"] else "Perdiste")


# Menú principal
def menu():
    while True:
        imprimir_encabezado()
        print("1. Jugar (modo individual)")
        print("2. Ver estadísticas de la última partida")
        print("3. Salir")
        print("4. Jugar modo multijugador")

        try:
            opcion = int(input("Elige una opción (1-4): "))

            match opcion:
                case 1:
                    jugar()
                case 2:
                    mostrar_estadisticas()
                case 3:
                    print("¡Gracias por jugar! Hasta la próxima.")
                    break
                case 4:
                    jugar_multijugador()
                case _:
                    print("Opción no válida, por favor elige un número entre 1 y 4.")
        except ValueError:
            print("Por favor, ingresa un número válido.")


# Punto de entrada del programa
if __name__ == "__main__":
    menu()