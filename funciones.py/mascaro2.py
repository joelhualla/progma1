productos = {
    "Monitor": 120,
    "Teclado": 30,
    "Mouse": 25,
    "Laptop": 800
}

mas_caro=""
mayor_precio=0

for producto, precio in productos.items():
    if precio > mayor_precio:
        mayor_precio= precio
        mas_caro = producto

print(f"el producto mas caro es {mas_caro} y su precio es {mayor_precio}")