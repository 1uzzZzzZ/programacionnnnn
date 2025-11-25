# 91.- Extraer usuarios de correos
import re

texto = "Contacta a admin@sitio.com o a ventas@empresa.org"
# Todo lo que no sea @ antes de una @
patron = r'([\w\.-]+)@'

usuarios = re.findall(patron, texto)
print("Usuarios:", usuarios)