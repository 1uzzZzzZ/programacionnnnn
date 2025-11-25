# 65.- Factoriales
import math

def mostrar_factorial(n):
    fact = math.factorial(n)
    print("Factorial de", n, "es", fact)

contador = 0
continuar = "si"

while continuar == "si":
    num = int(input("Ingresa numero para factorial: "))
    mostrar_factorial(num)
    contador = contador + 1
    continuar = input("Otro? (si/no): ")

print("Total de numeros leidos:", contador)