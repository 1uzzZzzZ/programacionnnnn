# 74.- Listar archivos csv con OS
import os

carpeta = input("Ingresa la ruta de la carpeta (o '.' para la actual): ")

if os.path.isdir(carpeta):
    archivos = os.listdir(carpeta)
    csvs = []
    
    for arch in archivos:
        if arch.endswith(".csv"):
            csvs.append(arch)
    
    csvs.sort()
    print("Archivos CSV encontrados:", csvs)
else:
    print("La carpeta no existe.")