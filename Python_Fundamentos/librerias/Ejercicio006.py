import pyfiglet
import random

def generar_mensaje_bienvenida_discord(nombre):
    mensaje="Bienvenido"+" "+nombre
    fonts=pyfiglet.FigletFont.getFonts()
    selecionar_fuente=random.choice(fonts)
    ascii_chart=pyfiglet.figlet_format(mensaje,font=selecionar_fuente)
    return ascii_chart

print(generar_mensaje_bienvenida_discord("Luis"))