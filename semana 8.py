import pandas as pd

data = {
    'Categoria': ['Electrónica', 'Ropa', 'Electrónica', 'Hogar', 'Ropa', 'Hogar'],
    'Producto': ['TV', 'Camisa', 'Radio', 'Mesa', 'Pantalón', 'Silla'],
    'Ventas': [1000, 50, 30, 150, 60, 80]
}

df = pd.DataFrame(data)

# Agrupar por Categoría y sumar ventas
resumen = df.groupby('Categoria')['Ventas'].sum()

print("Total de ventas por categoría:")
print(resumen)