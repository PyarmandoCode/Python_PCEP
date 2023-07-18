empleados=[
   {'codigo':'2334455','apellido':'Ruiz','nombre':'Armando','sueldo':7000,'area':'sistemas'},
   {'codigo':'2334456','apellido':'Gomez','nombre':'Pedro','sueldo':8800,'area':'sistemas'},
   {'codigo':'2334457','apellido':'Cespedes','nombre':'Javier','sueldo':9000,'area':'contabilidad'},
   {'codigo':'2334458','apellido':'Linares','nombre':'Oscar','sueldo':12000,'area':'contabilidad'},
   {'codigo':'2334459','apellido':'Palomino','nombre':'Maria','sueldo':170000,'area':'rrhh'},
   {'codigo':'2334460','apellido':'Prado','nombre':'Carlos','sueldo':270000,'area':'estadistica'}
]

def calcular_edad(nac):
    try:
        edad = 2023-nac
    except:
        print("Existe un error")     
    return edad

def buscar_empleado(bd):
    existe=False
    cod_emp=input("Ingrese el codigo del empleado:")
    for item in bd:
        if cod_emp ==  item['codigo']:
            print(f"El Sueldo del empleado {item['nombre']} " 
             + f"{item['apellido']} es {item['sueldo']}")
            existe=True
            break
    if existe == False:
        print("El Empleado no existe")       

            

