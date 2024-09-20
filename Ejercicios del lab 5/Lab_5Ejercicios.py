#1) La siguiente es una lista de las edades de 10 estudiantes:
# edades = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24] (4ptos)
# a. Ordena la lista y encuentra la edad mínima y máxima
# b. Añade de nuevo la edad mínima y máxima a la lista
# c. Encuentra la edad mediana (un elemento del medio o dos
# elementos del medio divididos por dos)
# d. Encuentra la edad promedio (suma de todos los elementos
#   divididos por su número)
# e. Encuentra el rango de las edades (máximo menos mínimo)
# f. Compara el valor de (mínimo - promedio) y (máximo - promedio
# ), usa el método abs()

edades = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]

# a. Ordena la lista y encuentra la edad mínima y máxima
edades.sort()  #ordena la lista en forma ascendente
minima = edades[0]
maxima = edades[-1]
print("La edad minima es:", minima)
print("la edad maxima es:", maxima)

# b. Añade de nuevo la edad mínima y máxima a la lista
edades.append(minima)  
edades.append(maxima)
print("la lista con la edad minima y maxima añadida es:", edades)

# c. Encuentra la edad mediana (un elemento del medio o dos
# elementos del medio divididos por dos)
if len(edades) % 2 == 0:
    mediana = (edades[len(edades) // 2]+ edades[len(edades)//2-1] )/2
else:
    mediana = (edades)[len(edades) // 2]
print("la edad mediana es:",mediana)

# d. Encuentra la edad promedio (suma de todos los elementos
#   divididos por su número)

promedio = sum(edades)/ len(edades)
print("el promedio de las edades es:", promedio)

# e. Encuentra el rango de las edades (máximo menos mínimo)

rango = maxima - minima
print("el rango de las edades es:", rango)

# f. Compara el valor de (mínimo - promedio) y (máximo - promedio
# ), usa el método abs()

diferencia_promedio_minima = abs(minima - promedio)
diferencia_promedio_maxima = abs(maxima - promedio)

print("la diferencia de la edad minima y el promedio es: ",diferencia_promedio_minima )
print("la diferencia de la edad maxima y el promedio es: ",diferencia_promedio_maxima )


# 2) “Soy profesor y me encanta inspirar y enseñar a la gente”.
# ¿Cuántas palabras únicas se han utilizado en la frase?
# Usa los métodos de split y sets para obtener las palabras
# únicas. (4pto)

frase = "Soy profesor y me encanta inspirar y enseñar a la gente"
palabras =frase.split()
palabras_unicas = set(palabras)
print("el numero de palabras unicas es:", len(palabras_unicas))

#3) Considera tres listas de números enteros, una con números del 1 al 10,
#  otra con números del 5 al 15, y la última con números del 10 al 20. 
#a. Convierte las listas en conjuntos. 
#b. Encuentra el conjunto de todos los números que están presentes en 
# las tres listas. 
# c. Encuentra el conjunto de todos los números que están presentes 
# en al menos una de las listas. 
# d. Encuentra el conjunto de todos los números que están presentes
#  en la primera lista, pero no en la última. 
# e. Convierte los conjuntos obtenidos en tuplas y suma el primer y
#  último elemento de cada tupla.
lista1=list(range(1,11))  
lista2=list(range(5,16))  
lista3=list(range(10,21))  
#a
c1=set(lista1)
c2=set(lista2)
c3=set(lista3)
#b
interseccion=c1 and c2 and c3
print("los numeros presentes en las tres listas son:", interseccion)
#c
union=c1 | c2 | c3
print("los numeros presentes en al menos una de las listas son:", union)
#d
diferencia=c1-c3
print("los numeros presentes en la primera lista pero no en la última son:", diferencia)
#e
tupla_interseccion = tuple(interseccion)
tupla_union = tuple(union)
tupla_diferencia = tuple(diferencia)
if tupla_interseccion:
    suma_interseccion=tupla_interseccion[0]+tupla_interseccion[-1]
    print(f"suma del 1er y ultimo elemento de la interseccion: {suma_interseccion}")

if tupla_union:
    suma_union=tupla_union[0]+tupla_union[-1]
    print(f"suma del 1er y ultimo elemento de la union: {suma_union}")

if tupla_diferencia:
    suma_diferencia=tupla_diferencia[0]+tupla_diferencia[-1]
    print(f"suma del 1er y ultimo elemento de la diferencia: {suma_diferencia}")

#4) Considera dos listas, l1 y l2, que contienen tuplas.
#  Cada tupla consta de una cadena de texto y un número entero.
#  La lista l1 tiene 5 elementos y la lista l2 tiene 3 elementos.
l1 = [("one", 1), ("two", 2), ("three", 3), ("four", 4), ("five", 5)]  
l2 = [("one", 1), ("two", 2), ("six", 6)] 
#Tu tarea es: 
#a. Crear conjuntos a partir de estas listas, s1 y s2. 
s1=set(l1)
s2=set(l2)

#b. Encontrar los elementos que son comunes a s1 y s2 y almacenarlos 
# en un conjunto s3. 
s3=s1 and s2
print("elementos comunes a s1 y s2:", s3)

#c. Encontrar los elementos que son únicos para s1 y s2 y almacenarlos 
# en un conjunto s4.
s4=s1^s2
print("elementos unicos entre s1 y s2:", s4)

#d. Crear una nueva lista l3 que contenga los elementos de s3 y s4 
# ordenados por el número entero de cada tupla. 
l3=sorted(list(s3 | s4), key=lambda x: x[1])  
print("lista ordenada por el numero entero:", l3)