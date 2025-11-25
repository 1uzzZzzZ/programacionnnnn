# 85.- Regex palabras con mayuscula
import re

texto = input("Ingresa un texto: ")
# Buscamos palabras que empiecen con Mayuscula [A-Z] seguidas de letras
patron = r'\b[A-Z][a-z]*\b'

encontradas = re.findall(patron, texto)
print("Palabras con mayuscula:", encontradas)