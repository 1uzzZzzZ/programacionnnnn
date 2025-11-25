# 83.- Promedio desde archivo
try:
    with open("numeros.txt", "r") as f:
        suma = 0
        cantidad = 0
        for linea in f:
            try:
                num = float(linea.strip())
                suma = suma + num
                cantidad = cantidad + 1
            except ValueError:
                print("Linea ignorada (no es numero):", linea.strip())
        
        if cantidad > 0:
            print("El promedio es:", suma / cantidad)
        else:
            print("No habia numeros validos.")
            
except FileNotFoundError:
    print("El archivo numeros.txt no existe.")
except ZeroDivisionError:
    print("Error division entre cero.")