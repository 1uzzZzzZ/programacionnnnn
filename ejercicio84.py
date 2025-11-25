# 84.- Manejo de multiples excepciones
archivo_nombre = input("Nombre del archivo a leer: ")

try:
    with open(archivo_nombre, "r") as f:
        contenido = f.read()
        
    if len(contenido) < 5:
        print("Error: El archivo tiene menos de 5 caracteres.")
    else:
        primeros_cinco = contenido[:5]
        numero = int(primeros_cinco)
        print("Numero convertido:", numero)

except FileNotFoundError:
    print("Error: El archivo no existe.")
except ValueError:
    print("Error: Los primeros 5 caracteres no son un numero valido.")
except Exception as e:
    print("Ocurrio otro error:", e)