# 63.- Lista al cuadrado (funcion)
def lista_cuadrados(lista_original):
    nueva = []
    for num in lista_original:
        nueva.append(num ** 2)
    return nueva

numeros = [2, 3, 4, 5]
res = lista_cuadrados(numeros)
print("Cuadrados:", res)