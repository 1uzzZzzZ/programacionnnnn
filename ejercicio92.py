# 92.- Dividir parrafo en oraciones
import re

parrafo = "Hola mundo. Esto es una prueba! Funciona? Si."
# Dividir por . ! o ?
oraciones = re.split(r'[.!?]', parrafo)

print("--- Oraciones ---")
for o in oraciones:
    if o.strip() != "":
        print(o.strip())