# Ejercicios Repaso

'''Ejercicio 1: Calculadora Mejorada
Crea un programa que pida al usuario dos números y una operación (+, -, *, /).
Luego, usa una estructura if-elif-else para realizar la operación correspondiente.
Si el usuario introduce una operación no válida, muestra un mensaje de error.'''

print("===== Calculadora =====")
print("Opción 1: Sumar")
print("Opción 2: Restar")
print("Opción 3: Multiplicar")
print("Opción 4: Dividir")

while True:
    try:
        opcion = int(input("Elija una opción: "))
        if 1 <= opcion <= 4:
            break
        else:
            print("No existe esa opción")
        num1 = int(input("Introduzca un número: "))
        num2 = int(input("Introduzca otro número: "))
    except ValueError:
        print("Eso no es un número")

if opcion == 1:
    print(num1 + num2)
elif opcion == 2:
    print(num1 - num2)
elif opcion == 3:
    print(num1 * num2)
elif opcion == 4:
    print(num1 / num2)

    
    
    
'''Ejercicio 2: Contador de Vocales
Pide al usuario una palabra y cuenta cuántas vocales (a, e, i, o, u) tiene. Usa un
bucle for y una lista para almacenar las vocales.'''

palabra = input("Introduce una palabra: ")
vocales = ['a', 'e', 'i', 'o', 'u']
contador_vocales = 0

for letra in palabra:
    if letra.lower() in vocales:
        contador_vocales += 1

print(f"La palabra '{palabra}' tiene {contador_vocales} vocales.")

'''Ejercicio 3: Manipulación de Listas
Crea una lista con al menos 10 números. Luego:
● Muestra la lista original.
● Muestra solo los números pares.
● Muestra la suma de todos los números de la lista.
● Reemplaza todos los números impares por 0 y muestra la lista modificada.'''

numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print("Lista original:", numeros)

numeros_pares = [num for num in numeros if num % 2 == 0]
print("Números pares:", numeros_pares)

suma_numeros = sum(numeros)
print("Suma de todos los números:", suma_numeros)

lista_modificada = [num if num % 2 == 0 else 0 for num in numeros]
print("Lista modificada:", lista_modificada)

'''Ejercicio 4: Simulación de Login
Crea un programa que simule un inicio de sesión. Define un usuario y una contraseña
predefinidos. Luego, pide al usuario que ingrese su usuario y contraseña. Si son
correctos, muestra "Acceso concedido", de lo contrario, "Acceso denegado". Dale al
usuario 3 intentos antes de bloquear el acceso.'''

usuario_predefinido = "admin"
contrasena_predefinida = "1234"

intentos_restantes = 3

while intentos_restantes > 0:
    usuario = input("Introduce tu usuario: ")
    contrasena = input("Introduce tu contraseña: ")

    if usuario == usuario_predefinido and contrasena == contrasena_predefinida:
        print("Acceso concedido")
        break
    else:
        intentos_restantes -= 1
        print("Acceso denegado")
        if intentos_restantes > 0:
            print(f"Te quedan {intentos_restantes} intentos")
        else:
            print("Acceso bloqueado")


'''Ejercicio 5: Números Primos
Crea una función que reciba un número y determine si es primo o no. Luego, pide un
número al usuario y usa la función para decirle si es primo.'''

def es_primo(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

numero = int(input("Introduce un número: "))
if es_primo(numero):
    print(f"El número {numero} es primo.")
else:
    print(f"El número {numero} no es primo.")

'''Ejercicio 6: Ordenando una Lista
Pide al usuario 5 números, guárdalos en una lista y luego muestra:
● La lista ordenada de menor a mayor.
● La lista ordenada de mayor a menor.
● El número más grande y el más pequeño de la lista.'''

numeros = [int(input("Introduce un número: ")) for _ in range(5)]

print("Lista ordenada de menor a mayor:", sorted(numeros))
print("Lista ordenada de mayor a menor:", sorted(numeros, reverse=True))
print("Número más grande:", max(numeros))
print("Número más pequeño:", min(numeros))

'''Ejercicio 7: Adivina el Número
Crea un programa que genere un número aleatorio entre 1 y 20 y pida al usuario que
lo adivine.
● Si el usuario adivina, muestra un mensaje de felicitaciones.
● Si el número es menor, dile "El número es mayor".
● Si el número es mayor, dile "El número es menor".
● El usuario tiene 5 intentos.
💡 Pista: Usa import random y random.randint(1,20).'''

import random

numero_aleatorio = random.randint(1, 20)
intentos_restantes = 5

while intentos_restantes > 0:
    intento = int(input("Adivina un número entre 1 y 20: "))
    if intento == numero_aleatorio:
        print("¡Felicitaciones! Adivinaste el número.")
        break
    elif intento < numero_aleatorio:
        print("El número es mayor.")
    else:
        print("El número es menor.")
    intentos_restantes -= 1

if intentos_restantes == 0:
    print(f"Lo siento, se han agotado los intentos. El número era {numero_aleatorio}.")

'''Ejercicio 8: Convertidor de Temperaturas
Crea una función que convierta grados Celsius a Fahrenheit y otra que convierta
grados Fahrenheit a Celsius. Luego, pide al usuario un valor y la conversión que
quiere realizar.
💡 Fórmulas:
● °F = (°C × 9/5) + 32
● °C = (°F − 32) × 5/9'''

def celsius_a_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def fahrenheit_a_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

valor = float(input("Introduce el valor de la temperatura: "))
conversion = input("¿Quieres convertir a (F)ahrenheit o a (C)elsius? ")

if conversion.lower() == 'f':
    print(f"{valor}°C es igual a {celsius_a_fahrenheit(valor)}°F")
elif conversion.lower() == 'c':
    print(f"{valor}°F es igual a {fahrenheit_a_celsius(valor)}°C")
else:
    print("Opción de conversión no válida.")

'''Ejercicio 9: Conteo de Palabras en un Texto
Pide al usuario que introduzca un texto y luego:
● Cuenta cuántas palabras tiene.
● Cuenta cuántas veces aparece la palabra "Python".
● Muestra el texto en mayúsculas y en minúsculas.
💡 Pista: Usa .split() para contar palabras.'''

texto = input("Introduce un texto: ")

palabras = texto.split()
conteo_palabras = len(palabras)
conteo_python = texto.lower().count("python")

print("Número de palabras en el texto:", conteo_palabras)
print("Número de veces que aparece 'Python':", conteo_python)
print("Texto en mayúsculas:", texto.upper())
print("Texto en minúsculas:", texto.lower())

'''Ejercicio 10: Pirámide de Números
Pide al usuario un número n y genera una pirámide numérica de n niveles como esta:
Si n = 5:'''

n = int(input("Introduce un número: "))

for i in range(1, n + 1):
    print(" ".join(str(x) for x in range(1, i + 1)))
