envio = 0
compra = int(input("Ingrese el valor de la compra>> "))
if compra < 100000:
	envio = 9000
total = compra + envio
print(f"El total de la compra es: {total}")
