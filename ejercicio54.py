# 54.- Ahorradores
nombres = ["Ana", "Beto", "Carla", "Daniel"]
ahorros = [500, 1500000, 200, 50000]

for i in range(len(nombres)):
    dinero = ahorros[i]
    nombre = nombres[i]
    
    if dinero < 1000:
        print(nombre, "no tendrás para tu futuro")
    elif dinero > 1000000:
        print(nombre, "ya merito te retiras")
    else:
        print(nombre, "ahorro regular")