#Importando mis Modulos
from base_de_datos import espectadores


resp=""
ano_actuaL=2023
encontrar=False
while resp!="N":
    dni=input("Ingresar su numero de documento:")
    for item in espectadores:
        encontrar=True
        if (dni in item["dni"]):
            edad = ano_actuaL - item["nac"] #Calculando la edad
            if edad>=18 and 3 == item["dosis"]:
                asiento=input("Asignar un numero de asiento")
                item['asiento']=asiento
                print(f'se le asigno el asiento {asiento} al Espectador')
            else:
                print("El Espectador no cumnple con algunas de las condiciones")    
            resp=input("Desea Continuar<S/N>:")    
            if resp == 'N':
                break
print(espectadores)            

    

