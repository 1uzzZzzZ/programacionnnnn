# 24.- Interes simple y compuesto
capital = float(input("Capital inicial: "))
tasa = float(input("Tasa de interes anual (%): "))
periodos = int(input("Numero de periodos (anios): "))

# Convertir porcentaje a decimal (ej. 10% = 0.10)
i = tasa / 100

# Interes Simple: M = C * (1 + i*n)
monto_simple = capital * (1 + (i * periodos))

# Interes Compuesto: M = C * (1 + i)^n
monto_compuesto = capital * ((1 + i) ** periodos)

print("Capital Final (Interes Simple):", monto_simple)
print("Capital Final (Interes Compuesto):", monto_compuesto)