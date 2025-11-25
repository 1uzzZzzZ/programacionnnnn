# 33.- Evaluacion de vendedor
nombre = input("Nombre del vendedor: ")
ventas = float(input("Volumen de ventas ($): "))

situacion = ""

if ventas < 1000:
    situacion = "Despedido"
elif ventas < 5000:
    situacion = "En periodo de prueba"
elif ventas < 10000:
    situacion = "Bono del 5%"
else:
    situacion = "Bono del 10%"

print("Vendedor:", nombre, "| Situacion:", situacion)