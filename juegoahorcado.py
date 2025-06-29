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
    "ganada": False
}


# Función para jugar
def jugar():
    palabra_secreta = "carro"  # Puedes cambiar esto a cualquier palabra
    letras_adivinadas = []
    intentos = 6  # Número de intentos

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

        # Mostrar el progreso de la palabra
        progreso = ""
        for letra_secreta in palabra_secreta:
            if letra_secreta in letras_adivinadas:
                progreso += letra_secreta + " "
            else:
                progreso += "_ "

        print("Palabra:", progreso.strip())

        # Verificar si ganó
        if all(letra in letras_adivinadas for letra in palabra_secreta):
            print("¡Felicidades! Adivinaste la palabra:", palabra_secreta.upper())
            ultima_partida["palabra_secreta"] = palabra_secreta
            ultima_partida["intentos"] = 6 - intentos
            ultima_partida["letras_adivinadas"] = letras_adivinadas
            ultima_partida["ganada"] = True
            break

    # Si se quedó sin intentos
    if intentos == 0:
        print(f"Te quedaste sin intentos. La palabra era: {palabra_secreta.upper()}")
        ultima_partida["palabra_secreta"] = palabra_secreta
        ultima_partida["intentos"] = 6
        ultima_partida["letras_adivinadas"] = letras_adivinadas
        ultima_partida["ganada"] = False


# Función para mostrar las estadísticas de la última partida
def mostrar_estadisticas():
    if ultima_partida["palabra_secreta"] == "":
        print("Aún no has jugado ninguna partida.")
    else:
        print("Estadísticas de la última partida:")
        print(f"Palabra secreta: {ultima_partida['palabra_secreta']}")
        print(f"Intentos usados: {ultima_partida['intentos']}")
        print(f"Letras adivinadas: {', '.join(ultima_partida['letras_adivinadas'])}")
        if ultima_partida["ganada"]:
            print("Resultado: ¡Ganaste!")
        else:
            print("Resultado: Perdiste")


# Menú principal
def menu():
    while True:
        imprimir_encabezado()
        print("1. Jugar")
        print("2. Ver estadísticas de la última partida")
        print("3. Regresar al menú principal")

        try:
            opcion = int(input("Elige una opción (1-3): "))

            match opcion:
                case 1:
                    jugar()
                case 2:
                    mostrar_estadisticas()
                case 3:
                    print("¡Gracias por jugar! Regresando al menú principal.")
                    break
                case _:
                    print("Opción no válida, por favor elige un número entre 1 y 3.")
        except ValueError:
            print("Por favor, ingresa un número válido.")


# Llamada a la función de menú
if __name__ == "__main__":
    menu()