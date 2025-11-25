def dividir_numeros(a, b):
    try:
        resultado = a / b
        return resultado
    except ZeroDivisionError:
        return "Error: No se puede dividir entre cero."
    except TypeError:
        return "Error: Entrada no válida, se requieren números."

# Pruebas
print(f"10 / 2 = {dividir_numeros(10, 2)}")
print(f"5 / 0 = {dividir_numeros(5, 0)}")
print(f"10 / 'a' = {dividir_numeros(10, 'a')}")