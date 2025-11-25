# 48.- Busqueda por indice en 3 listas
n = int(input("Cuantos productos vas a registrar? "))

prod_nombres = []
prod_claves = []
prod_stock = []

for i in range(n):
    print("Producto", i)
    nm = input("Nombre: ")
    cl = input("Clave: ")
    st = int(input("Cantidad: "))
    
    prod_nombres.append(nm)
    prod_claves.append(cl)
    prod_stock.append(st)

idx = int(input("Introduce el indice (posicion) a buscar: "))

if idx >= 0 and idx < n:
    print("Nombre:", prod_nombres[idx])
    print("Clave:", prod_claves[idx])
    print("Stock:", prod_stock[idx])
else:
    print("Indice invalido")