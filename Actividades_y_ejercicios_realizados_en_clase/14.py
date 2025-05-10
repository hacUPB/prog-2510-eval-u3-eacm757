def convertir_puntuacion(puntuacion:int):
    if puntuacion > 100 or puntuacion < 0:
        return "Puntuacion Invalida"
    elif 90 <= puntuacion <= 100:
        return "A"
    elif 80 <= puntuacion <= 89:
        return "B"
    elif 70 <= puntuacion <= 79:
        return "C"
    elif 60 <= puntuacion <= 69:
        return "D"
    else:
        60 < puntuacion
        return "F"

def determinar_dia(dia:int):
    if dia < 0 or dia > 7:
        d_semana = "El numero no corresponde a ningun dia de la semana"
    elif dia == 1:
        d_semana = "Lunes"
    elif dia == 2:
        d_semana = "Martes"
    elif dia == 3:
        d_semana = "Miercoles"
    elif dia == 4:
        d_semana = "Jueves"
    elif dia == 5:
        d_semana = "Viernes"
    elif dia == 6:
        d_semana = "Sabado"
    else:
        dia == 7
        d_semana = "Domingo"
    return d_semana
    
        
def main():
    nota = convertir_puntuacion(59)
    print(nota)

    dia = determinar_dia(4)
    print(f"el dia de la semana es {dia}")

if __name__ == "__main__":
    main()
