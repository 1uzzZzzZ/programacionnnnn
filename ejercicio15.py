# 15.- Precio con IVA
producto = input("Nombre del producto: ")
precio_sin_iva = float(input("Precio sin IVA: "))

precio_final = precio_sin_iva * 1.16

print("Producto:", producto)
print("Precio con IVA (16%):", precio_final)