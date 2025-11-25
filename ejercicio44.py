# 44.- Calculadora basica con repeticion
opcion = "s"

while opcion != "n":
    print("1. Suma")
    print("2. Resta")
    print("3. Multiplicacion")
    print("4. Division")
    print("5. Exponente")
    print("6. Modulo")
    
    eleccion = int(input("Elige una operacion (1-6): "))
    n1 = float(input("Numero 1: "))
    n2 = float(input("Numero 2: "))
    
    if eleccion == 1:
        print("Resultado:", n1 + n2)
    elif eleccion == 2:
        print("Resultado:", n1 - n2)
    elif eleccion == 3:
        print("Resultado:", n1 * n2)
    elif eleccion == 4:
        print("Resultado:", n1 / n2)
    elif eleccion == 5:
        print("Resultado:", n1 ** n2)
    elif eleccion == 6:
        print("Resultado:", n1 % n2)
    else:
        print("Opcion no valida")
        
    opcion = input("Deseas realizar otra operacion? (s/n): ")