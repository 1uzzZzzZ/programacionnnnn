# 77.- Leer un archivo linea por linea
try:
    with open("entrada.txt", "r") as archivo:
        contador = 1
        for linea in archivo:
            print(contador, linea.strip())
            contador = contador + 1
except FileNotFoundError:
    print("Error: El archivo entrada.txt no existe.")