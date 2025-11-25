def celsius_a_fahrenheit(celsius):
    """Convierte una temperatura de Celsius a Fahrenheit."""
    return (celsius * 9/5) + 32

# Lista de temperaturas en Celsius
temps_celsius = [0, 20, 25, 30, 100]

print("Conversión de Temperaturas:")
for t in temps_celsius:
    t_fahr = celsius_a_fahrenheit(t)
    print(f"{t}°C equivale a {t_fahr}°F")