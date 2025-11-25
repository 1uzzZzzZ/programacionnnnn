import matplotlib.pyplot as plt
import statistics
import random
from collections import Counter
import numpy as np

# --- 14.2 Estadística básica ---
# Generar conjunto de datos aleatorios (edades entre 18 y 60)
datos = [random.randint(18, 60) for _ in range(50)]

media = statistics.mean(datos)
mediana = statistics.median(datos)
try:
    moda = statistics.mode(datos)
except:
    moda = "Multimodal"

print(f"Media: {media:.2f}, Mediana: {mediana}, Moda: {moda}")

# Graficar histograma
plt.figure(figsize=(10, 4))
plt.subplot(1, 3, 1)
plt.hist(datos, color='skyblue', edgecolor='black')
plt.title('14.2 Estadística: Histograma')

# --- 14.3 Tablas de frecuencias (Texto) ---
texto = "python datos codigo python analisis datos python visualizacion codigo"
palabras = texto.split()
frecuencias = Counter(palabras)

nombres = list(frecuencias.keys())
valores = list(frecuencias.values())

plt.subplot(1, 3, 2)
plt.bar(nombres, valores, color='salmon')
plt.title('14.3 Frecuencia de Palabras')

# --- 14.5 Visualización de 3 funciones distintas ---
x = np.linspace(0, 10, 100)
lineal = x
exponencial = np.exp(x * 0.5) # Escalado para que no sea tan grande
trigonometrica = np.sin(x) * 10

plt.subplot(1, 3, 3)
plt.plot(x, lineal, label='Lineal', linestyle='--')
plt.plot(x, exponencial, label='Exponencial', color='red')
plt.plot(x, trigonometrica, label='Seno', color='green')
plt.title('14.5 Funciones Matemáticas')
plt.legend()

plt.tight_layout()
plt.show()