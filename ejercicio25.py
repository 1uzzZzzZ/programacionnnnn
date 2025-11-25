# 25.- Ecuacion de la recta
print("Punto 1:")
x1 = float(input("x1: "))
y1 = float(input("y1: "))

print("Punto 2:")
x2 = float(input("x2: "))
y2 = float(input("y2: "))

# Pendiente m = (y2 - y1) / (x2 - x1)
m = (y2 - y1) / (x2 - x1)

# Interseccion b = y - mx (usando punto 1)
b = y1 - (m * x1)

print("Pendiente (m):", m)
print(f"Ecuacion de la recta: y = {m}x + {b}")