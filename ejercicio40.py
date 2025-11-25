# 40.- Repeticion hasta respuesta especifica
lenguaje = input("Cual es tu lenguaje de programacion favorito? ")

while lenguaje != "Python":
    lenguaje = input("Incorrecto. Intenta otra vez: ")

print("Exacto, es Python.")