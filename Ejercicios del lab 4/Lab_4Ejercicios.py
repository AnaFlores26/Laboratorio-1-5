# 1) Suma de Números Pares: 
# Pide al usuario un número entero positivo 'n'. Calcula la suma de todos
#  los números pares desde 2 hasta 'n' (inclusive) utilizando un 
# bucle while. 
n=int(input("ingrese un numero entero positivo: "))
suma=0
numero=2
while numero <= n:
    suma += numero  
    numero += 2  
print("la suma de todos los numeros pares desde 2 hasta", n, "es:", suma)

# 2) Conjetura de Collatz: 
# Pide al usuario un número entero positivo. Aplica la conjetura de 
# Collatz: si el número es par, divídelo por 2; si es impar, multiplícalo
#  por 3 y suma 1. Repite el proceso hasta que el número llegue a 1. 
# Utiliza un bucle while e imprime la secuencia de números generada. 
numero=int(input("ingrese un numero entero positivo: "))
while numero != 1:
    print(numero, end=" ")  
    if numero % 2 == 0:
        numero = numero//2  
    else:
        numero = numero*3+1  
print(1)

# 3) Tabla de Multiplicar con for: 
# Pide al usuario un número entero positivo. Imprime la tabla de 
# multiplicar de ese número utilizando un bucle for. 
numero=int(input("ingrese un numero entero positivo: "))
for i in range(1,11):  
    resultado=numero*i
    print(numero, "x", i, "=", resultado)

#4) Imprimir Patrón de Triángulo: Pide al usuario un número entero 
# positivo 'n'. Imprime un triángulo de asteriscos con 'n' filas 
# utilizando un bucle for anidado.
n = int(input("ingrese un numero entero positivo: "))
for i in range(1, n+1):  
    for j in range(i):  
        print("*", end="")
    print()

# 5) Contar Vocales en una Frase: 
#Pide al usuario una frase y cuenta el número total de vocales 
# (mayúsculas y minúsculas) utilizando un bucle for. 
frase=input("ingrese una frase: ")
contador_vocales=0
for letra in frase:
    if letra.lower() in "aeiou":  
        contador_vocales += 1  
print("el numero total de vocales en la frase es:", contador_vocales)

# 6) Suma de Dígitos: 
# Pide al usuario un número entero positivo. Calcula la suma de sus 
# dígitos utilizando un bucle while. 
numero = int(input("ingrese un numero entero positivo: "))
suma_digitos=0
while numero > 0:
    digito = numero % 10  
    suma_digitos += digito  
    numero = numero // 10  
print("la suma de los digitos es:", suma_digitos)

#7) Invertir una Cadena: 
#Pide al usuario una cadena e inviértela utilizando un bucle for. 
cadena=input("ingrese una cadena: ")
cadena_invertida=""
for letra in cadena:
    cadena_invertida = letra + cadena_invertida  
print("la cadena invertida es:", cadena_invertida)

#8) Número de Fibonacci: Pide al usuario un número entero positivo 'n'. 
# Calcula el enésimo número de Fibonacci utilizando un bucle for. 
n=int(input("ingrese un numero entero positivo: "))
a,b=0,1
for i in range(n):
    a,b=b, a+b  
print(f"el numero {n} de la secuencia de fibonacci es:", a)

#9) Verificar si una Cadena es Palíndromo: Pide al usuario una cadena y 
# verifica si es un palíndromo (se lee igual de izquierda a derecha 
#que de derecha a izquierda) utilizando un bucle for. 
cadena=input("ingrese una cadena: ")
cadena=cadena.replace(" ", "").lower()
es_palindromo = True
for i in range(len(cadena) // 2):
    if cadena[i] != cadena[-(i + 1)]:
        es_palindromo = False
        break
if es_palindromo:
    print("la cadena es un palindromo")
else:
    print("la cadena no es un palindromo")

# 10) Calculadora de Promedio: 
#Pide al usuario una serie de números separados por comas. Calcula el 
# promedio de esos números utilizando un bucle for.
numeros=list(map(float, input("ingrese una serie de numeros separados por comas: ").split(',')))
suma=0
for numero in numeros:
    suma += numero
promedio = suma / len(numeros)
print("el promedio de los numeros es:", promedio)