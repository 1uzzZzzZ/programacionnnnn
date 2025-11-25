# 70.- Libreria math
import math as mt

# a) Seno de 45 (en radianes) + cos(pi)
# Convertimos 45 grados a radianes
rad45 = mt.radians(45)
res_a = mt.sin(rad45) + mt.cos(mt.pi)

# b) Raiz de euler a la 2
# euler es mt.e
res_b = mt.sqrt(mt.e ** 2)

# c) Redondear pi * raiz de 2
val = mt.pi * mt.sqrt(2)
res_c = round(val, 3)

print("a)", res_a)
print("b)", res_b)
print("c)", res_c)