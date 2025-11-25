# 68.- Numero primo
def es_primo(n):
    if n < 2:
        return False
    # Checar divisores desde 2 hasta n-1
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

num = int(input("Numero a verificar: "))
if es_primo(num):
    print("Es primo")
else:
    print("No es primo")