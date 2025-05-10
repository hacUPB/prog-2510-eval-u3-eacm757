nota = float(input("Ingrese su nota"))

if 0<=nota<= 2.9:
    print("su nota es baja")
elif 3.0<=nota<=3.9:
    print("su nota es mededia")
elif 4.0<=nota<=5:
    print("su nota es alta")
else:
    print("la nota ingresada no es valida")
