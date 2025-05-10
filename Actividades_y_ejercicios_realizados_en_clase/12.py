def mcd(num,den):
    if num <= den:
        menos = num
    else:
        menor = den
    for divisor in range(menor,0,-1):
        if num % divisor == 0 and den % divisor == 0:
            max_com_div = divisor
            break
    return max_com_div


def imprime_fraccion(num, den, maximo):
    print(f"{num}/{den} = {num/maximo}/{den/maximo}")
    


def main():
    numerador = int(input("ingrese el numerador:"))
    denominador = int(input("ingrese el denominador:"))
    maximo = mcd(numerador, denominador)
    print(f"M.C.D es {maximo}")

if __name__ == "__main__":
    main()
    
