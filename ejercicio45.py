# 45.- Calculadora con repeticion por operacion
programa_activo = True

while programa_activo:
    print("1. Suma | 2. Resta | 3. Multiplicacion | 4. Division")
    operacion = int(input("Que operacion deseas trabajar? "))
    
    repetir_operacion = True
    
    while repetir_operacion:
        n1 = float(input("Dato 1: "))
        n2 = float(input("Dato 2: "))
        
        if operacion == 1:
            print("Suma:", n1 + n2)
        elif operacion == 2:
            print("Resta:", n1 - n2)
        elif operacion == 3:
            print("Multi:", n1 * n2)
        elif operacion == 4:
            print("Div:", n1 / n2)
            
        res = input("Repetir la MISMA operacion? (si/no): ")
        if res != "si":
            repetir_operacion = False
    
    res_general = input("Quieres cambiar de operacion? (si/no): ")
    if res_general != "si":
        programa_activo = False