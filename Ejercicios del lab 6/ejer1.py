#Ejercicio parte 01:
#Ejercicio Complejo:
#Generador de Contraseñas Seguras
#Descripción: Vamos a crear un generador de contraseñas seguras utilizando los conceptos
#que hemos aprendido hasta ahora, incluyendo funciones, módulos y control de flujo. La idea
#es que el programa genere una contraseña aleatoria con una longitud específica y asegure
#que cumple con ciertos requisitos de seguridad.
#Requisitos de seguridad de la contraseña:
#La contraseña debe tener al menos 8 caracteres.
#Debe incluir al menos una letra mayúscula y una letra minúscula.
#Debe contener al menos un número.
#Debe contener al menos un carácter especial (por ejemplo, !, @, #, $, %, etc.).

import random  
import string  # letras, números y caracteres especiales

def generar_contraseña_segura(longitud=8):
    
    if longitud < 8:
        print("La longitud mínima es de 8 caracteres")
        return None  # No sigue si no se cumple la longitud mínima
    
    letras_mayusculas = string.ascii_uppercase  
    letras_minusculas = string.ascii_lowercase  
    numeros = string.digits  # 0-9
    caracteres_especiales = string.punctuation  # !@#$%^&*()_+

    contraseña = [
        random.choice(letras_mayusculas), 
        random.choice(letras_minusculas),  
        random.choice(numeros),            
        random.choice(caracteres_especiales)  
    ]

    todos_los_caracteres = letras_mayusculas + letras_minusculas + numeros + caracteres_especiales
    for _ in range(longitud - 4):  
        contraseña.append(random.choice(todos_los_caracteres))  

    random.shuffle(contraseña)

    return ''.join(contraseña)

def menu_principal():
    print("Generador de Contraseñas Seguras")  
    longitud = int(input("Ingrese la longitud deseada para la contraseña (mínimo 8 caracteres): "))

    contraseña = generar_contraseña_segura(longitud)
    
    if contraseña:
        print(f"Su contraseña segura es: {contraseña}")  

menu_principal()
