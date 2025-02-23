# Contar vocales en una palabra

palabra = input("Ingresa una palabra: ").lower()
vocales = "aeiou"
contador = 0

for letra in palabra:
    if letra in vocales:
        contador += 1

print(f"La palabra '{palabra}' tiene {contador} vocales.")

# Eliminar espacios de una frase

def eliminar_espacios(frase):
    return frase.replace(" ", "")

frase_usuario = input("Ingresa una frase: ")
frase_sin_espacios = eliminar_espacios(frase_usuario)

print("Frase sin espacios:", frase_sin_espacios)

# Invertir una cadena

texto = input("Ingresa una palabra o frase: ")
invertido = texto[::-1]
print(f"Texto invertido: {invertido}")

# Contar vocales

def contar_vocales(frase):
    vocales = "aeiouAEIOU"
    contador = 0

    for letra in frase:
        if letra in vocales:
            contador += 1  

    print(f"La frase tiene {contador} vocales.")

frase = input("Ingresa una frase: ")  
contar_vocales(frase)

# Contar consonantes

def contar_consonantes(frase):
    consonantes = "bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ"
    contador = 0

    for letra in frase:
        if letra in consonantes:
            contador += 1

    print("La frase tiene", contador, "consonantes.")

frase = input("Ingresa una frase: ")
contar_consonantes(frase)

# Sumar los dígitos de un número

num = input("Ingresa un número: ")
suma = 0

for digito in num:
    suma += int(digito)

print(f"La suma de los dígitos de {num} es: {suma}")

# Factorial de un número

def factorial(n):
    resultado = 1
    for i in range(1, n + 1):
        resultado *= i
    return resultado

num = int(input("Ingresa un número: "))
print(f"El factorial de {num} es: {factorial(num)}")

# Fibonacci

def fibonacci_iterativo(n):
    a, b = 0, 1
    for _ in range(n):
        print(a, end=" ")
        a, b = b, a + b

num = int(input("Ingresa cuántos términos de Fibonacci deseas: "))
fibonacci_iterativo(num)

# Multiplos de un número

def calcular_multiplos(numero, cantidad):
    print(f"Los primeros {cantidad} múltiplos de {numero} son:")
    for i in range(1, cantidad + 1):
        print(numero * i)

num = int(input("Ingresa un número: "))
cant = int(input("¿Cuántos múltiplos deseas calcular? "))

calcular_multiplos(num, cant)

# Conversor de temperatura

def celsius_a_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def celsius_a_kelvin(celsius):
    return celsius + 273.15

temp_celsius = float(input("Ingresa la temperatura en Celsius: "))

temp_fahrenheit = celsius_a_fahrenheit(temp_celsius)
temp_kelvin = celsius_a_kelvin(temp_celsius)

print(f"{temp_celsius}°C equivale a:")
print(f"- {temp_fahrenheit:.2f}°F (Fahrenheit)")
print(f"- {temp_kelvin:.2f}K (Kelvin)")