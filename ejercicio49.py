# 49.- Mostrar productos en diccionario (del ejercicio anterior)
# Reutilizo la carga de datos
n = int(input("Cuantos productos? "))
nombres = []
claves = []
stocks = []

for i in range(n):
    nombres.append(input("Nombre: "))
    claves.append(input("Clave: "))
    stocks.append(int(input("Stock: ")))

print("--- Diccionario de productos ---")
diccionario = {}

for i in range(n):
    # Usamos la clave del producto como llave del diccionario
    clave_actual = claves[i]
    diccionario[clave_actual] = {
        "nombre": nombres[i], 
        "stock": stocks[i]
    }

print(diccionario)