#Metodos en Listas

mi_lista=[]


#mi_lista.append(6) #Añadir elementos al final de la lista
#mi_lista.insert(2,200) #Añadir elementos a tu lista indicandole la posicion
#mi_lista.remove(2) #Eliminar elemntos de la lista por su indice
#size=len(mi_lista) #totalizar los elementos de una Lista
mi_lista.extend([20,2,3,5,7,8,5,5]) #Añadir n elementos a una lista origen
#cant=mi_lista.count(5)#Cuenta los valores que coincidan en el argumento
#mi_lista.sort()#Ordenar elementos de una lista
mi_lista.reverse()#Ordenar elementos de forma reversa
#print(mi_lista)

#Recorre una Lista
# for x in mi_lista:
#     print(x)

#Zip para zipear dos o n listas de manera bidi
mi_lista = [1,2,3,4,5]
mi_lista2 = [5,6,7,8]
for elem1,elem2 in zip(mi_lista,mi_lista2):
    print(elem1,elem2)





