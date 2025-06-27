import operator


ventas = {
    "Carlos": 1500,
    "Laura": 3200,
    "Javiera": 2500,
    "Tomás": 4000,
    "María": 2900
}


venta_max = max(ventas.items(), key=operator.itemgetter(1))
print(f"la venta mas alta la tiene {venta_max[0]} con {venta_max[1]}")


venta_menor = min(ventas.items(), key=operator.itemgetter(1))
print(f"la ventas minima las hizo el señor {venta_menor[0]}  con {venta_menor[1]}")


ranking=sorted(ventas.items(), key=operator.itemgetter(1), reverse=True)

for i, (nombre,venta) in enumerate(ranking, start=1):
    print(f"{i}.{nombre}:{venta} puntos")
