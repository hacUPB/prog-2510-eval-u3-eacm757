base_datos = {
    "usuario1": "contrasena1",
    "usuario2": "contrasena2",
    "usuario3": "contrasena3",
    "usuario4": "contrasena4",
    "usuario5": "contrasena5"
}

def login(usuario:str, contrasena:str):
    if usuario in base_datos:
        if contrasena == base_datos[usuario]:
            print("Ingreso exitoso")
            return True
        else:
            print("Conrtraseña Invalida")
            return False
    else:
        print("Usuario no registrado")
        return False
    
        

def main():
    cont = 0
    while cont < 3:
        user = input("Ingrese su nombre de usuario:")
        password = input("Ingrese su contraseña:")
        resultado = login(user, password)
        if resultado == False:
            cont += 1
            if cont == 3:
                print("Bloqueado")
        else:
            print("Acceso concedido")
    
main()
