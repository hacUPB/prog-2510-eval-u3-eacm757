
envio = 9000
compra = int(input("ingrese el valor de la compra:"))
if compra >= 100000:
             print("el envio es gratis, el valor de su compra es:",compra)
else:
    print("el valor de",compra , "no supera el monto minimo, el valor de su compra es:",compra + 9000)



             
num = int(input("ingrese un numero:"))
if num % 2 == 0:
          print("el numero", num, "es par")
          print(f"el numero {num} es par")
else:
    print("el numero", num, "es impar")
    print(f"el numero {num} es impar")

    

edad = int(input("Ingrese su edad:"))
if 0 <= edad <= 5:
           print(f"La edad de {edad} esta en Primera infancia")
           print("la edad de", edad, "esta en la Primera infancia")
    
if 6 <= edad <= 11:
            print(f"La edad de {edad} esta en Infancia")
            print("la edad de", edad, "esta en Infancia")
            
elif 12 <= edad <= 18:
            print(f"La edad de {edad} esta en Adolescencia")
            print("la edad de", edad, "esta en Adolescencia")
            
elif 14 <= edad <= 26:
            print(f"La edad de {edad} esta en Juventud")
            print("la edad de", edad, "esta en Juentud")
            
elif 27 <= edad <= 59:
            print(f"La edad de {edad} esta en la Adultez")
            print("la edad de", edad, "esta en la Adultez")
            
elif edad >= 60:
            print(f"La edad de {edad} esta en Envejecimiento y vejez")
            print("la edad de", edad, "esta en Envejecimiento y vejez")

else:
    edad < 0
    print("la edad ingresada no es valida")




AM = "America del norte"
peso = int(input("ingrese el peso en gramos:"))
if peso > 5000:
    print("Por seguridad no podemos llevar su paquete")
if peso <= 5000:
    lugar = (input("A donde desea enviar su paquete:"))
    precio = peso * 11
    print(f"EL precio total a pagar es {precio}")
    print("El precio total es:", peso * 11)



print("=== MENÚ PRINCIPAL ===")
print("1. Ver datos de sensores")
print("2. Configurar parámetros")
print("3. Salir")

opcion = int(input("Selecciona una opción: "))

match opcion:
    case 1:
        print("Mostrando datos de sensores...")
    case 2:
        print("Entrando a configuración...")
    case 3:
        print("Saliendo del programa...")
    case _:
        print("Opción inválida.")
