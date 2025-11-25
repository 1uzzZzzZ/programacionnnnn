# 90.- Censurar palabras
import re

texto = input("Ingresa un comentario: ")
prohibidas = ["tonto", "feo"]

# Reemplazar ignorando mayus/minus (flag IGNORECASE)
for mala in prohibidas:
    patron = re.compile(mala, re.IGNORECASE)
    texto = patron.sub("****", texto)

print("Texto censurado:", texto)