# 61.- Perimetro rectangulo
def perimetro_rect(base, altura):
    return (2 * base) + (2 * altura)

b = float(input("Base: "))
a = float(input("Altura: "))
print("Perimetro:", perimetro_rect(b, a))