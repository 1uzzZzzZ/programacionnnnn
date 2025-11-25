# 17.- Calculo de beneficio
precio_venta = float(input("Precio de venta por pieza: "))
cantidad_vendida = int(input("Cantidad vendida: "))
costo_fijo = float(input("Costo fijo total: "))
costo_variable = float(input("Costo variable por pieza: "))

ingreso_total = precio_venta * cantidad_vendida
costo_total = costo_fijo + (costo_variable * cantidad_vendida)
beneficio = ingreso_total - costo_total

print("El beneficio total es:", beneficio)