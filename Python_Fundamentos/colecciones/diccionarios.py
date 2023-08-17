mi_diccionario ={"a":1,"b":2,"c":3,"d":4}
#print(mi_diccionario)

#Metodos
#print(mi_diccionario.get("d")) #Get me trae el valor del Key
#print(mi_diccionario.keys()) #Me devuelve los Keys 
#print(mi_diccionario.values()) #Me devuelve los Values
#print(mi_diccionario.items()) #me devuelve la Key valor

mi_diccionario.update({"c":120})#Actualizar elementos del Diccionario
mi_diccionario["x"]=30 #Key existe lo reemplaza cuando no lo agrega
#mi_diccionario.clear()#Eliminar TODOS los elementos del diccionario
#mi_diccionario.pop("d")#Eliminar un Elemento del Diccionario
#print(mi_diccionario)

#Recorrer los diccionarios

mi_diccionario ={"a":1,"b":2,"c":3,"d":4}

print(mi_diccionario["d"])

# for clave in mi_diccionario:
#     print(clave)

# for valor in mi_diccionario.values():
#     print(valor)

# for clave,valor in mi_diccionario.items():
#     print(clave,valor)

# for valor in mi_diccionario.items():
#     print(valor)