# 20.- Calculo de salario con horas extra
# Base: 40 horas a 63 pesos. Extra: 80 pesos c/u.
horas_extra = int(input("Cantidad de horas extra trabajadas: "))

pago_base = 40 * 63
pago_extra = horas_extra * 80
salario_total = pago_base + pago_extra

print("Salario semanal total:", salario_total)