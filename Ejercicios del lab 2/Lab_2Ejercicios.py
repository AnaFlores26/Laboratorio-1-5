#1) Encuentra la longitud del texto python, 
# convierte el valor a float y luego conviértelo a string
t="python"
a=len(t)
b=float(a)
c=str(b)
print(t,a,b,c)

# 2) Los números pares son divisibles por 2 y el residuo es cero.
#  ¿Cómo comprobarías si un número es par o no usando python? 

a=int(input("Ingrese un número:"))
if a%2==0:
    print("El número es par")
else: 
    print("NO es un número par")

 #3) Comprueba si la división entera de 7 entre 3 es igual al valor
 #  de 2.7 convertido a entero.

a=7
b=3
if a//b == int(2.7): 
    print("son iguales") 
else: 
    print("no son iguales")

 # 4) Comprueba si el tipo de '10' es igual al tipo de 10 

if type('10') == type(10):
    print("Los tipos son iguales")
else:
    print("Los tipos no son iguales")
    
 # 5) Comprueba si int('9.8') es igual a 10 
 
a=int(float('9.8'))

if a == 10:
    print(True)
else:
    print(False)

 # 6) Escribe un script que solicite al usuario que introduzca 
 # las horas y la tarifa por hora. ¿Cuál es el pago de la persona? 
 # Introduce las horas: 40 
 # Introduce la tarifa por hora: 28 
 # Tu salario semanal es 1120
horas=int(input("Introduzca las horas: "))
tarifa= float(input("Introduzca la tarifa por hora: "))
ss= int(horas*tarifa)
print("Tu salario semanal es: ", ss)
 
 #7) Escribe un script que solicite al usuario que introduzca 
 # el número de años. Calcula el número de segundos que una persona
 #  puede vivir. Supongamos que una persona puede vivir cien años. 
 # Introduce el número de años que has vivido: 100 
 # Has vivido durante 3153600000 segundos.
años = int(input("Introduce el número de años que has vivido: "))
segundos_por_año = 365 * 24 * 60 * 60
segundos_vividos = años * segundos_por_año
print(f"Has vivido durante {segundos_vividos} segundos.")

 #8) Escribe un script en Python que muestre la siguiente tabla 
 # 1 1 1 1 1 
 # 2 1 2 4 8 
 # 3 1 3 9 27 
 # 4 1 4 16 64 
 # 5 1 5 25 125
for numero in range(1, 6):
    print(numero, 1, numero, numero**2, numero**3)

#9) Invertir una cadena: Escribe un programa que pida al usuario 
# una cadena y luego la imprima al revés. 
cadena = input("Ingrese una cadena: ")
cadenaalreves = ""
for letra in cadena:
    cadenaalreves = letra + cadenaalreves  
print("La cadena al reves es:", cadenaalreves)

# 10) Contar vocales: Escribe un programa que cuente el número 
# de vocales en una cadena dada por el usuario. 
cadena=input("Ingrese una cadena: ")
vocales="aeiouAEIOU"
contadorvocales=0
for letra in cadena:
    if letra in vocales:
        contadorvocales +=1 
print(f"El numero de vocales de la cadena es: {contadorvocales}")

#11) Palíndromo: Escribe un programa que verifique si una cadena 
# dada por el usuario es un palíndromo (se lee igual de izquierda a
#  derecha que de derecha a izquierda). 
cadena=input("Ingrese una cadena: ")
if cadena == cadena[::-1]:
    print("Es un palindromo")
else:
    print("No es un palindromo")

# 12) Reemplazar espacios: Escribe un programa que reemplace todos
#  los espacios en una cadena dada por el usuario con guiones bajos. 
cadena=input("Ingrese una cadena: ")
print(cadena.replace(" ","_"))

#13) Contar palabras: Escribe un programa que cuente el número de 
# palabras en una cadena dada por el usuario. 
a=input("Ingrese una cadena: ")
palabras=a.split()
print("El numero de palabras en la cadena es: ",len(palabras))

#14) Mayúsculas y minúsculas: Escribe un programa que convierta una 
# cadena dada por el usuario a mayúsculas y luego a minúsculas, 
# imprimiendo cada resultado. 
b=input("Ingrese una cadena: ")
print(a.upper())
print(a.lower())

#15) Eliminar espacios en blanco: Escribe un programa que elimine 
# los espacios en blanco al principio y al final de una cadena dada 
# por el usuario. 
c=input("Ingrese una cadena: ")
print(c.strip())

#16) Extraer subcadena: Escribe un programa que extraiga una subcadena
#  de una cadena dada por el usuario, especificando los índices de
#  inicio y fin.
cadena=input("Ingrese una cadena: ")
inicio = int(input("Ingrese el indice de inicio: "))
fin = int(input("Ingrese el indice de fin: "))
subcadena= cadena[inicio:fin]
print("La subcadena es:", subcadena)

#17) Verificar prefijo y sufijo: Escribe un programa que verifique 
# si una cadena dada por el usuario comienza con un prefijo 
# específico y termina con un sufijo específico.
cadena = input("Ingrese una cadena: ")
prefijo = input("Ingrese el prefijo: ")
sufijo = input("Ingrese el sufijo: ")
if cadena.startswith(prefijo) and cadena.endswith(sufijo):
    print("La cadena comienza con el prefijo y termina con el sufijo")
elif cadena.startswith(prefijo):
    print("La cadena comienza con el prefijo, pero no termina con el sufijo")
elif cadena.endswith(sufijo):
    print("La cadena termina con el sufijo, pero no comienza con el prefijo")
else:
    print("La cadena no comienza con el prefijo ni termina con el sufijo")