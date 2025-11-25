# 55.- Menu de operaciones con listas
tipo = input("Quieres lista de numeros (n) o texto (t)? ")
lista = []

opcion = 0

while opcion != 6:
    print("\n--- MENU ---")
    print("1. Agregar")
    print("2. Eliminar")
    print("3. Ordenar")
    print("4. Buscar")
    print("5. Ver calculos (solo numeros)")
    print("6. Salir")
    
    opcion = int(input("Elige una opcion: "))
    
    if opcion == 1:
        val = input("Valor a agregar: ")
        if tipo == "n":
            val = float(val)
        lista.append(val)
        print("Lista actual:", lista)
        
    elif opcion == 2:
        val = input("Valor a eliminar: ")
        if tipo == "n":
            val = float(val)
        if val in lista:
            lista.remove(val)
            print("Eliminado.")
        else:
            print("No esta en la lista.")
            
    elif opcion == 3:
        lista.sort()
        print("Lista ordenada:", lista)
        
    elif opcion == 4:
        val = input("Valor a buscar: ")
        if tipo == "n":
            val = float(val)
        if val in lista:
            print("Si existe en el indice:", lista.index(val))
        else:
            print("No existe.")
            
    elif opcion == 5:
        if tipo == "n":
            print("Maximo:", max(lista))
            print("Minimo:", min(lista))
            print("Suma:", sum(lista))
            print("Promedio:", sum(lista)/len(lista))
        else:
            print("Opcion solo para numeros.")
            
    elif opcion == 6:
        print("Adios")