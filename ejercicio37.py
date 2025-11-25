# 37.- Interes compuesto con repeticion
continuar = "si"

while continuar == "si":
    capital = float(input("Capital inicial: "))
    tasa = float(input("Tasa de interes (decimal, ej 0.10): "))
    periodos = int(input("Numero de periodos: "))
    
    # Formula M = C * (1 + i)^n
    monto = capital * ((1 + tasa) ** periodos)
    print("Monto final:", monto)
    
    continuar = input("Deseas hacer otro calculo? (si/no): ")