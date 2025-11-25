# 50.- Busqueda por nombre o clave
# Datos predefinidos para probar rapido
nombres = ["Coca", "Pepsi", "Fanta"]
claves = ["001", "002", "003"]
stocks = [10, 5, 8]

busqueda = input("Ingresa nombre o clave a buscar: ")

encontrado = False

for i in range(len(nombres)):
    # Buscamos si coincide con nombre O con clave
    if nombres[i] == busqueda or claves[i] == busqueda:
        print("Encontrado en indice:", i)
        print("Producto:", nombres[i])
        print("Clave:", claves[i])
        print("Stock:", stocks[i])
        encontrado = True
        break # Termina el ciclo si lo encuentra

if encontrado == False:
    print("Producto no encontrado.")