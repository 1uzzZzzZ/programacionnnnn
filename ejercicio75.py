# 75.- Leer argumentos sys
# Para probar este, ejecutar en terminal: python ejercicio75.py archivo.txt 5
import sys

# sys.argv[0] es el nombre del script
# sys.argv[1] deberia ser nombre del archivo
# sys.argv[2] deberia ser n

if len(sys.argv) == 3:
    nombre_archivo = sys.argv[1]
    
    try:
        n = int(sys.argv[2])
        # Intentamos abrir (crea un archivo dummy para probar si no tienes uno)
        with open(nombre_archivo, 'r') as f:
            print(f"--- Primeras {n} lineas ---")
            for i in range(n):
                linea = f.readline()
                if not linea: break
                print(linea.strip())
                
    except ValueError:
        print("Error: El segundo argumento debe ser un numero entero.")
    except FileNotFoundError:
        print("Error: El archivo no existe.")
else:
    print("Error: Se requieren 2 argumentos (archivo y numero).")