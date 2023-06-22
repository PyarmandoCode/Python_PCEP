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