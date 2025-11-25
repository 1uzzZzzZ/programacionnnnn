# 29.- Division segura
dividendo = float(input("Dividendo: "))
divisor = float(input("Divisor: "))

if divisor == 0:
    print("Error: No se puede dividir entre cero.")
else:
    resultado = dividendo / divisor
    print("Resultado:", resultado)