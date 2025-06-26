productos = {
    "Monitor": 120,
    "Teclado": 30,
    "Mouse": 25,
    "Laptop": 800
}


mas_caro=""
precio_mayor=0

for producto, valor in productos.items():
    if valor > precio_mayor:
        precio_mayor=valor 
        mas_caro= producto

    
print(f"el {mas_caro} es {precio_mayor}")