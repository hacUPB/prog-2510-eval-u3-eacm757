
num = int(input("ingrese el dividendo:"))
den =  int(input("ingrese el divisor:"))
if den == 0:
    print ("la division no esta definida")
elif num == 0:
    print("la division es 0")
elif num > 0:
    division = num // den
    mod = num % den
    if mod == 0:
        print(f"la division es exacta, cociente es: {division}")
    else:
        print(f"la division no es exacta, el cociente es {division} y sobran:{mod}")
