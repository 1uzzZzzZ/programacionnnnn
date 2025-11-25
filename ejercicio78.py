# 78.- Contar lineas, palabras y caracteres
nombre = "datos.txt"
try:
    with open(nombre, "r") as f:
        contenido = f.read()
        
        # Contamos
        lineas = contenido.count("\n") + 1
        # Si el archivo esta vacio, ajustamos
        if len(contenido) == 0: 
            lineas = 0
            
        palabras = len(contenido.split())
        caracteres = len(contenido)
        
        print("Lineas:", lineas)
        print("Palabras:", palabras)
        print("Caracteres:", caracteres)
        
except FileNotFoundError:
    print("No se encontro el archivo datos.txt")