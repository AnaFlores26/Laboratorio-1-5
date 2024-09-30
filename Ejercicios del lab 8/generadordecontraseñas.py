#3) Generador de Contraseñas: Crea una función que genere contraseñas aleatorias. La función debe 
#aceptar parámetros como longitud de la contraseña y si debe incluir 
# letras mayúsculas, minúsculas, números y caracteres especiales. 
# Utiliza funciones lambda para generar caracteres aleatorios y maneja 
#excepciones si se proporcionan parámetros inválidos. 

import random, string

def generar_contraseña(longitud, usar_mayusculas, usar_minusculas, usar_numeros, usar_especiales):
    try:
        if longitud < 1:
            return "Error: La longitud debe ser al menos 1."
        caracteres = "" # para caracteres permitidos 
        
        # Lambda para elegir un carácter aleatorio de una cadena dada
        elegir_caracter = lambda cadena: random.choice(cadena)
        
        if usar_mayusculas:
            caracteres += string.ascii_uppercase 

        if usar_minusculas:
            caracteres += string.ascii_lowercase  

        if usar_numeros:
            caracteres += string.digits       

        if usar_especiales:
            caracteres += string.punctuation      

        if not caracteres:
            return "Error: Debes seleccionar al menos un tipo de carácter."
        
        # generar contraseña
        contraseña = ''.join(elegir_caracter(caracteres) for _ in range(longitud))
        
        return f"Contraseña generada: {contraseña}"
    
    except Exception as e:
        return f"Ocurrió un error inesperado: {e}"

def menu_generador_contraseña():
    try:

        longitud = int(input("Ingrese la longitud de la contraseña: "))
        
        usar_mayusculas = input("¿Deseas que contenga mayusculas? (si/no): ").lower() == 'si'
        usar_minusculas = input("¿Deseas que contenga minúsculas? (si/no): ").lower() == 'si'
        usar_numeros = input("¿Deseas que contenga números? (si/no): ").lower() == 'si'
        usar_especiales = input("¿Deseas que contenga caracteres especiales? (si/no): ").lower() == 'si'
        
        resultado = generar_contraseña(longitud, usar_mayusculas, usar_minusculas, usar_numeros, usar_especiales)
        print(resultado)
    
    except ValueError:
        print("Ocurrió un error, ingrese un valor numérico válido para la longitud")
    except Exception:
        print("Ocurrió un error inesperado. Por favor, inténtalo de nuevo")

menu_generador_contraseña()