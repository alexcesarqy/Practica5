# -*- coding: utf-8 -*-
"""
Created on Sun Dec 22 11:01:49 2024

@author: HP
"""
#%% Ejercicio 1: Verificar números pares e impares en un rango
# Hacer un programa que ingrese por teclado un número inicial y un número final para generar un rango.
# Imprimir de cada número si es par o impar (recorrer la lista).
# Utilizando el operador % y while.

# Definimos la función para verificar paridad
def verificar_paridad(numero):
    """
    Verifica si un número es par o impar.
    """
    if numero % 2 == 0:
        return "par"
    else:
        return "impar"

# Solicitar números inicial y final
num_inicial = int(input("Ingrese el número inicial: "))
num_final = int(input("Ingrese el número final: "))

# Generar y recorrer el rango
print("\nResultados:")
while num_inicial <= num_final:
    resultado = verificar_paridad(num_inicial)
    print(f"El número {num_inicial} es {resultado}.")
    num_inicial += 1
#%% Ejercicio 2: Tabla de multiplicar de un número
# Hacer un programa que solicite un número.
# Imprima las tablas de multiplicar del 1 al 10 de dicho número.
# Utilizando while y funciones.

# Función para imprimir la tabla de multiplicar
def imprimir_tabla(numero):
    """
    Imprime la tabla de multiplicar de un número dado.
    """
    i = 1
    while i <= 10:
        print(f"{numero} x {i} = {numero * i}")
        i += 1

# Solicitar el número al usuario
num = int(input("Ingrese un número para imprimir su tabla de multiplicar: "))

# Imprimir la tabla
print("\nTabla de multiplicar:")
imprimir_tabla(num)
#%% Ejercicio 3: Validar nombre y apellido
# Hacer un programa que solicite el ingreso de un nombre y apellido:
# Verificar que no contengan números ni símbolos extraños.
# Si no son válidos, solicitar nuevamente.
# Utilizar while y funciones.

# Función para validar texto
def validar_nombre(texto):
    """
    Verifica si un texto contiene solo letras y espacios.
    """
    return texto.replace(" ", "").isalpha()

# Solicitar nombre y apellido
while True:
    nombre = input("Ingrese su nombre: ").strip()
    apellido = input("Ingrese su apellido: ").strip()

    if validar_nombre(nombre) and validar_nombre(apellido):
        print("\nNombre y apellido válidos.")
        break
    else:
        print("El nombre o apellido contiene caracteres no válidos. Intente nuevamente.")
#%% Ejercicio 4: Análisis de comentarios EPIT
# Solicitar un comentario de un alumno EPIT.
# Verificar si tiene palabras negativas (malo, pésimo, no) o positivas (bueno, excelente, bien).
# Utilizar listas, while y funciones.

# Listas de palabras clave
palabras_positivas = ["bueno", "excelente", "bien"]
palabras_negativas = ["malo", "pésimo", "no"]

# Función para analizar el comentario
def analizar_comentario(comentario):
    """
    Analiza si un comentario es positivo, negativo o neutro.
    """
    for palabra in palabras_negativas:
        if palabra in comentario.lower():
            return "Comentario NEGATIVO"
    for palabra in palabras_positivas:
        if palabra in comentario.lower():
            return "Comentario POSITIVO"
    return "Comentario NEUTRO"

# Solicitar comentarios al usuario
while True:
    comentario = input("Ingrese un comentario (o 'salir' para terminar): ").strip()
    if comentario.lower() == "salir":
        print("Programa finalizado.")
        break
    resultado = analizar_comentario(comentario)
    print(f"\nResultado: {resultado}")
#%% Ejercicio 5: Generar listas de múltiplos
# Hacer un programa que:
# - Genere una lista aleatoria de hasta 60 números.
# - Subdivida la lista en tres listas: múltiplos de 2, de 3 y de 5.
# - Utilice while y funciones.

import random

# Función para generar números aleatorios
def generar_lista(n, limite):
    return [random.randint(1, limite) for _ in range(n)]

# Función para verificar múltiplos
def es_multiplo(num, divisor):
    return num % divisor == 0

# Generar lista aleatoria
numeros = generar_lista(60, 100)

# Inicializar listas
multiplos_2, multiplos_3, multiplos_5 = [], [], []

# Recorrer la lista con while
i = 0
while i < len(numeros):
    if es_multiplo(numeros[i], 2):
        multiplos_2.append(numeros[i])
    if es_multiplo(numeros[i], 3):
        multiplos_3.append(numeros[i])
    if es_multiplo(numeros[i], 5):
        multiplos_5.append(numeros[i])
    i += 1

# Imprimir resultados
print("Números generados:", numeros)
print("Múltiplos de 2:", multiplos_2)
print("Múltiplos de 3:", multiplos_3)
print("Múltiplos de 5:", multiplos_5)
#%% Ejercicio 6: Números capicúa
# Hacer un programa que:
# - Solicite un número inicial de 3 cifras y un número final de 4 cifras.
# - Genere un rango y verifique si cada número es capicúa.

# Función para verificar capicúa
def es_capicua(numero):
    return str(numero) == str(numero)[::-1]

# Solicitar números inicial y final
while True:
    inicial = int(input("Ingrese un número inicial (3 cifras): "))
    final = int(input("Ingrese un número final (4 cifras): "))
    if 100 <= inicial <= 999 and 1000 <= final <= 9999:
        break
    else:
        print("Los números deben ser de 3 y 4 cifras, respectivamente.")

# Verificar números capicúa
numero = inicial
while numero <= final:
    if es_capicua(numero):
        print(f"{numero} es capicúa.")
    numero += 1
#%% Ejercicio 7: Validar DNI
# Hacer un programa que:
# - Solicite el ingreso del DNI.
# - Verifique que no contenga letras ni símbolos y tenga 8 dígitos.

# Función para validar DNI
def validar_dni(dni):
    return dni.isdigit() and len(dni) == 8

# Solicitar DNI
while True:
    dni = input("Ingrese su DNI: ").strip()
    if validar_dni(dni):
        print("\nDNI válido.")
        break
    else:
        print("El DNI no es válido. Intente nuevamente.")
