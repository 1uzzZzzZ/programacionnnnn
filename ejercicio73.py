# 73.- Integracion numerica scipy
import numpy as np
from scipy.integrate import quad

def f(x):
    return np.sin(x**2)

# Integral de 0 a 2
resultado, error = quad(f, 0, 2)

print(f"Resultado de la integral: {resultado:.5f}")