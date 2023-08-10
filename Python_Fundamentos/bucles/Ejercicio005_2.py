mi_lista=[1,2,3,4,5,8]

# for elem in mi_lista:
#     if elem>6:
#         print("Encontrado")
#         break#el Break se esta ejecutando
# else:
#     print("No se encontro")    


# x = 5
# try:
#     while x <15:
#         if x % 2 == 0:
#             print("Numero Par encontrado")
#             break
#         print(x)
#         x +=1
#     else:
#         print("Todos los Numeros son impares")    
# except: #Capturar la Excepcion si existe el error
#     print("ocurrio un error")        
# else:
#     print("Cogido valido")    


cursos = {"100":"python","200":"django"}
try:
    clave=input("Ingrese la clave:")
    print(cursos[clave])
except KeyError as msg_error:
    print(f"Lo Siento {msg_error} no es una clave valida")    
finally:
    print("Se completo el proceso correctamente")    
