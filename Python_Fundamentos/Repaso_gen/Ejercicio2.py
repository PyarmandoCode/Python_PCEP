msj = "n"
sumstotal=0
while True:
    nombre_prod = input("Ingrese el Producto a comprar:")
    precio_prod=float(input("Ingrese el Precio del Producto a comprar:"))
    cantidad_prod=int(input("Ingrese la cantidad del producto:"))
    subtotal = precio_prod*cantidad_prod
    sumtotal = sumstotal+subtotal #Acumulador
    msj=input("Deseas seguir comprando(s/n)")
    if msj.upper() =="N":
        print(f"Total a pagar {subtotal}")
        break #Salir de While
