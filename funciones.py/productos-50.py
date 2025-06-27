productos = {"Lápiz": 10, "Cuaderno": 55, "Goma": 8, "Regla": 40}
print(f"los productos que vales menos de 50 son ")
for producto, valor in productos.items():
    
    if valor < 50:
        print(f"{producto} que vale {valor}")