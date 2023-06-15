#PCEP-30-02 3.1 – Collect and process data using lists
ciudades =["Lima","Quito","La Paz","Bogota"] #Lista
paises = {"Perú":"Lima","Ecuador":"Quito","Bolivia":"La Paz","Colombia":"Bogota"} #Diccionarios
costumbres=("Caminar","Bailar","Deporte") #tuplas =Inmutables
habitantes={"20500","30000","8000"}#sets #ordenados


#Crud de Datos = Create ,Read,Update,Delete
#Insercion de Elementos
#ciudades.append("Santiago")
#ciudades.append("Arequipa")
#Insertarlo en cualquier posicion
#ciudades.insert(3,"Trujillo")
#Eliminar Elementos de una Lista
#ciudades.pop(3)
#ciudades.remove("Bogota")
#del ciudades[3]
#ciudades.clear()
#Actualizar elemento de ls lista
#ciudades[0]="Cuzco"
#La cantidad de elementos de una Lista
#print(len(ciudades))
#Rango de Valores
#nuevas_ciudades=ciudades[1:3]
#print(nuevas_ciudades)
#ciudades =["Lima","Quito","La Paz","Bogota"] #Lista
#nuevas_ciudades=ciudades[1:]
#print(nuevas_ciudades)
#nuevas_ciudades=ciudades[-1:]
#print(nuevas_ciudades)
#Checkear Elementos
#existe = 'Santiago' in ciudades
#print(existe)
# ciudad=input("Ingresar la Ciudad:")
# if ciudad in ciudades:
#     print("La Ciudad Ya Existe en la Lista")  
# else:
#     ciudades.append(ciudad)
#     print("Se Añdio la Ciudad Correctamente")
#     print(ciudades)

#ordenar Listas
ciudades.sort(reverse=True)
#ciudades.reverse()


#Listado de Elementos
for item in ciudades:
     print(item)



