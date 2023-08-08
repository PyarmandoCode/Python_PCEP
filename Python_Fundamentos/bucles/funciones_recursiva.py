def fibonacci(n):
    if n==0 or n ==1:
        return n
    else:
        return fibonacci(n-1)+fibonacci(n-2)
    

def factorial(n):
    if n==0 or n ==1:
        return n
    else:
        return n*factorial(n-1)
    

def calcular_potencia(a,b):
    if b==0:
        return 1
    else:
        return a * calcular_potencia(a,b-1)

#print(calcular_potencia(8,4))