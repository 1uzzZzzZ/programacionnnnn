# 38.- Validacion de numero entre 1 y 5
numero = int(input("Ingresa un numero entre 1 y 5: "))

while numero < 1 or numero > 5:
    print("Numero fuera de rango.")
    numero = int(input("Intentalo de nuevo (1-5): "))

print("Dato correcto:", numero)