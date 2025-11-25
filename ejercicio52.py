# 52.- Reporte de ventas e ingresos
productos = []
precios = []
ventas = []

print("Ingresa datos de 5 productos:")
for i in range(5):
    print("Producto", i+1)
    p = input("Nombre: ")
    pr = float(input("Precio: "))
    v = int(input("Ventas: "))
    
    productos.append(p)
    precios.append(pr)
    ventas.append(v)

print("--- REPORTE ---")
for i in range(5):
    ingreso = precios[i] * ventas[i]
    print(productos[i], "| Precio:", precios[i], "| Ventas:", ventas[i], "| Ingreso:", ingreso)