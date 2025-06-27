usuarios = {
    "Lucas": {"edad": 25, "rol": "admin"},
    "Ana": {"edad": 20, "rol": "usuario"},
    "Diego": {"edad": 30, "rol": "admin"},
    "Mar": {"edad": 17, "rol": "usuario"}
}

for nombre, datos in usuarios.items():
    if datos["rol"] == "admin" and datos["edad"] > 21:
        print(f"{nombre} es admin y tiene {datos['edad']} años")