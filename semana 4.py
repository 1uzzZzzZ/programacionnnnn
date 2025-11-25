import numpy as np

# Crear array de 10 números enteros aleatorios entre 1 y 100
datos = np.random.randint(1, 101, 10)

# Calcular media y máximo
media = np.mean(datos)
maximo = np.max(datos)

print(f"El array generado es: {datos}")
print(f"La media de los datos es: {media}")
print(f"El valor máximo es: {maximo}")