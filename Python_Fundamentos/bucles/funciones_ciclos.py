def mostrar_patron(num_filas,char):
    for i in range(num_filas):
        for num_cols in range(num_filas-i):
            print(char,end="")
        print()    


mostrar_patron(20,"A")        