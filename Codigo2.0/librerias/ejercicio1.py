import pyfiglet
import random


def mensaje_a_imprimir(msj):
    fuentes = pyfiglet.FigletFont.getFonts()
    fuente_seleccionado = random.choice(fuentes)
    ascii_char = pyfiglet.figlet_format(msj, font=fuente_seleccionado)
    return ascii_char


def crear_rectangulo(rows, cols):
    for i in range(rows):
        for j in range(cols):
            if i == 0 or i == rows - 1 or j == 0 or cols - 1:
                print("*", end=" ")
            else:
                print(" ", end=" ")
        print()


def resultado(valor):
    match valor:
        case "A":
            print("Excelente")
        case "B":
            print("Buen Trabajo")
        case "C":
            print("Aprobastes con lo Justo")
        case _:
            print("Vuelva a intentarlo")


#resultado("B")
#crear_rectangulo(5, 5)
# print(mensaje_a_imprimir("Feliz Dia del Padre"))
