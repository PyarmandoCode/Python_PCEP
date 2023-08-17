#Calcular el Total a pagar de un producto

try:
    #Este es el cuerpo del Script
    des=0
    imp=0.18
    nombre_prod = input("Ingrese el Producto a comprar:")
    precio_prod=float(input("Ingrese el Precio del Producto a comprar:"))
    cantidad_prod=int(input("Ingrese la cantidad del producto:"))
    total = precio_prod * cantidad_prod
    if total>1000:
        des=total * 0.01
    else:
        des=0
    neto =  total - des
    total_imp= neto * imp
    total_bruto = neto + total_imp
    print(f"El Total a Pagar es:{total_bruto} con descuento {des} el impuesto es {total_imp}")
except ValueError:   
    print("Se debe ingresar datos Numericos")
else:
    print("La compra se realizo con exito")    
finally:
    print("Se cerraron todos los objetos")
        

