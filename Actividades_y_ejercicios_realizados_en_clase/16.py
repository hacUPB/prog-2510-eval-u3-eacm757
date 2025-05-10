from random import randint

lista =[]
for i in range(100):
    lista.append(randint(50,90))
conjunto = set(lista)
no_repetidos = list(conjunto)
print(no_repetidos)
print(f"hay {len(no_repetidos)} elementos repetidos")



lista1 = []
lista2 = []

for i in range(100):
    lista1.append(randint(0, 38))
    lista2.append(randint(50, 150))
    
conjunto1 = set(lista1)
conjunto2 = set(lista2)
comunes = conjunto1.intersection(conjunto2)
lista_comunes = list(comunes)
print(lista_comunes)


