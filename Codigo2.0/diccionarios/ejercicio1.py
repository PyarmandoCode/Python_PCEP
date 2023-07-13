nombres=["Manuel","Pedro","Raul","Maria","Fidel"]
edad= [25,70,19,17,23]
union = {}

for i in range(0,5):
    #La Clave del Diccionario es el Nombre y el Valor es la edad
    union[nombres[i]] = edad[i]

def buscar_nombre():
    nombre=input("Ingrese el Nombre")
    resultado=union[nombre]
    return resultado

print(buscar_nombre())

