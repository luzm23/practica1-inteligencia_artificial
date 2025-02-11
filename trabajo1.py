# Pedir el nombre y la materia
nombre = input("Ingresa tu nombre: ")
materia = input("Ingresa el nombre de la materia: ")
calificacion = int(input("Ingresa tu calificación: "))

# Verificar en qué rango está la calificación
if 95 <= calificacion <= 100:
    resultado = "Excelente"
elif 85 <= calificacion <= 90:
    resultado = "Bueno"
elif 70 <= calificacion <= 74:
    resultado = "Suficiente"
else:
    resultado = "N/A."

# Mostrar los resultados
print(f"\nNombre: {nombre}")
print(f"Materia: {materia}")
print(f"Calificación: {calificacion}")
print(f"Resultado: {resultado}")
