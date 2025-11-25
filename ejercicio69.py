# 69.- Validar email simple
def validar_email(email):
    # Validacion simple: debe tener @
    if "@" in email:
        return True
    else:
        return False

correo = input("Ingresa tu correo: ")
if validar_email(correo):
    print("Direccion valida")
else:
    print("Direccion no valida (falta @)")