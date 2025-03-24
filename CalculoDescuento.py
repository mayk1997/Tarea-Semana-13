 #Definimos la funcion
def calcular_descuento(valor_total, valor_desc=25):
    # Calcular el descuento
    descuento = valor_total * (valor_desc / 100)
    #retornamos el valor descuento
    return descuento

# LLamamos a la funcion y mostramos el valor final
total_1 = 254.99  # Valor sin descuento
descuento_1 = calcular_descuento(total_1)  # Llamamos a la funcion y guardamos en valot total 1
valor_final_1 = total_1 - descuento_1  # Calcular el monto final a pagar restando el descuento del valor total.

# Llamamos a la funcion con los parametros para el descuento de la siguiente compra
total_2 = 987.46  # Valor sin descuento
desc_2 = 30  # Porcentaje de descuento
descuento_2 = calcular_descuento(total_2, desc_2)  # Llamamos a la funcion y cambiamos los parametros con los valores del 2do descuento
valor_final_2 = total_2 - descuento_2  # Valor final con descuento

# Muestra del porcentaje de descuento y el valor final

print(f"Compra #1 sin descuento es: {total_1:.3f}, "
      f"porcentaje de descuento es 25%, "
      f"el valor en cnatidad del descuento es = {descuento_1:.3f}, "
      f"el precio final es = {valor_final_1:.3f}")
print(f"Compra #2 sin descuento es: {total_2:.3f}, "
      f"porcentaje de descuento es: {desc_2}%, "
      f"el valor en cantidad del descuento es = {descuento_2:.3f}, "
      f"el precio final es = {valor_final_2:.3f}")