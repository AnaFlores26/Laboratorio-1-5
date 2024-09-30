# 1) Conversor de Temperatura: Escribe un programa que
# convierta entre Celsius y Fahrenheit. El programa debe
# permitir al usuario ingresar una temperatura y la unidad
# en la que está (C o F). Luego, realiza la conversión y
# muestra el resultado. Utiliza funciones y control de flujo
# para realizar las conversiones y manejar excepciones en
# caso de entradas incorrectas.

def convertir_temperatura(temperatura, unidad):
    if unidad == "c":
        tgf= (temperatura*9/5) + 32
        return f"La temperatura cambiada: {tgf} grados F°"
    elif unidad == "f":
        tgc = (temperatura - 32) * 5/9
        return f"La temperatura cambiada: {tgc} grados C°"
    else:
        raise ValueError("Unidad de temperatura incorrecta")

def menu_principal():
    try:
        temperatura = float(input("Ingrese la temperatura: "))
        unidad = input("Ingrese la unidad de temperatura (C/F): ").lower()
        resultado = convertir_temperatura(temperatura, unidad)
        print(resultado)
    except ValueError:
        print("ocurrio un error de valor")

programa= menu_principal()
print(programa)


