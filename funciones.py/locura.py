import operator  # Módulo para ordenar fácilmente

notas = {
    "Lucía": 80,
    "Pedro": 95,
    "Ana": 100,
    "Sofía": 70,
    "Leo": 60
}

# Obtener el alumno con la nota más alta
mayor = max(notas.items(), key=operator.itemgetter(1))
print(f"🥇 Nota más alta: {mayor[0]} con {mayor[1]} puntos")

# Obtener el alumno con la nota más baja
menor = min(notas.items(), key=operator.itemgetter(1))
print(f"🥄 Nota más baja: {menor[0]} con {menor[1]} puntos")

# Ordenar todos del mayor al menor
ranking = sorted(notas.items(), key=operator.itemgetter(1), reverse=True)

print("\n📊 Ranking completo:")
for i, (alumno, nota) in enumerate(ranking, start=1):
    print(f"{i}. {alumno}: {nota} puntos")