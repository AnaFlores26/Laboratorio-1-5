#1) Orden Alfabético: 
#Escribe un programa que solicite al usuario dos palabras y determine 
# cuál va primero en orden alfabético. 
p1=input("Ingrese la primera palabra: ")
p2=input("Ingrese la segunda palabra: ")
if p1 < p2:
    print(f"{p1} va primero por alfabetico")
else:
    print(f"{p2} va primero por alfabetico")

#2) Clasificación de Triángulos: 
#Escribe un programa que pida al usuario las longitudes de tres lados de 
# un triángulo y determine si es equilátero, isósceles o escaleno. 
l1 = float(input("Ingrese la longitud del 1er lado: "))
l2 = float(input("Ingrese la longitud del 2do lado: "))
l3 = float(input("Ingrese la longitud del 3er lado: "))

if l1 == l2 == l3:
    print("El triangulo es equilátero")
elif l1 == l2 or l2 == l3 or l1 == l3:
    print("El triangulo es isosceles")
else:
    print("El triangulo es escaleno")

#3) Promedio de Notas: 
#Escribe un programa que calcule el promedio de una lista de notas 
# ingresadas por el usuario. 
notas = input("Ingrese las notas separadas por comas: ").split(',')
suma = 0
for nota in notas:
    suma += float(nota)
promedio = suma / len(notas)
print("El promedio de las notas es:", promedio)

# 4) Calculadora Simple: 
#Escribe un programa que realice operaciones aritméticas básicas 
# (suma, resta, multiplicación, división) con dos números ingresados 
# por el usuario. 
num1 = float(input("Ingrese el 1er numero: "))
num2 = float(input("Ingrese el 2do numero: "))
op=input("Ingrese la operación que desee realizar").lower()
if op== "suma":
    resultado = num1 + num2
elif op == "resta":
    resultado = num1 - num2
elif op == "multiplicación":
    resultado = num1 * num2
elif op == "divición":
    if num2 != 0:
        resultado = num1 / num2
    else:
        resultado = "Error"
else:
    resultado = "Operación no valda"

print("El resultado es:", resultado)

#5) ¿Par o Impar? 
#Pide al usuario un número entero y utiliza una estructura if...else 
# para determinar si es par o impar. Imprime el resultado. 
numero = int(input("Ingrese un numero entero: "))

if numero % 2 == 0:
    print("El numero es par")
else:
    print("El numero es impar")

# 6) Mayor de Tres
#Pide al usuario tres números y utiliza estructuras if...elif...else 
# anidadas para determinar cuál es el mayor. 
n1 = int(input("Ingrese el 1er número: "))
n2 = int(input("Ingrese el 2do número: "))
n3 = int(input("Ingrese el 3er número: "))

if n1>=n2 and n1>=n3:
    mayor=n1
elif n2>=n1 and n2>=n3:
    mayor=n2
else:
    mayor=n3

print("El mayor de los tres números es:", mayor)

#7) Calculadora de Descuento: 
#Pide al usuario el precio original de un producto y la categoría del 
# descuento ("estudiante", "jubilado", "empleado" u "otro"). Aplica un 
# descuento del 10% para estudiantes, 15% para jubilados, 5% para 
# empleados y 0% para otros. Imprime el precio final.
precio_original=float(input("Ingrese el precio original del producto: "))
categoria=input("Ingrese la categoría (estudiante, jubilado, empleado, otro): ").lower()

if categoria == "estudiante":
    descuento = 0.10
elif categoria == "jubilado":
    descuento = 0.15
elif categoria == "empleado":
    descuento = 0.05
else:
    descuento = 1

descontar=precio_original*descuento
precio_final=precio_original - descontar
print("El precio final es:", precio_final)

#8) Número Positivo, Negativo o Cero:
#Pide al usuario un número y utiliza una estructura if...elif...else 
# para determinar si es positivo, negativo o cero. 
numero =float(input("Ingrese un numero: "))
if numero > 0:
    print("El número es positivo")
elif numero < 0:
    print("El número es negativo")
else:
    print("El número es cero")

#9) Año Bisiesto:  
# Pide al usuario un año y utiliza 
# una estructura if...elif...else para determinar si es bisiesto.
#  Un año es bisiesto si es divisible por 4, pero no por 100, a menos 
# que también sea divisible por 400. 
año=int(input("Ingrese un año: "))

if (año % 4 == 0 and año % 100 != 0) or (año % 400 == 0):
    print(f"El año {año} es bisiesto.")
else:
    print(f"El año {año} no es bisiesto.")

#10) Conversor de Unidades de Longitud: 
#Pide al usuario una longitud en metros y la unidad a la que desea
#  convertir ("pies", "pulgadas" o "yardas"). 
# Realiza la conversión e imprime el resultado. 
metros = float(input("Ingrese la longitud en metros: "))
unidad = input("Ingrese la unidad a la que desea convertir (pies, pulgadas, yardas): ").lower()
if unidad == "pies":
    conversion = metros * 3.28084
elif unidad == "pulgadas":
    conversion = metros * 39.3701
else:
    unidad == "yardas"
    conversion = metros * 1.09361
print(f"La conversion a {unidad} es: {conversion}")

#11) Calculadora de IMC: 
#Pide al usuario su peso en kilogramos y su altura en metros. 
# Calcula su índice de masa corporal (IMC = peso / altura^2) y utiliza
#  una estructura if...elif...else para determinar su categoría 
# (bajo peso, normal, sobrepeso, obesidad). 
peso = float(input("Ingrese su peso en kilogramos: "))
altura = float(input("Ingrese su altura en metros: "))

imc = peso / (altura ** 2)

if imc < 18.5:
    categoria = "Bajo peso"
elif 18.5 <= imc < 25:
    categoria = "Normal"
elif 25 <= imc < 30:
    categoria = "Sobrepeso"
else:
    categoria = "Obesidad"

print(f"Su IMC es: {imc:.2f}, lo que indica {categoria}.")

#12) Día de la Semana: 
#Pide al usuario un número del 1 al 7 y utiliza una estructura
#  if...elif...else para imprimir el día de la semana correspondiente. 
numero = int(input("Ingrese un número del 1 al 7: "))

if numero == 1:
    dia="Lunes"
elif numero == 2:
    dia="Martes"
elif numero == 3:
    dia="Miércoles"
elif numero == 4:
    dia="Jueves"
elif numero == 5:
    dia="Viernes"
elif numero == 6:
    dia="Sábado"
elif numero == 7:
    dia="Domingo"
else:
    dia="Numero no valido"

print(dia)

#13) Validación de Edad: 
#Pide al usuario su edad y utiliza una estructura if...else para determinar si es mayor de edad (18 
#años o más).
edad=int(input("Ingrese su edad: "))

if edad >= 18:
    print("mayor de edad")
else:
    print("menor de edad")

#14) Piedra, Papel o Tijera: 
#Pide al usuario que elija "piedra", "papel" o "tijera". 
# Genera una elección aleatoria para la computadora y determina quién gana.
import random

opciones = ["piedra", "papel", "tijera"]
usuario = input("ingrese piedra, papel o tijera: ").lower()

if usuario not in opciones:
    print("opcion no valida")
else:
    computadora= random.choice(opciones)
    print("La computadora escogio: ", computadora)

    if usuario == computadora:
        print("Empate")
    elif (usuario == "piedra" and computadora == "tijera") or \
         (usuario == "papel" and computadora == "piedra") or \
         (usuario == "tijera" and computadora == "papel"):
        print("Ganaste")
    else:
        print("Perdiste")   

#15) Número de Teléfono con Formato: 
#Pide al usuario un número de teléfono de 10 dígitos y utiliza slicing y
#  concatenación para darle el formato "(###) ###-####".
numero_telefono = input("Ingrese un número de teléfono de 10 dígitos: ")

if len(numero_telefono) == 10 and numero_telefono.isdigit():
    p1 = numero_telefono[:3]  
    p2 = numero_telefono[3:6]  
    p3 = numero_telefono[6:]
    print("(" + p1 + ") " + p2 + "-" + p3)
else:
    print("El numero ingresado no es valido")