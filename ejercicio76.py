# 76.- Graficar con matplotlib
import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5]
y = [2, 4, 1, 8, 7]

plt.plot(x, y, marker='o')
plt.title("Grafica de Datos")
plt.xlabel("Eje X")
plt.ylabel("Eje Y")

plt.savefig("grafica.png")
print("Grafica guardada como grafica.png")
plt.show()