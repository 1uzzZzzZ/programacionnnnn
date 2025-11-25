# 81.- Escribir sin borrar (append)
frase = input("Escribe una frase para agregar: ")

try:
    with open("registro.txt", "a") as f:
        f.write(frase + "\n")
    print("Frase agregada.")
except Exception as e:
    print("Error:", e)