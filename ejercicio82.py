# 82.- Combinar dos archivos
try:
    with open("a.txt", "r") as fa:
        data_a = fa.read()
        
    with open("b.txt", "r") as fb:
        data_b = fb.read()
        
    with open("combinado.txt", "w") as f_combo:
        f_combo.write(data_a + "\n" + data_b)
        
    print("Archivos combinados.")
except FileNotFoundError:
    print("Error: Falta el archivo a.txt o b.txt")