# 87.- Extraer numeros de texto
import re

texto = "El precio es 123.50 y el descuento es .20 o 0.5"
# Busca enteros o decimales
patron = r'\d*\.?\d+'

numeros_texto = re.findall(patron, texto)
# Convertir a float
lista_numeros = []
for n in numeros_texto:
    # Evitamos convertir un punto solo si ocurriera
    if n != '.': 
        lista_numeros.append(float(n))

print("Numeros encontrados:", lista_numeros)