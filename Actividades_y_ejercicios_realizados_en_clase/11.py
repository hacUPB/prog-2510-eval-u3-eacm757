print("--" * 21)
print("Grados celsius\t|\t Grados Fahrenheit")
print("--" * 21)

for celsius in range (0,110,10):
        fahrenheit = (celsius * 9/5) +32
        print(f"{celsius}\t\t|\t\t{fahrenheit}")
    
