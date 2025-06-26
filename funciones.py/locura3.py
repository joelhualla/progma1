import operator

ventas = {
    "Valentina": 5200,
    "Jorge": 3100,
    "Camila": 7800,
    "Ignacio": 4300,
    "Fernanda": 2500
}



mayor=max(ventas.items(), key=operator.itemgetter(1))
print(f"es que hizo mas venta fue {mayor[0]} por {mayor[1]}")

menor= min(ventas.items(), key=operator.itemgetter(1))
print(f"la que tiene menos venta es {menor[0]} con {menor[1]}")

ranking= sorted(ventas.items(), key=operator.itemgetter(1 ), reverse=True)



for i, (vendedor, venta) in enumerate(ranking, start=1 ):
    print(f"{i} {vendedor}con {venta}")




    
