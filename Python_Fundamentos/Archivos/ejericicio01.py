import csv
def aperturar_archivo():
    with open('datos.csv','r') as data_empleados:
        csv_leer=csv.reader(data_empleados)
        lista_empleados=list(csv_leer)
        return lista_empleados


print(aperturar_archivo())




