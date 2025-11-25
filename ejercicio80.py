# 80.- Copiar contenido
try:
    with open("origen.txt", "r") as f_origen:
        contenido = f_origen.read()
    
    with open("copia.txt", "w") as f_destino:
        f_destino.write(contenido)
        
    print("Copia realizada con exito.")
except FileNotFoundError:
    print("El archivo origen.txt no existe.")