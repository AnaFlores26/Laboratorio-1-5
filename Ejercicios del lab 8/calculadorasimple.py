#2) Calculadora Simple: Crea una calculadora simple que pueda realizar 
# operaciones básicas como suma, resta, multiplicación y división.
#  La calculadora debe aceptar dos números del usuario y el tipo de 
# operación que desea realizar. Maneja excepciones en caso de errores de entrada.
 
def calcular(n1, n2, operacion):
    if operacion == "+":
        return n1 + n2
    elif operacion == "-":
        return n1 - n2
    elif operacion == "*":
        return n1 * n2
    elif operacion == "/":
        if n2 == 0:  
             return "Error: No se puede dividir entre cero."
        return n1 / n2
    else:
        raise ValueError("Operación no válida. Use +, -, *, /.")

def menu_calculadora():
    try:
        num1=float(input("Ingrese el primer número: "))
        num2=float(input("Ingrese el segundo número: "))
        operacion=input("Ingrese la operación (+, -, *, /): ").strip()

        resultado = calcular(num1, num2, operacion)
        print(f"El resultado de {num1} {operacion} {num2} es: {resultado:.2f}")
    
    except ValueError:
        print("Error: Por favor, ingrese números válidos.")
    except Exception as e:
        print(f"Ocurrió un error inesperado: {e}") 

menu_calculadora()        