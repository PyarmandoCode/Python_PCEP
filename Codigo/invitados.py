"""
todo Realizar un Script que me permita añadir
Invitados a Una Lista
"""
acepta=True
lista=[]

while acepta==True:
    invitado=input("Ingrese el Nombre del Invitado al curso:")
    lista.append(invitado)
    adiciona=input("Desea Agregar Otro Invitado:(S/N)")
    if adiciona == 'S':
        acepta=True
    elif adiciona=='N':
        print('Invitados: {}'.format(lista))
        print('La Cantidad total de Invitados es {}'.format(len(lista)))
        break
    else:
        print("Opcion no Valida")
        break

    


