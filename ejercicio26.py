# 26.- Comparar dos numeros (Tema 3: If)
n1 = int(input("Numero 1: "))
n2 = int(input("Numero 2: "))

if n1 > n2:
    print(n1, "es mayor que", n2)
elif n2 > n1:
    print(n2, "es mayor que", n1)
else:
    print("Ambos numeros son iguales")