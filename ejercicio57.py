# 57.- Buscar valor sin usar 'in'
lista = [10, 20, 30, 40, 50]
buscado = int(input("Que numero buscas? "))

encontrado = False

for elemento in lista:
    if elemento == buscado:
        encontrado = True
        break # Detiene el ciclo si lo encuentra

if encontrado == True:
    print("El valor SI esta en la lista.")
else:
    print("El valor NO esta en la lista.")