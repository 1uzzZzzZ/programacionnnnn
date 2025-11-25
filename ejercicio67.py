# 67.- Multiples funciones de listas
def ordena_creciente(lista):
    lista.sort()
    return lista

def ordena_decreciente(lista):
    lista.sort(reverse=True)
    return lista

def elimina_indice(lista, indice):
    valor = lista.pop(indice)
    return valor

def elimina_dato(lista, dato):
    lista.remove(dato)
    return lista

def estadisticas(lista):
    p = sum(lista) / len(lista)
    ma = max(lista)
    mi = min(lista)
    return p, ma, mi

# Programa principal
numeros = [5, 2, 9, 1, 8]
print("Original:", numeros)

print("Creciente:", ordena_creciente(numeros))
print("Decreciente:", ordena_decreciente(numeros))

eliminado = elimina_indice(numeros, 0)
print("Elimine el indice 0, valor:", eliminado)
print("Queda:", numeros)

numeros = elimina_dato(numeros, 2) # Elimina el valor 2 si existe
print("Despues de borrar el 2:", numeros)

prom, mayor, menor = estadisticas(numeros)
print("Prom:", prom, "Max:", mayor, "Min:", menor)