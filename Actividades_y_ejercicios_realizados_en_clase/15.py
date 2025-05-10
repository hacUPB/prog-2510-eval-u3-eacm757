from random import randint
filas = 5
columnas = 12
lista = []                #Creamos una lista vacía [[6,8,67],[4,7,12]]
for i in range(filas):        #Número de filas que tendrá la matriz (4)
    lista.append([])      #Agregamos una fila vacía a la matriz
    for j in range(columnas):    #En este bucle vamos a recorrer cada una de las filas (3)
        n = randint(0, 30)
        lista[i].append(n)  #Agregamos un elemento a la Lista en la posición siguiente

for i in range(filas):  #indice de las filas
    for j in range(columnas):  #
        print(f"{lista[i][j]:3}", end="  ")
    print()


#genenar indice
for f in range(filas):
    total_anio = sum(lista[f])
    ventas_anio.append(total_anio)
print(ventas_anio)

mayor = max(ventas_anio)
print(mayor)
indice = ventas_anio.index(mayor)
print(f"El año de mayor ventas fue {2020 + indice}")
