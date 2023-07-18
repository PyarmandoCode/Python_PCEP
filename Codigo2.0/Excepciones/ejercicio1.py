# Sintaxis

"""
try:
    #Codigo a ejecutar
    #pero podria haber errores en este bloque
except <tipo de error>:
    #Haz esto para manejar la excepcion
    #El Bloque except se ejecuta si el bloque try lanza un error
else:
    #Esto se ejecutara si el bloque try se ejecuta sin errores      
finally:
    #Este Bloque siempre se va a ejecutar    
"""

#print(1/0) #ZeroDivisionError
#print(1+"e") # TypeError unsupported operand type(s) for +: 'int' and 'str'
d = {1:1,2:2}
#print(d[3]) #KeyError
l = [1,2,3]
#print(l[4]) #IndexError
#print(l.foobar) #AttributeError

#Atrapando excepciones

while True:
    try:
        x=int(input("Digite un numero:"))
        break
    except ValueError:
        print("Debe Ingresar un Valor Valido")


