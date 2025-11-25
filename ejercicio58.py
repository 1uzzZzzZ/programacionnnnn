# 58.- Funcion para llenar lista
def llenar_lista():
    nueva_lista = []
    print("Ingresa 5 numeros:")
    for i in range(5):
        n = int(input("Numero: "))
        nueva_lista.append(n)
    return nueva_lista

# Probando la funcion
mi_lista = llenar_lista()
print("Lista creada:", mi_lista)