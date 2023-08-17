#Modulo que me permitira acceder al archibo CSV
import csv
def aperturar_archivo():
    with open('cinema.csv','r') as data_cinema:
        csv_leer=csv.reader(data_cinema)
        lista_empleados=list(csv_leer)
        return lista_empleados