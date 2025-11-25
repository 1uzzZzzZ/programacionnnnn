# 86.- Validar correo simple con regex
import re

email = input("Ingresa correo: ")
# Patron basico: letras/num + @ + letras + . + letras
patron = r'^[\w\.-]+@[\w\.-]+\.\w+$'

if re.match(patron, email):
    print("Valido")
else:
    print("Invalido")