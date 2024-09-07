# 1. Sumar todos los elementos de una lista:

# Crea una función llamada suma_elementos que reciba una lista de números como parámetro y devuelva la suma de todos sus elementos.

# Pista: Puedes utilizar una variable para acumular la suma dentro del bucle "for".
numbers=[56,89,456,98,123,987,345]
def sumaElementos(numbers):
    result =0
    for number in numbers:
        result += number
    return result    

print('Esta es la suma de todos los numeros: ',sumaElementos(numbers))


# 2. Contar la cantidad de elementos pares en una lista:

# Crea una función llamada contar_pares que reciba una lista de números como parámetro y devuelva la cantidad de elementos pares que contiene.

# Pista: Dentro del bucle "for", puedes verificar si cada elemento es divisible por 2.

numeros =[2,3,7,10,35,38,12,13,15]
def contar_pares(numeros):
   contador=0
   for numero in numeros:
      if numero % 2 ==0:
        contador+=1 
   return contador
print('Esta es la cantidad de pares que se encuentra en la lista: ',contar_pares(numeros))


# 3. Encontrar el elemento más grande de una lista:

# Crea una función llamada elemento_mas_grande que reciba una lista de números como parámetro y devuelva el elemento más grande de la lista.

# Pista: Puedes utilizar una variable para almacenar el elemento más grande encontrado hasta el momento.
n_Numbers=[45,78,90,1234,129,567,345,890]

def elemento_mas_grande(n_Numbers):
   caja = 0
   for number in n_Numbers:
      if caja < number:
         caja =number

   return  caja  
print('El numero mas grande de la lista es: ',elemento_mas_grande(n_Numbers))

# Crea una función llamada multiplicar_elementos que reciba una lista de números como parámetro y devuelva una nueva lista con los elementos de la lista original multiplicados por 2.

# Pista: Puedes crear una nueva lista vacía y agregar los elementos musltiplicados por 2 dentro del bucle "for".
ori_numeros =[2,6,90,34,12,56,457,908]
def multiplicar_elementos(ori_numeros):
   new_numbers=[]
   multiplicacion =0
   for number in ori_numeros:
      multiplicacion = number*2
      new_numbers.append(multiplicacion)
   return new_numbers
print('Lista modificada',multiplicar_elementos(ori_numeros))

# Crea una función llamada invertir_lista que reciba una lista como parámetro y devuelva una nueva lista con los elementos de la lista original invertidos.

# Pista: Puedes agregar los elementos de la lista original en orden inverso a la nueva lista.
lista=['principio','papas',76,{'juan':34,'pedro':34},(2,5),'final']
def invertir_lista(lista):
   new_list=[]
   for element in lista:
      new_list.insert(0,element)
   return new_list
print(invertir_lista(lista))
   
    

      
      
      
      

   