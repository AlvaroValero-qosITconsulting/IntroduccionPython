#Variables y tipos de datos


#Mostrar por consola
print("=============================")
print("======MostrarPorConsola======")
print("=============================")

print("Hola mundo")
print(3+2)

print("=============================")
print("=========Comentarios=========")
print("=============================")

#Esto es un comentario en fila
'''Esto es un 
comentario en bloque'''
print("# y ''''''")

print("=============================")
print("=========TipoDeDatos=========")
print("=============================")

'''Mostrar una variable
En Python las variables no necesitan especificar su tipo'''

n = 4
print("n es entero: ", n)

#Media de dos variables
nota_2 = 10
nota_1 = 5
nota_media = (nota_1 + nota_2)/2
print("Media de dos variables (10 y 5): ", nota_media)

print("Multiplicación: ", nota_2*nota_1)

print("Mod: ", 10%2)

#Cadenas en Python

print("=============================")
print("===========Cadenas===========")
print("=============================")

cadena = "Hola"

print("Esto es una cadena: ", cadena)
print(cadena*2)

cadena1 = "Hola"
cadena2 = "mundo"
print("Suma dos cadena: ", cadena1 + " " + cadena2)

cadena3 = " "*10

print("Estos son diez espacios:" + cadena3 + "Aquí acaban los diez espacios")

palabra = "Python"

print(palabra[1])
print(palabra[0:2])

#palabra[0] = "N" da error porque palabra[0] = P. Esta propiedad es inmutable

print("============================")
print("=====TabulacionesYSalto=====")
print("============================")

"Hola mundo"
'Hola mundo'

#\t tabula y \n salta de linea

print ("Justo aquí \t empieza una tabulación")
print("una linea \n otra linea")

print("============================")
print("=======Listas(arrays)=======")
print("============================")

numero = [1,2,3,4,5]

print(numero)

#En las listas pueden mezclarse diferentes tipos de datos
datos = [4, "una cadena", 3.14, -15, "otra cadena", "1", 1]

print(datos)
len(datos)

print(datos[1])

print(datos[-1])

print(len(datos)-1)

print(datos[0:2])

print(datos[-7:-1])

print(numero)

numero + [6,7,8,9]

print(numero + [6,7,8,9])

pares = [2,4,5,8,10]
print(pares)

pares[2] = 6

print(pares)

pares.append(12)

print(pares)

letras = ["a", "b", "c", "d", "e", "f"]
print(letras[0:3])

letras[0:3] = ["A", "B", "C"]

print(letras)

a = [1, 2, 3]
b = [4, 5, 6]
c = [7, 8, 9]

r = [a, b, c]

print(r)

print(r[1])

print(r[1][1])

print(r[-1])

print(r[-1][-1])

print("=============================")
print("==========Operadores=========")
print("=============================")

print(1+1 == 3)

print(1+1 == 2)

print(3 > 2)

a = 10
b = 5

print(a == b*2)

print("Hola" == "Hola")

l1 = [0,1,2]
l2 = [2,3,4]

print(l1 == l2)

#len() es la funcion que devuelve la longuitud de una cadena
print(len(l1) == len(l2))

print(True * 3)
print(False * 3)

print(not True)
print (True and True)
print(True and False)
print(False and False)
print(False or True)

len(c) >= 20 and c[0] == "H"

#Comparación L con H y h
c = "Lectura"
print(c[0] == "H" or c[0] == "h")

#Acumulador
a = 5
a = a + 2
print(a)

a += 2
print(a)

print("=============================")
print("=========Condicionales=======")
print("=============================")

if True:
    print("Hola")
    print("otra linea")
    
a = 5
if a == 2:
    print("a vale 2")
if a == 5:
    print("a vale 5")


if a == 2:
    print("a vale 2")
    if a == 5:
        print("a vale 5")
        
a = 11
if a % 2 == 0:
    print("El numero es par")
else: 
    print("El numero es impar")
    
comando = "OTRA COSA"
if comando == "ENTRAR":
    print("Bienvenido al sistema")
elif comando == "SALUDAR":
    print("Hola")
    
nota = float(int(input("Introduce una nota:")))
print(nota)

print("=================")

nota1 = int(input("Calificación: "))

if nota1 >= 9:
    print("Tiene un sobresaliente")
elif nota1 >= 7:
    print("Tiene un notable")
elif nota1 >= 6:
    print("Tiene un bien")
elif nota1 >= 5:
    print("Tiene un suficiente")
else:
    print("Tiene un suspenso")

print("=============================")
print("============Bucles===========")
print("=============================")

c = 0
while c <= 6:
    c += 1
    print("c vale: ", c)

for i in range(1,11):
    print(f"Tabla del {i}: ")
    for j in range(1,11):
        print(f"{i} x {j} = {i * j}")
        

a = int(input("Tabla de multiplicacion del: "))
print(f"Tabla del {a}: ")

for i in range(1,11):
    print(f"{a} x {i} = {a * i}")
    
    
print("=============================")
print("===========Funciones=========")
print("=============================")

def saludo():
    print("Hola como estas")
    
saludo()

def sumar(a, b):
    return a + b

resultado = sumar(3, 4)
print("La suma es ", resultado)

print("Funcion para saber es si es par")

def Espar(a):
    b = False
    if a % 2 == 0:
        b = True
        return b
    else:
        return b

print(Espar(3), Espar(2))
