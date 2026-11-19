import json
with open('data.json', 'r', encoding='utf-8') as file:
    data = json.load(file)

ventas = data['ventas']

# 1. Total facturado.
total = 0
for venta in ventas:
    total += venta['cantidad'] * venta['precio_unitario']

print("Total facturado:", f"{total:.2f}", "€")

# 2. Ventas por categoria.
por_categoria = {}
for venta in ventas:
    categoria = venta['categoria']
    importe = venta['cantidad'] * venta['precio_unitario']
    if categoria in por_categoria:
        por_categoria[categoria] = por_categoria[categoria] + importe
    else:
        por_categoria[categoria] = importe

print("Ventas por categoría:")
for categoria in por_categoria:
    print(" ", categoria, ":", f"{por_categoria[categoria]:.2f} €")

# 3. Producto más vendido (por unidades)
unidades = {}
for venta in ventas:
    producto = venta['producto']
    if producto in unidades:
        unidades[producto] += venta['cantidad']
    else:
        unidades[producto] = venta['cantidad']

mas_vendido= ""
maximo = 0
for producto in unidades:
    if unidades[producto] > maximo:
        maximo = unidades[producto]
        mas_vendido = producto

print("Producto más vendido:", mas_vendido, "con", maximo, "unidades")

