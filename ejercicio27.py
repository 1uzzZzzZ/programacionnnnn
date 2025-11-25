# 27.- Area o perimetro de un cuadrado
opcion = input("Deseas calcular Area (A) o Perimetro (P)?: ")
lado = float(input("Ingresa el valor del lado del cuadrado: "))

if lado < 0:
    print("Error: El lado debe ser positivo.")
else:
    if opcion == "A" or opcion == "a":
        area = lado * lado
        print("El area es:", area)
    elif opcion == "P" or opcion == "p":
        perimetro = lado * 4
        print("El perimetro es:", perimetro)
    else:
        print("Error: Opcion no valida.")