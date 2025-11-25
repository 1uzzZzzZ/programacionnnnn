# 36.- Repetir elevacion al cuadrado
respuesta = "si"

while respuesta == "si":
    numero = int(input("Ingresa un numero: "))
    print("El cuadrado es:", numero * numero)
    
    respuesta = input("Deseas ingresar otro numero? (si/no): ")