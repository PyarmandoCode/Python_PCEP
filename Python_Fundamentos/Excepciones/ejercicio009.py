"""
try:
	# Codigo a ejecutar
	# Pero podria haber errores en este bloque
    
except <tipo de error>:
	# Haz esto para manejar la excepcion
	# El bloque except se ejecutara si el bloque try lanza un error
    
else:
	# Esto se ejecutara si el bloque try se ejecuta sin errores
   
finally:
	# Este bloque se ejecutara siempre

"""

#print(1/0) #ZeroDivisionError
#print(1+"e") #unsupported operand type(s)
d = {1:1,2:2}
#print(d[3]) #KeyError: 3
l= [1,2,3]
#print(l[4]) #IndexError:
#Capturando Excepciones
# try:
#     x= 2/0 #Bloque de codigo a evaluar
#     print(x)
# except:
#     print("A Ocurrido una Excepcion")    
# else:
#     print("No ha ocurrido una Excepcion")  
# finally:
#     print("Se cerraron los Objetos correctamente")      


while True:
    try:
        x = int(input("Digite un numero:"))
        break
    except ValueError:
        print("No se aceptan caracteres")



