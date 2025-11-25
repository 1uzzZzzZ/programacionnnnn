# 51.- Registro de asistencia
n = int(input("Cuantos trabajadores son? "))
trabajadores = []
asistencias = []

for i in range(n):
    nom = input("Nombre del trabajador: ")
    asis = int(input("Asistio? (1=Si, 0=No): "))
    trabajadores.append(nom)
    asistencias.append(asis)

print("--- Lista de Asistencia ---")
for i in range(n):
    texto = ""
    if asistencias[i] == 1:
        texto = "asistió"
    else:
        texto = "no asistió"
    
    print(trabajadores[i], texto, "a trabajar")