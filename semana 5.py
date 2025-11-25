import pandas as pd

# Datos para el DataFrame
datos = {
    'Nombre': ['Luis', 'Marta', 'Pedro', 'Sofia'],
    'Puntuacion': [85, 92, 78, 95]
}

# Crear el DataFrame
df = pd.DataFrame(datos)

# Filtrar puntuaciones mayores a 80
df_filtrado = df[df['Puntuacion'] > 80]

print("DataFrame original:")
print(df)
print("\nDataFrame filtrado (Puntuación > 80):")
print(df_filtrado)