print ("--" *20)
print("Fastfast Airlines!")
print ("--" *20)

while True:
    print("| 1. Sr. | 2. Sra. |")
    indicativo = int(input("Ingrese su titulo (1-2):"))
    if indicativo == 1:
        nombre = input("Ingrese su nombre:").capitalize()
        apellido = input("Ingrese su apellido:").capitalize()
        print()
        print(f"Bienvendo a Fastfast Airlines! Sr. {nombre} {apellido}")
        break
    elif indicativo == 2:
        nombre = input("Ingrese su nombre:").capitalize()
        apellido = input("Ingrese su apellido:").capitalize()
        print()
        print(f"Bienvendo a Fastfast Airlines! Sra. {nombre} {apellido}")
        break
    else:
       print("ha ingresado un numero invalido, porfavor vuelva a intentarlo")

print("Tenemos para usted las siguientes rutas")
print("| Medellin | Bogotá | Cartagena |")
print()
while True:
    origen = input("Ingrese la ciudad de origen:").lower()
    destino = input("Ingrese la ciudad de destino:").lower()
    if ((origen == "medellin" or origen == "medellín") and (destino == "bogotá" or destino == "bogota" )) or ((origen == "bogotá" or origen == "bogota" ) and (destino == "medellin" or destino == "medellín")):
        distancia = 240
        break
    elif ((origen == "medellin" or origen == "medellín") and (destino == "cartagena")) or ((origen == "cartagena") and (destino == "medellin" or destino == "medellín")):
        distancia = 461
        break
    elif ((origen == "bogotá" or origen == "bogota") and (destino == "cartagena")) or ((origen == "cartagena") and (destino == "bogotá" or destino == "bogota")):
        distancia = 657
        break
    else:
        print()
        print("Las ciudades ingresadas son invalidas")
print()
print("| Lunes | Martes | Miércoles | Jueves | Viernes | Sábado | Domingo |")
dia_semana = input("Escoja el dia de la semana del viaje:").lower()
if distancia < 400:
    if (dia_semana == "lunes" or dia_semana == "martes" or dia_semana == "miércoles" or dia_semana == "jueves"):
        precio = 79900
    elif (dia_semana == "viernes"or dia_semana == "sábado" or dia_semana == "domingo"):
        precio = 119900
elif distancia >= 400:
    if (dia_semana == "lunes" or dia_semana == "martes" or dia_semana == "miércoles" or dia_semana == "jueves"):
        precio = 156900
    elif (dia_semana == "viernes" or dia_semana == "sábado" or dia_semana == "domingo"):
        precio = 213000
print()
dia_mes = input("Ingrese el dia del mes del viaje(1-30):")
print()
import random 
while True:        
    print("| 1.Pasillo | 2.ventana | 3.Sin preferencia |")
    asiento = input("Tiene alguna preferancia de asiento?, Seleccione una opción:")
    if asiento == "1":
        fila = "C"
        break
    elif asiento == "2":
        fila = "A"
        break
    elif asiento == "3":
        fila = "B"
        break
    else:
        print("Opcion invalida, vuelva a intentar")
num_asiento = random.randint(1,29)
print()
print(f"Tu vuelo de {origen} a {destino} del {dia_semana} {dia_mes} de abril esta reservado")
print(f"El valor de tu boleto es: {precio} y tu asiento es {num_asiento}{fila}")

        
