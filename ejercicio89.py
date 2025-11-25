# 89.- Validar contrasena segura
import re

pwd = input("Ingresa contrasena: ")

segura = True
if len(pwd) < 8:
    segura = False
if not re.search(r'[A-Z]', pwd): # Mayuscula
    segura = False
if not re.search(r'[a-z]', pwd): # Minuscula
    segura = False
if not re.search(r'[0-9]', pwd): # Numero
    segura = False

if segura:
    print("Contrasena segura")
else:
    print("Insegura")