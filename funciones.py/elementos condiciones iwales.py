numeros = {"a": 30, "b": 25, "c": 40, "d": 15}
contador = 0

for clave, valor in numeros.items():
    if valor > 20:
        contador += 1

print(f"Hay {contador} valores mayores que 20")