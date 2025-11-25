# 31.- Evaluacion academica
calificacion = float(input("Ingresa calificacion (0-10): "))

if calificacion < 0 or calificacion > 10:
    print("Error: Calificacion fuera de rango.")
elif calificacion < 6:
    print("Situacion: Irregular")
elif calificacion < 10:
    # Cubre de 6 a 9.99...
    print("Situacion: Regular")
else:
    # Exactamente 10
    print("Situacion: Excelencia")