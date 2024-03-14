def calcular_descuento(monto_total, porcentaje_descuento=10):
    descuento = monto_total * (porcentaje_descuento / 100)
    return descuento

# Llamada a la función con solo el monto total de la compra
monto_compra = 100
descuento1 = calcular_descuento(monto_compra)
print(f"Descuento 1: {descuento1}")

# Llamada a la función con el monto total de la compra y un porcentaje de descuento específico
descuento2 = calcular_descuento(monto_compra, 20)
print(f"Descuento 2: {descuento2}")
