# -*- coding: utf-8 -*-
"""
Created on Sun Dec 22 08:03:52 2024

@author: HP
"""

# Desarrollo: Estructura Iterativa - Bucle "while"

# Introducción:
# El bucle `while` ejecuta repetidamente un bloque de código mientras se cumpla una condición.
# Es importante evitar la ejecución de bucles infinitos.

# Ejemplo 1: Imprimir la tabla del 3
i = 1
while i <= 10:
    print(f"3 x {i} = {3 * i}")
    i += 1  # Incrementar para evitar bucle infinito

# Ejemplo 2: Repetir una frase
def repetir_frase(frase, veces):
    contador = 1
    while contador <= veces:
        print(frase)
        contador += 1

frase = input("Ingrese una frase: ")
veces = int(input("¿Cuántas veces desea repetirla? "))
repetir_frase(frase, veces)

# Ejemplo 3: Validar contraseña
password_correcta = "1234"
intentos = 3
while intentos > 0:
    password = input("Ingrese la contraseña: ")
    if password == password_correcta:
        print("¡Contraseña correcta!")
        break
    else:
        intentos -= 1
        print(f"Contraseña incorrecta. Intentos restantes: {intentos}")

# Ejemplo 4: Validar nombre usando `break`
while True:
    nombre = input("Ingrese su nombre: ")
    if nombre.lower() == "rose":
        print("¡Nombre válido!")
        break
    else:
        print("Nombre incorrecto. Intente de nuevo.")

# Ejemplo 5: Validar nombre y contraseña usando `continue`
nombres_validos = ["rose", "jack", "anna"]
passwords_validos = ["1234", "abcd", "5678"]
while True:
    nombre = input("Ingrese su nombre: ").lower()
    if nombre not in nombres_validos:
        print("Nombre no válido. Intente nuevamente.")
        continue
    password = input("Ingrese su contraseña: ")
    if password in passwords_validos:
        print("¡Nombre y contraseña correctos!")
        break
    else:
        print("Contraseña incorrecta. Intente nuevamente.")
## EJEMPLOS
# Ejemplo 1: Buscar el número 2 en una lista

# Definimos la lista de valores
valores = [5, 1, 9, 2, 7, 4]

# Variables auxiliares
encontrado = False
indice = 0
longitud = len(valores)

# Bucle para buscar el número 2
while not encontrado and indice < longitud:
    valor = valores[indice]
    if valor == 2:
        encontrado = True
    else:
        indice += 1

# Verificamos si el número fue encontrado
if encontrado:
    print(f'El número 2 ha sido encontrado en el índice {indice}')
else:
    print('El número 2 no se encuentra en la lista de valores')
# Ejemplo 2: Solicitar ingreso de contraseña con intentos limitados

# Inicializamos las variables
password = ''
intentos = 0
MAX_INTENTOS = 5

# Bucle para verificar la contraseña
while password != '12345':
    intentos += 1
    password = input('Por favor, ingrese su contraseña: ')
    
    # Verificar si se alcanzaron los intentos máximos
    if intentos == MAX_INTENTOS:
        print('Finalizó los intentos...!')
        break

# Mensaje de éxito si la contraseña es correcta
if intentos != MAX_INTENTOS:
    print('¡Contraseña correcta!')
# Ejemplo 3: Secuencia 3n+1

# Definimos la función para generar la secuencia
def seq3np1(n):
    """
    Imprime la secuencia 3n+1 comenzando desde el número dado.
    La secuencia termina cuando el valor llega a 1.
    """
    while n != 1:
        print(n, end=", ")
        if n % 2 == 0:
            n = n // 2
        else:
            n = n * 3 + 1
    print(n, end=".\n")

# Solicitamos el número inicial al usuario
num = int(input('Ingrese un número de inicio n: '))
seq3np1(num)
# Ejemplo 4: Contar dígitos "0" y "5" en un número

# Definimos la función para contar los dígitos
def num_digi(n):
    """
    Cuenta los dígitos "0" y "5" en un número entero positivo.
    """
    count = 0
    while n > 0:
        digit = n % 10
        if digit == 0 or digit == 5:
            count += 1
        n = n // 10
    return count

# Solicitamos el número al usuario
num = int(input('Ingrese un número que contenga los dígitos "0" y "5": '))

# Llamamos a la función y obtenemos el resultado
cantidad = num_digi(num)

# Mostramos el resultado
print(f'\nLa cantidad de dígitos "0" y "5" en el número {num} es: {cantidad}')

