mi_lista=[1,2,3,4,5,8]

# for elem in mi_lista:
#     if elem>6:
#         print("Encontrado")
#         break#el Break se esta ejecutando
# else:
#     print("No se encontro")    


x = 5
while x <15:
    if x % 2 == 0:
        print("Numero Par encontrado")
        break
    print(x)
    x +=1
else:
    print("Todos los Numeros son impares")    
