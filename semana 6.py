import pandas as pd
import os

# 1. Crear datos y guardarlos en un CSV (simulando un archivo externo)
datos = {
    'Estudiante': ['Ana', 'Beto', 'Carla', 'Daniel', 'Elena'],
    'Edad': [20, 21, 19, 22, 20],
    'Calificacion': [8.5, 9.0, 7.5, 9.5, 8.0]
}
df_inicial = pd.DataFrame(datos)
df_inicial.to_csv('estudiantes.csv', index=False)
print("Archivo 'estudiantes.csv' creado exitosamente.")

# 2. Leer el archivo CSV
df_leido = pd.read_csv('estudiantes.csv')

# 3. Calcular promedio
promedio = df_leido['Calificacion'].mean()

print("\nContenido del archivo:")
print(df_leido)
print(f"\nEl promedio de la clase es: {promedio}")