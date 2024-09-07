"""1. Eliminar duplicados de una lista:"""

def eliminar_duplicados(lista):
 
  conjunto_unico = set(lista)

  lista_sin_duplicados = list(conjunto_unico)

  return lista_sin_duplicados

# Ejemplo de uso:
mi_lista = [1, 2, 3, 2, 1, 5, 6, 5]
resultado = eliminar_duplicados(mi_lista)
print(resultado)


"""2. Adivinar un número con intentos limitados:"""""

import random

def adivinar_numero():
    """Juego de adivinar un número aleatorio entre 1 y 100.

    El usuario tiene 7 intentos para adivinar el número.
    """

    numero_secreto = random.randint(1, 100)
    intentos = 7

    while intentos > 0:
        intento = int(input("Adivina el número (entre 1 y 100): "))

        if intento == numero_secreto:
            print("¡Felicitaciones! Adivinaste el número.")
            break
        elif intento < numero_secreto:
            print("El número es mayor.")
        else:
            print("El número es menor.")

        intentos -= 1
        print(f"Te quedan {intentos} intentos.")

    if intentos == 0:
        print(f"Lo siento, se te acabaron los intentos. El número era {numero_secreto}.")

adivinar_numero()


"""3. Contar vocales en una frase:"""

def contar_vocales(frase):
  
  vocales = "aeiouAEIOU"
  contador = 0
  i = 0

  while i < len(frase):
    if frase[i] in vocales:
      contador += 1
    i += 1

  return contador

# Pedimos al usuario que ingrese una frase
frase = input("Ingrese una frase: ")

# Llamamos a la función para contar las vocales
num_vocales = contar_vocales(frase)

# Imprimimos el resultado
print("La frase contiene", num_vocales, "vocales.")



"""""4. Calculadora básica:"""


while True:
    # Pedimos al usuario que ingrese los números y la operación
    num1 = float(input("Ingrese el primer número: "))
    num2 = float(input("Ingrese el segundo número: "))
    operacion = input("Ingrese la operación (+, -, *, /): ")

    # Realizamos la operación según la elección del usuario
    if operacion == '+':
        resultado = num1 + num2
    elif operacion == '-':
        resultado = num1 - num2
    elif operacion == '*':
        resultado = num1 * num2
    elif operacion == '/':
        if num2 == 0:
            print("Error: División por cero")
        else:
            resultado = num1 / num2
    else:
        print("Operación inválida")
        continue

    # Mostramos el resultado
    if operacion in "+-*/":
        print("Resultado:", resultado)

    # Preguntamos si desea continuar
    continuar = input("¿Desea continuar? (s/n): ")
    if continuar.lower() != 's':
        break



    """""5. Crear una lista de números pares:"""

numeros_pares = []
contador = 2

while contador <= 100:
    numeros_pares.append(contador)
    contador += 2

print(numeros_pares)