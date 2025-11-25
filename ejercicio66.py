# 66.- Separar reprobados
def obtener_reprobados(nombres, calificaciones):
    lista_reprobados = []
    # Recorremos por indice
    for i in range(len(nombres)):
        if calificaciones[i] < 6:
            lista_reprobados.append(nombres[i])
    return lista_reprobados

# Datos de prueba
n = ["Ana", "Juan", "Pedro", "Luis"]
c = [10, 5, 8, 4]

reprobados = obtener_reprobados(n, c)
print("Alumnos reprobados:", reprobados)