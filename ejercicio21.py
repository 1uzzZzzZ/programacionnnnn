# 21.- Banquete por evento
nombre_evento = input("Nombre del evento: ")
# La fecha se pide pero no afecta el calculo
fecha = input("Fecha del evento: ") 
asistentes = int(input("Numero de asistentes: "))

# Calculos unitarios
agua_total = asistentes * 1.5
carne_total = asistentes * 350 # en gramos
salsa_total = agua_total * 0.25

print("--- REQUERIMIENTOS PARA", nombre_evento, "---")
print("Agua de jamaica (litros):", agua_total)
print("Carne (gramos):", carne_total)
print("Salsa (litros):", salsa_total))