frutas = ["Manzana", "Banana", "Cereza"]

# Agregar un elemento al final de la lista
frutas.append("Damasco")

# Insertar un elemento en una posición específica
frutas.insert(-1, "Naranja")

# Extender la lista con otra lista
frutas.extend(["Pera", "Kiwi"])

print(frutas)



numeros = [1, 2, 3, 4, 5]

# Eliminar un elemento por valor
numeros.remove(3)

# Eliminar un elemento por índice y obtener su valor
valor_eliminado = numeros.pop(1)

# Eliminar todos los elementos de la lista
numeros.clear()

print(numeros)
print("Valor Eliminado:", valor_eliminado)


nombres = ["Ana", "Carlos", "Eva", "David"]

# Ordenar la lista alfabéticamente (ascendente)
nombres.sort()

# Ordenar la lista alfabéticamente en orden descendente
nombres.sort(reverse=True)

# Revertir el orden de la lista
nombres.reverse()

print(nombres)


colores = ["Rojo", "Azul", "Verde", "Rojo", "Amarillo"]

# Contar la cantidad de veces que aparece un elemento
cantidad_rojo = colores.count("Rojo")

# Encontrar el índice de un elemento
indice_azul = colores.index("Azul")

print("Cantidad de Rojo:", cantidad_rojo)
print("Índice de Azul:", indice_azul)


frase = input("Escriba una frase:")
palabras = frase.split()
num_palabras = len(palabras)
print(f"El numero de palabras es: {num_palabras}")
blancos = frase.count(" ")
print(f"la cantidad de espacios en blanco son: {blancos}")
num_letras = len(frase)
print(f"El numero de caracteres es:{num_letras}")
num_a

