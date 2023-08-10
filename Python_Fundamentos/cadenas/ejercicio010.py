unaCadena = 'Esta es una cadena de texto'
otraCadena = "Esta es otra cadena de texto"

a="""Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."""

#print(a[2:5]) #Rebanar
#print(len(a))

a="  Cadena de Texto "
#print(a.strip())#Eliminar espacios al inicio o al final del texto
#print(a.lower())#Minusculas
#print(a.upper())#Mayusculas

curso="El Curso de PYTHON inicia el Dia Lunes"
#print(curso.replace("PYTHON","FLASK"))#Reemplaza una subcadena de otra cadena
msj="PYTHON,FACIL"
#print(msj.split(","))#Dividir subcadenas en base a una instancia de separador(,)

estaCadena = "esta es una cadena de caracteres adicional esta"
# Coloca una mayúscula a la primera letra de la cadena
#print(estaCadena.capitalize())
# Contabilizar el número de ocurrencias de una subcadena
print(estaCadena.count("esta"))
