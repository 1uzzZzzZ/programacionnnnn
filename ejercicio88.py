# 88.- Buscar fechas
import re

texto = "Naci el 01/01/2025 y hoy es 20/05/2025"
patron = r'\d{2}/\d{2}/\d{4}'

fechas = re.findall(patron, texto)
print("Fechas encontradas:", fechas)