import requests
import json

# --- ACTIVIDAD 13.1 y 13.2: Consumo de API y Validación ---

# Definimos la URL de la API (Endpoint para obtener información de un Pokémon)
url = "https://pokeapi.co/api/v2/pokemon/pikachu"

print(f"Consultando API: {url}...")

# Realizamos la petición GET
respuesta = requests.get(url)

# Validamos el código de estado (200 significa éxito)
if respuesta.status_code == 200:
    print("Conexión exitosa (Código 200)")
    
    # --- ACTIVIDAD 13.3: Manejo de JSON y Estadísticas ---
    datos = respuesta.json()

    # Extraemos información relevante
    nombre = datos['name']
    peso = datos['weight']
    altura = datos['height']
    habilidades = datos['abilities']

    print("-" * 30)
    print(f"RESUMEN DE DATOS:")
    print(f"Nombre: {nombre.capitalize()}")
    print(f"Peso: {peso}")
    print(f"Altura: {altura}")
    
    # Procesar datos para mostrar estadísticas (contar habilidades)
    cantidad_habilidades = len(habilidades)
    print(f"Número total de habilidades: {cantidad_habilidades}")
    
    print("Lista de habilidades:")
    for elemento in habilidades:
        nombre_habilidad = elemento['ability']['name']
        print(f" - {nombre_habilidad}")
        
else:
    print(f"Error al conectar con la API. Código: {respuesta.status_code}")