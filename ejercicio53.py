# 53.- Recibir n datos hasta decir "no" y ordenar
lista = []
seguir = "si"

while seguir == "si":
    dato = float(input("Ingresa un numero: "))
    lista.append(dato)
    seguir = input("Agregar otro? (si/no): ")

lista.sort()
print("Lista ordenada:", lista)