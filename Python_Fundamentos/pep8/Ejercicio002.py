#Not Recomendable
x = "Armando Ruiz"
y,z = x.split()
print(z,y,sep=', ')

#Recomendar
nombre = "Armando Ruiz"
primer_nombre,segundo_nombre=nombre.split()
# print(segundo_nombre,primer_nombre,sep=', ')


#Otro Ejemplo PEP8
#def db(x):
#    return x*2

#Recomendado
def multiplicar_por_dos(x):
    return x*2


#print(multiplicar_por_dos(5))

#Lineas MaximaS 79 Caracteres

def function(arg_one,arg_two,
             arg_three,arg_four):
    return arg_one


variable_uno=0
variable_dos=0
variable_tres=0

total = ( variable_uno
         + variable_dos
         - variable_tres)


#Sangrias
#Procesos Condicionales
x=3
if x>5:
    print("El numero es Mayor a 5")
elif x>10:
    print("El numero es Mayor a 10")
elif x>20:
    print("El numero es Mayor a 20")
else:
    print("El Numero no es Mayor a 5")    

#Procesos Repetitivos
for x in range(1,10):
    print("Python clase dos")
print("Fuera del bucle")    

def maximo(x):
    return x*2




