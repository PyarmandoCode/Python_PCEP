from data import aperturar_archivo

#print(aperturar_archivo())

#Mostrar las peliculas que existen por pais

def pelicula_por_pais(cartelera,paisp):
    peliculas_pais=[]
    for mes,pais,pelicula,ano,salas in cartelera:
        if pais==paisp:
            peliculas_pais.append((pelicula,pais,ano,mes))
    return peliculas_pais        

pais = input("Ingrese el Pais a Filtrar:")
print(pelicula_por_pais(aperturar_archivo(),pais))

