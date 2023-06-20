# resultado= input("Ingrese el Resultado Obtenido:")
# if resultado == 'A':
#     print("Excelente")
# elif resultado == 'B':
#     print('Buen Trabajo')
# elif resultado == 'C':
#     print("Aprobastes con lo Justo")
# else:
#     print("Vuelva a Intentarlo")

resultado = input("Ingrese el Resultado Obtenido:")
match resultado:
    case "A":
        print("Excelente")
    case "B":
        print("Buen Trabajo")
    case "C":
        print("Aprobastes con lo Justo")
    case _:
        print("Vuelva a intentarlo")
