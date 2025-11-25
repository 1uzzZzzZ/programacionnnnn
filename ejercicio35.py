# 35.- Orden descendente de tres numeros (Sin listas)
a = int(input("Numero 1: "))
b = int(input("Numero 2: "))
c = int(input("Numero 3: "))

print("Orden descendente:")

if a >= b and a >= c:
    if b >= c:
        print(a, b, c)
    else:
        print(a, c, b)
elif b >= a and b >= c:
    if a >= c:
        print(b, a, c)
    else:
        print(b, c, a)
else:
    # C es el mayor
    if a >= b:
        print(c, a, b)
    else:
        print(c, b, a)