# 47.- Calificaciones de n materias
n = int(input("Cuantas materias son? "))
nombres = []
promedios = []

for i in range(n):
    mat = input("Nombre de la materia: ")
    cal = float(input("Promedio de la materia: "))
    nombres.append(mat)
    promedios.append(cal)

print("--- REPORTE ---")
for i in range(n):
    print(nombres[i], ":", promedios[i])