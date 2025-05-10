while True:
    altitud_inicial = float(input("Ingrese la altitud inicial del satelite |Km|:"))
    if altitud_inicial >= 0:
        break
    else:
        print("Ha ingresado un valor negativo, vuelva a intentar:")

while True:
    coef_arrastre = float(input("Ingrese el coeficiente de arrastre:"))
    if coef_arrastre > 0:
        break
    else:
        print("Ha ingresado un valor incorrecto, vuelva a intentar")

while True:
    altitud_min = float(input("Ingrese altitud minima de seguridad"))
    if altitud_min >= 0:
        break
    else:
        print("Ha ingresado un valor negativo, vuelva a intentar:")
print("\nRealizando simulación de orbita\n")

cont = 0
while altitud_inicial > altitud_min:
    altitud_perdida = coef_arrastre * altitud_inicial
    altitud_inicial -= altitud_perdida
    coef_arrastre += 0.0001
    cont +=1
    print(f"Órbita{cont}: Altitud actual: {altitud_inicial:.2f}Km, Coeficiente de arrastre:{coef_arrastre:.4f}")
    
    if altitud_inicial <= altitud_min:
        print("El satélite ha reingresado en la atmósfera.")
        print("Órbitas completadas:", cont)
        break

    if altitud_perdida <= 0.01:
        print("El satélite se estabilizó en una órbita de:", altitud_inicial , "km")
        print("Órbitas completadas:", cont)
        break

        
