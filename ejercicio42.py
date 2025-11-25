# 42.- Confirmacion de contrasena (con limite de 3 intentos)
p1 = input("Crea tu contrasena: ")
p2 = input("Confirma tu contrasena: ")

intentos = 1

while p1 != p2 and intentos < 3:
    print("No coinciden. Llevas", intentos, "intentos.")
    p2 = input("Intenta confirmar de nuevo: ")
    intentos = intentos + 1

if p1 == p2:
    print("Contrasena correcta.")
else:
    print("Cuenta cancelada.")