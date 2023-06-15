import keyword
import random
#PCEP-30-02 2.2 – Perform different types of iterations
#Bucle For


# for num in range(1,10,2):
#     print(num,"Hola Mundo")
# print("Fin del bucle")


#Contadores y Acumuladores
# c=0
# sum=0
# for i in range(5):
#     valor=int(input("Ingrese Valores:")) #20,10,8,2,20
#     c +=1 #contador
#     sum +=valor #acumulando
# print("Cantidad de valores ingresados",c)    
# print("Suma de los valores",sum)    


# c=0
# sum=0
# for i in range(5):
#     notas=int(input("Ingrese Las Notas:")) #20,10,8,2,20
#     c +=1 #contador
#     sum +=notas #acumulando
# promedio=sum/c    
# if promedio>10.5:
#     print("Felicitaciones Usted aprobo el curso de PYTHON")
# else:
#     print("Ud Lamentablemente debera realizar un Examen de validacion")    
# print("El Promedio General",promedio)    


#cursos = ["PYTHON","DJANGO","FLASK","FAST_API",100,True,12.20]
#for valores in cursos:
#    print(valores)

#Bucle While
# i=0
# suma=0

# while i<=100:#Devolver True
#     print(i)
#     i=i+1
#     suma = suma +i #acumulador
# print(f"La Suma de los numeros es {suma}") 
# print("Fin del Bucle")   

contrasena="PCEP"
cont=0
while True:
    con=input("Ingrese la Contraseña:")
    if con == contrasena:
        print("Contraseña Correcta")
        break #Salir del Bucle
    else:
        print("Contraseña errada")
        cont +=1
        if cont==3:
            print("La Cuenta se ha Bloqueado intentelo en 24 Horas")
            break

#print(keyword.kwlist)

#numero_secreto=random.randint(1,100)
#print(numero_secreto)


# while True:
#     numero=int(input("Cual es el Numero Generado:"))
#     if numero==numero_secreto:
#         print("Genial Acertastes!!!")
#         break
#     else:
#         if numero_secreto>numero:
#             print("El Numero secreto es Mayor que {}".format(numero))
#         else:
#             print("El Numero secreto es Menor que {}".format(numero))    
#         print("No Acertastes")