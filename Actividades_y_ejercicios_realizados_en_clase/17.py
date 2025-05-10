frase = "hola mundo hola python HOLA mundo hola python"
palabras = frase.lower().split()
frecuencia = {}

for palabra in palabras:
    if palabra in frecuencia:
        frecuencia[palabra] += 1
    else:
        frecuencia[palabra] = 1

print(frecuencia)  # {'hola': 2, 'mundo': 1, 'python': 1}
