personas = {"Sofia": 17, "Carlos": 20, "Lucia": 15, "Andres": 21}

for nombre, edad in personas.items():
    if edad > 18:
        print(f"{nombre}")
