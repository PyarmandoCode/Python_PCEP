# todo Tipo de datos

"""
Comentarios en Varias Lineas
"""

curso_actual = "PYTHON"  # Str
profesor_curso = 'Armando Ruiz'  # Str
precio_curso = 1200.20  # Float
cantidad_participantes = 60  # Int
curso_abierto = True  # Bool

# todo Concatenado
# print("Cual es el curso que Llevo?:" + curso_actual)
# print("Cual es el curso que Llevo?:", curso_actual)
# print(f"Cual es el curso que Llevo?: {curso_actual} ")
# print("Cual es el curso que Llevo?: %s" % (curso_actual))

# print("Cual es el Precio del Curso?:" + str(precio_curso))
# print("Cual es el Precio del Curso?:" , precio_curso)
# print(f"Cual es el Precio del Curso {precio_curso}  y el Profesor {profesor_curso}")

# todo Castear
# print(type(str(precio_curso)))
# print(type(str(cantidad_participantes)))

# todo Funcion de Entrada de datos
# nombre_persona = input("Ingrese el Nombre de la Persona:")
# print(f"El Nombre de la Persona que se ingreso es {nombre_persona}")

# todo Programa de Cambio de divisas
# monto_cambiar = float(input("Ingrese el Monto de Pesos a cambiar en $"))
valor_dolar = 3.57
# total_dolares = monto_cambiar / valor_dolar
# print(f"El Total de Dolares que tienes en el bolsillo es {total_dolares}")
# print("El Total de Dolares que tienes en el bolsillo es %.3f" % total_dolares)

# todo Notacion Cientifica

# Todo Binario
num1 = "0b100"  # 4
num2 = "0b110"  # 6
sumar = int(num1, 2) + int(num2, 2)
#print(sumar)

# Todo Hexa
hnum1 = "0x10"  # 4
hnum2 = "0x10"  # 6
suma = int(hnum1, 16) + int(hnum2, 16)
print(suma)
