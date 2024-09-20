#Ejercicio 1: Usando la función incorporada len() ,
# encuentre la longitud de su nombre

nombre = "Ana"                  
longitud_nombre = len(nombre)
print("Mi nombre es:", nombre)
print ("La longitud de mi nombre es:",longitud_nombre)

#Ejercicio 2: Compara la longitud de tu nombre y tu apellido

nombre = "Ana"
LN= len(nombre)
print("Mi nombre es:", nombre)
print ("La longitud de mi nombre es:",LN)
apellido = "Flores"
LA = len(apellido)
print ("La longitud de mi apellido es:",LA)
if LN == LA: 
    print("La longitud de mi nombre y apellido son iguales")
else: 
    if LN > LA:
        print("la longitud de mi nombre es mayor a la de mi apellido")
    else: 
        print("la longitud de mi apellido es mayor a la de mi nombre")

# Ejercicio 3: Declara 5 como num_one y 4 como num_two

num_one, num_two = 5, 4 

# Sume num_one y num_two
# y asigne el valor a una variable total
total= num_one+num_two 
print("la sumaes:",total)

# Resta num_two de num_one y
# asigna el valor a una variable diff
diff = num_one-num_two
print("la resta es:",diff)
 
# Multiplica num_two y num_one y
# asigna el valor a una variable producto
producto = num_one*num_two 
print("multiplicacion")
# Dividir num_one por num_two y 
# asignar el valor a una variable división
división = num_one/num_two 

# Utilice la división de módulo para encontrar 
# num_two dividido por num_one y asigne el valor a 
# un resto variable 
resto= num_one%num_two 

# Calcula num_one a la potencia de num_two
# y asigna el valor a una variable exp
exp= num_one**num_two 

# Encuentra la división del piso de num_one por num_two y 
# asigna el valor a una variable floor_division
floor_division= num_one//num_two 

# Ejercicio 4: El radio de un círculo es de 30 metros

import math 
radio= 30
# Calcula el área de un círculo y 
# asigna el valor a una variable llamada area_of_circle
area_of_circle = math.pi*(radio**2)

#Calcula la circunferencia de un círculo y 
# asigna el valor a una variable llamada circum_of_circle 
circum_of_circle = 2*math.pi*radio

#Tome el radio como entrada del usuario y calcule el área
radio_usuario = float(input("Ingrese el radio del círculo: "))
area_usuario = math.pi * (radio_usuario ** 2)
print("El área del círculo con radio", radio_usuario, "es:", area_usuario)

#Ejercicio 5: Utilice la función de entrada incorporada
#  para obtener el nombre, apellido, país y edad de un usuario
#y almacenar el valor en sus nombres de variable 
# correspondientes.

nombre = input("Ingrese su nombre: ")
apellido = input("Ingrese su apellido: ")
pais = input("Ingrese su país: ")
edad = int(input("Ingrese su edad: "))
print("Nombre:", nombre, "Apellido:", apellido,"País:", pais, "Edad:", edad)

