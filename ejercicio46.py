# 46.- Lista de 10 datos al cuadrado
lista = []
print("Ingresa 10 numeros:")

for i in range(10):
    num = int(input("Numero: "))
    lista.append(num)

print("Resultados elevados al cuadrado:")
for n in lista:
    print(n ** 2)