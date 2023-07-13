def funcion1():
    print("Bienvenido al Sistema")

def acceso(clave):
    clavesis="admin123"
    if clave == clavesis:
        resultado="Bienvenido al Sistema"
    else:
        resultado="Error en el Acceso"   
    return resultado     

def msj(nombre,mensaje="Adios"):
    saludo=mensaje + " " +nombre
    return saludo

def cambio_pesos(valordolar,monto):
    total = monto * valordolar
    return total

#print(cambio_pesos(3.60,2500))
#print(msj("Armando"))
#clave=input("ingrese la clave:")
#print(acceso(clave))
#Invocar a la funcion
#funcion1()

