# 64.- Es Multiplo
def es_multiplo(n1, n2):
    if n1 % n2 == 0:
        return True
    else:
        return False

a = int(input("Numero A: "))
b = int(input("Numero B: "))

if es_multiplo(a, b):
    print(a, "es multiplo de", b)
else:
    print(a, "no es multiplo de", b)