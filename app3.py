# 1 Diccionario para almacenar los datos de los alumnos
alumnos = {}

# Bucle para ingresar varios alumnos
while True:
    # Pedir nombre del alumno
    nombre = input("Ingrese el nombre del alumno ( 'salir' para terminar): ")
    if nombre.lower() == 'salir':
        break
    
    # Pedir apellido del alumno
    apellido = input("Ingrese el apellido del alumno: ")
    
    
    while True:
        try:
            nota = float(input("Ingrese nota del alumno (del 1 al 10): "))
            if 1 <= nota <= 10:
                break
            else:
                print("La nota debe estar entre 1 y 10.")
        except ValueError:
            print("Por favor, ingrese un valor numérico válido.")
            
    
   # Guardar los datos en el diccionario
    alumnos[f"{nombre} {apellido}"] = nota

# Mostrar todos los alumnos y sus notas
print("\nDiccionario de alumnos y sus notas:")
for alumno, nota in alumnos.items():
    print(f"{alumno}: {nota}") 
    

#2 Calcular el promedio de las notas de un diccionario:

def promedio_notas(alumnos):
    # Verificar si el diccionario no está vacío
    if not alumnos:
        return 0
    
    # Inicializar suma de notas
    suma_notas = 0
    
    # Recorrer el diccionario y sumar todas las notas
    for nota in alumnos.values():
        suma_notas += nota
    
    # Calcular el promedio
    promedio = suma_notas / len(alumnos)
    
    return promedio

#alumnos = {"Juan Pérez": 8.5, "Ana Gómez": 9.2, "Luis Martínez": 7.0}

# promedio = promedio_notas(alumnos)
# print(f"El promedio de las notas es: {promedio:.2f}")

#3 Encontrar al alumno con la nota más alta:

def alumno_con_mejor_nota(alumnos):
    # Verificar si el diccionario no está vacío
    if not alumnos:
        return None
    
    # Inicializar variables para el mejor alumno y la nota más alta
    mejor_alumno = None
    nota_mas_alta = float('-inf')  # El valor más bajo posible para comparar

    # Recorrer el diccionario
    for alumno, nota in alumnos.items():
        # Si la nota actual es mayor que la nota más alta registrada
        if nota > nota_mas_alta:
            nota_mas_alta = nota
            mejor_alumno = alumno
    
    return mejor_alumno

# alumnos = {"Juan Pérez": 8.5, "Ana Gómez": 9.2, "Luis Martínez": 7.0}

#mejor_alumno = alumno_con_mejor_nota(alumnos)
#print(f"El alumno con la mejor nota es: {mejor_alumno}")

# 4 Crear un diccionario de palabras y sus definiciones:

# Crear un diccionario vacío para almacenar las palabras y sus definiciones
diccionario = {}

# Bucle para ingresar varias palabras
while True:
    # Pedir palabra
    palabra = input("Ingrese una palabra (o escriba 'salir' para terminar): ")
    if palabra.lower() == 'salir':
        break
    
    # Pedir definición
    definicion = input(f"Ingrese la definición de '{palabra}': ")
    
    # Guardar la palabra y su definición en el diccionario
    diccionario[palabra] = definicion

# Mostrar todas las palabras y sus definiciones
print("\nDiccionario de palabras y sus definiciones:")
for palabra, definicion in diccionario.items():
    print(f"{palabra}: {definicion}")
    
# Ingrese una palabra (o escriba 'salir' para terminar): gato
# Ingrese la definición de 'gato': Mamífero carnívoro doméstico.
# Ingrese una palabra (o escriba 'salir' para terminar): casa
# Ingrese la definición de 'casa': Construcción destinada a ser habitada.
# Ingrese una palabra (o escriba 'salir' para terminar): salir


# 5 Buscar una palabra en un diccionario:

def buscar_palabra(diccionario, palabra):
    # Usar el método get() para buscar la palabra en el diccionario
    definicion = diccionario.get(palabra)
    
    # Si la palabra se encuentra, devolver su definición
    if definicion:
        return f"Definición de '{palabra}': {definicion}"
    
    # Si no se encuentra, devolver un mensaje indicando que no está
    return f"La palabra '{palabra}' no se encontró en el diccionario."

## Crear un diccionario de ejemplo
diccionario = {
    "gato": "Mamífero carnívoro doméstico.",
    "casa": "Construcción destinada a ser habitada.",
    "árbol": "Planta perenne de tallo leñoso."
}

#resultado = buscar_palabra(diccionario, palabra_a_buscar)
#print(resultado)


#palabra_a_buscar = "perro"
#resultado = buscar_palabra(diccionario, palabra_a_buscar)
#print(resultado)#palabra_a_buscar = "gato"

