# 34.- Clasificacion por edad
edad = int(input("Ingresa tu edad: "))

if edad < 0 or edad > 120:
    print("Edad invalida")
else:
    # Clasificacion
    if edad < 10:
        print("Clasificacion: Niño")
    elif edad <= 17:
        print("Clasificacion: Adolescente")
    elif edad <= 29:
        print("Clasificacion: Joven")
    elif edad <= 59:
        print("Clasificacion: Adulto")
    else:
        print("Clasificacion: Adulto mayor")
    
    # Mayor de edad
    if edad >= 18:
        print("(Es mayor de edad)")
    else:
        print("(Es menor de edad)")