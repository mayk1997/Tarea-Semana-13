def promedio_temperatura(ciudades_temperaturas):
    # Implemento un diccionario vacío para guardar las medias de temperatura.
    promedio_temperatura = {}

    # Hago una iteración sobre cada ciudad y su lista de temperaturas en el diccionario de entrada
    for ciudad, temperaturas in ciudades_temperaturas.items():
        # Cálculo del promedio
        promedio = sum(temperaturas) / len(temperaturas)
        # Guardo el promedio calculado en el diccionario de resultados
        promedio_temperatura[ciudad] = promedio

    # Devuelvo el diccionario que contiene los promedios de temperatura por ciudad
    return promedio_temperatura

# Hago un diccionario de ciudades y temperaturas
ciudades_temperaturas = {
    "Loja": [30, 31, 30, 27, 29, 29, 30, 29, 29, 30, 29, 30, 28, 29],
    "Manabi": [24, 23, 24, 23, 24, 25, 25, 22, 21, 22, 21, 21, 20, 22],
    "Riobamba": [18, 18, 17, 16, 18, 19, 20, 21, 18, 18, 16, 16, 17, 19],
    "Tulcan": [34, 34, 31, 31, 32, 31, 32, 31, 31, 34, 33, 33, 33, 32],
}

# Llamo a la función con el diccionario de ciudades y temperaturas
promedio_temperatura = promedio_temperatura(ciudades_temperaturas)

# Imprimo los resultados
print("Las temperaturas promedio por ciudad son:")
for ciudad, promedio in promedio_temperatura.items():
    print(f"{ciudad}: {promedio:.2f}°C")