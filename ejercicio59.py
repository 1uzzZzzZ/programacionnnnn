# 59.- Funcion sumatoria
def calcular_sumatoria(lista_numeros):
    suma = 0
    for n in lista_numeros:
        suma = suma + n
    return suma

# Prueba
datos = [5, 5, 5]
print("La suma es:", calcular_sumatoria(datos))