frutas = set()
frutas = {"manzanas","fresas","cerezas"}
print(type(frutas)) # class 'set'

frutas.add("platanos") #Agregar Items No Repetidos
frutas.add("platanos")

frutas.update(["naranja","sandia","coco"]) #Adicionar n elementos
frutas.remove("coco") #Eliminar items de una Tupla
#frutas[0]="PAPAYA" #No se puede modificar los items de un SET
print(frutas)

