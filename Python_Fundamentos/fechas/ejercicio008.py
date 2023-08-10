#"Modulos"

import datetime as dt

#Obtener La Fecha del Sistema
fecha_actual=dt.datetime.now()
#Mostrar el Año
#print(fecha_actual.year)
#Metodo strftime()

'''
	%b		Nombre del mes, versión corta
	%m		Número de mes [1,12]
	%d		Día de la semana
	%Y		Número de año
	%H		Hora [0,23]
	%h		hora [0,12]
	%p		PM/AM
	%M		Minuto
	%S		Segundo
	%f		microsegundo
	Entre otros...
'''
#Obtener el dia de la semana
#print(fecha_actual.strftime("%A"))
#Obtener el NOMBRE del mes
#print(fecha_actual.strftime("%B"))
#Obtener el Minuto de la fecha del sistema
#print(fecha_actual.strftime("%M"))

#Crear un elemento de tipo fecha
y=dt.datetime(2023,5,17)
#print(y)
print(type(y))#Datetime