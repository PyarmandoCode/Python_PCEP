#Metodo Tradicional
nums = [1,2,3,4,5]
# cubes_and_squares=[]
# for num in nums:
#     if num % 2 ==0:
#         cubes_and_squares.append(num**3)
#     else:
#         cubes_and_squares.append(num**2)    

# print(cubes_and_squares)    

#Metodo Comprension de Listas
#Sintaxis:
cubes_and_squares=[num ** 3 if num %2 ==0 else num **2 for num in nums]
print(cubes_and_squares)