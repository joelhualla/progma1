suma = 0
contador = 0

numero = int(input("Ingresa un número (se sumará hasta pasar 100): "))

while suma <= 100:
    suma += numero
    contador += 1

    if suma > 100:
        break

    numero = int(input("Ingresa otro número: "))

print(f"La suma total es {suma}")
print(f"Ingresaste {contador} números")

4
    