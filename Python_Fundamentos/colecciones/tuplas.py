#Principal diferencia con las Listas  es que las tuplas son Inmutables
#Seteando las Tuplas = Inicializando
tupla= ()
tupla2 = tuple()

tupla = (1,2,3,4) #tuple
tupla1 = 5,6,7,8 #tuple

#print(type(tupla))
#print(type(tupla1))
#print(tupla[3]) #4

#tupla[1]=23
#print(len(tupla)) #Tamaño de la Tupla

#Seleccionar Porciones de la Tupla


tupla = (1,2,3,4,12,34,56,78,12,34,56) #tuple
#print(tupla[-2]) #Devuelve 3
#print(tupla[5:8])#Devuelve (34, 56, 78)
#print(tupla[2:]) #Devuelve (3, 4, 12, 34, 56, 78, 12, 34, 56)
#print(tupla[:2]) #Devuelve (1,2)
#print(tupla[0:2]) #Devuelve (1,2)

frutas =("manzanas","fresas","uvas")
#print(frutas)
# for items in frutas:
#     print(items)


buscar=input("Ingrese el Valor a Buscar:")
if buscar in frutas:
    print("Si encontro el el valor")
else:
    print("NO encontro el el valor")

