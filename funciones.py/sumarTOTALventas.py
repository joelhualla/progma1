ventas = {
    "Producto A": 150,
    "Producto B": 300,
    "Producto C": 200
}

total=0

for producto, monto in ventas.items():
    total += monto

print(f"el monto total es{total}")