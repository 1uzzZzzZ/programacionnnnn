# 30.- Analisis de beneficios
precio = float(input("Precio unitario: "))
cantidad = int(input("Cantidad vendida: "))
egresos = float(input("Total de egresos: "))

ingresos = precio * cantidad

print("Ingresos totales:", ingresos)

if ingresos < egresos:
    print("Estado: En perdidas")
elif ingresos == egresos:
    print("Estado: Punto de equilibrio")
else:
    print("Estado: Generando ganancias")