cont = 0
suma_salarios = 0
tarifa = float(input("Ingrese la tarifa de pago:"))
while cont < 5:
    horas = float(input("Ingrese las horas trabajadas:"))
    salario = tarifa * horas
    print(f"su salario es {salario}")
    suma_salarios += salario
    cont += 1
print(f"la sumatoria de todos los salarios es {suma_salarios}")
    
    
