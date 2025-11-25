# 62.- Calificacion final
def evaluar_semestre(c1, c2, c3):
    prom = (c1 + c2 + c3) / 3
    if prom < 6:
        print("Te vas a extra")
    return prom

cal1 = float(input("Calificacion 1: "))
cal2 = float(input("Calificacion 2: "))
cal3 = float(input("Calificacion 3: "))

final = evaluar_semestre(cal1, cal2, cal3)
print("Promedio final:", final)