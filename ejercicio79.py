# 79.- Crear archivo perfil.txt
nombre = input("Tu nombre: ")
edad = input("Tu edad: ")
carrera = input("Tu carrera: ")

try:
    with open("perfil.txt", "w") as f:
        f.write(nombre + "\n")
        f.write(edad + "\n")
        f.write(carrera + "\n")
    print("Archivo guardado correctamente.")
except Exception as e:
    print("Ocurrio un error al guardar:", e)