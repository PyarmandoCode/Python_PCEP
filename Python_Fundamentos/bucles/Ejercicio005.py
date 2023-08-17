#Bucle For

# for vuelta in range(5,20,3):
#     print(vuelta,"Clase dos de Python")

# for vuelta in range(1,20,3):
#     print(vuelta,"Clase de Python")


# for vuelta in range(1,20):
#     if vuelta == 15:
#         break
#     else:
#         print(vuelta)

contraseña="admin123"
while True:
    ingreso=input("Ingrese su contraseña:")
    if ingreso==contraseña:
        print("Contraseña Correcta")
        break #True
    else:
        print("Contraseña Incorrecta")