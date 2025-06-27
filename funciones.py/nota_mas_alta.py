notas = {
    "Lucía": 80,
    "Pedro": 95,
    "Ana": 100,
    "Sofía": 70
}

nota_alta=0
nombre=""
for nombre, nota in notas.items():
    if nota > nota_alta:
        nota_alta = nota
        nombre_final=nombre
       
       
print(f" la nota mas alta es {nota_alta}del alumno {nombre_final}")