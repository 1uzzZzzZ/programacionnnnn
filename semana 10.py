class Rectangulo:
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def calcular_area(self):
        return self.base * self.altura

# Uso de la clase
mi_rectangulo = Rectangulo(10, 5)
area = mi_rectangulo.calcular_area()

print(f"El rectángulo con base {mi_rectangulo.base} y altura {mi_rectangulo.altura}")
print(f"Tiene un área de: {area}")