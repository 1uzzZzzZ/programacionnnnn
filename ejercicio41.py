# 41.- Confirmacion de contrasena (sin limite)
p1 = input("Ingresa tu contrasena: ")
p2 = input("Confirma tu contrasena: ")

while p1 != p2:
    print("Las contrasenas no coinciden.")
    p2 = input("Vuelve a confirmar la contrasena: ")

print("Contrasena guardada.")