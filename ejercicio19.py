# 19.- Promedio y datos del alumno
nombre = input("Nombre del alumno: ")
boleta = input("Numero de boleta: ")

c1 = float(input("Calificacion 1: "))
c2 = float(input("Calificacion 2: "))
c3 = float(input("Calificacion 3: "))
c4 = float(input("Calificacion 4: "))
c5 = float(input("Calificacion 5: "))

promedio = (c1 + c2 + c3 + c4 + c5) / 5

print("--- DATOS ---")
print("Nombre:", nombre)
print("Boleta:", boleta)
print("Promedio:", promedio)