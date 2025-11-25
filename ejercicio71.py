# 71.- Libreria sympy (Ecuaciones)
import sympy as sp

x = sp.Symbol('x')

# a) x^2 - 5x + 7 = 0
eq1 = x**2 - 5*x + 7
sol1 = sp.solve(eq1, x)
print("Solucion a):", sol1)

# b) 7x^2 + 9x - 7 = 8x^2 - 2x - 3
# Pasamos todo a un lado: (7x^2 + 9x - 7) - (8x^2 - 2x - 3) = 0
lhs = 7*x**2 + 9*x - 7
rhs = 8*x**2 - 2*x - 3
eq2 = lhs - rhs
sol2 = sp.solve(eq2, x)
print("Solucion b):", sol2)