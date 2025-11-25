# 56.- Agregar 10 numeros consecutivos
lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]

# Tomamos el ultimo valor
ultimo = lista[-1]

# Agregamos 10 mas
for i in range(1, 11):
    lista.append(ultimo + i)

print("Lista extendida:", lista)