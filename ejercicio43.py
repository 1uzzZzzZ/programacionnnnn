# 43.- Acumulador de abonos
total = 0

while total <= 100000:
    print("Llevas acumulado:", total)
    abono = float(input("Cantidad a abonar? "))
    
    if abono < 0:
        print("Error: No se aceptan cantidades negativas.")
    else:
        total = total + abono

print("Meta superada. Total final:", total)