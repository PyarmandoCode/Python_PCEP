nums=[1,2,3,4,5]
#Metodo Tradicional
cubes_of_even=[]
for num in nums:
    if num % 2 == 0:
        cubes_of_even.append(num**3)
print(cubes_of_even)        

#Comprension de Listas (list comprehension)
#Sintaxis:[expression for variable in iterable if condicion]
cubes_of_even=[num **3 for num in nums if num % 2==0]
print(cubes_of_even)




