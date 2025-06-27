import operator
notas = {
    "Ana": 65,
    "Luis": 58,
    "Carlos": 70,
    "Javiera": 42,
    "Tomás": 55,
    "Lucía": 35,
    "Pedro": 60,
    "Valentina": 67,
    "Diego": 50,
    "Sofía": 25
}


aprobado= [ (nombre,nota)for nombre, nota in notas.items() if nota >= 60 ]

ordenados= sorted(aprobado, key=operator.itemgetter(1), reverse=True)

for medalla, (nombre, nota) in enumerate(ordenados, start=1):
    print(f"{medalla} {nombre}con {nota}")


          