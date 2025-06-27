duplicado = set()
nombres = ""

while nombres != "333":
    nombres = input("Ingresa un nombre: ").strip()
    
    if nombres == "333":
        break  # Finaliza el bucle si se ingresa "333"

    if nombres in duplicado:
        print(f"⚠️ El nombre '{nombres}' está repetido")
    else:
        duplicado.add(nombres)
        print(f"✅ Nombre '{nombres}' agregado")