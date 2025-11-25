# 60.- Funcion promedio usando sumatoria
# Copio la funcion anterior para usarla aqui
def calcular_sumatoria(lista_numeros):
    suma = 0
    for n in lista_numeros:
        suma = suma + n
    return suma

def calcular_promedio(lista):
    total = calcular_sumatoria(lista)
    cantidad = len(lista)
    if cantidad == 0:
        return 0
    return total / cantidad

mis_datos = [10, 9, 8, 10]
print("El promedio es:", calcular_promedio(mis_datos))