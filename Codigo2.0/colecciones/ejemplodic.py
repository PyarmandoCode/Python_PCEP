#print("Diccionarios")

d = {
     "Yellow":"Amarillo",
     "Blue":"Azul",
     "Black":"Negro",
     "Pink":"Rosado"
}

#print(d)
#print(type(d))
#Busqueda de Valores
#print(d["Black"])
#print(d["Pink"])
#print(d["Blue"])

#Modificar Valores diccionario
d['Black']="White"
d.update({"Pink":"Rosado F"})

#Eliminar un Elemento del diccionario
del d['Black']
d.pop("Black")


clientes=[
   {'cuenta':'2334455','apellido':'Ruiz','nombre':'Armando','saldo':7000},
   {'cuenta':'2334456','apellido':'Gomez','nombre':'Pedro','saldo':8800},
   {'cuenta':'2334457','apellido':'Cespedes','nombre':'Javier','saldo':9000},
   {'cuenta':'2334458','apellido':'Linares','nombre':'Oscar','saldo':12000},
   {'cuenta':'2334459','apellido':'Palomino','nombre':'Maria','saldo':170000}
]

ingr_cuenta = input("Ingrese su numero de cuenta:")
for item in clientes:
    if ingr_cuenta==item['cuenta']:
        print('{} tu saldo actual es {}'.format(item['apellido'],item['saldo']))
        break



