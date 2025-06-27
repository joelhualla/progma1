notas = {"Juan": 58, "Valentina": 92, "Pedro": 74, "Laura": 45}

for alumno, nota in notas.items():
    if nota >= 60:
        print(f"{alumno} APROBADO")
