import operator

productos = {
    "Notebook": 750000,
    "Mouse": 12000,
    "Teclado": 25000,
    "Monitor": 180000,
    "Impresora": 90000,
    "Parlantes": 35000,
    "Silla Gamer": 150000,
    "Webcam": 30000 
    }


mayor= max(productos.items(), key=operator.itemgetter(1))

print(f"el producto mac caro es {mayor[0]} con {mayor[1]}")


import operator

productos = {
    "Notebook": 750000,
    "Mouse": 12000,
    "Teclado": 25000,
    "Monitor": 180000,
    "Impresora": 90000,
    "Parlantes": 35000,
    "Silla Gamer": 150000,
    "Webcam": 30000 
    }


mayor= max(productos.items(), key=operator.itemgetter(1))



ranking= sorted(productos.items(), key=operator.itemgetter(1), reverse=True)

for i, (producto,precio) in enumerate(ranking, start=1):
    print(f"{i} {producto} con {precio}")

