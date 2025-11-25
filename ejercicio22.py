# 22.- Calificacion de examen
preguntas_totales = int(input("Total de preguntas del examen: "))
preguntas_correctas = int(input("Aciertos (preguntas correctas): "))

# Regla de tres para escala de 0 a 10
calificacion = (preguntas_correctas / preguntas_totales) * 10

print("La calificacion final es:", calificacion)