clave = int(input("ingresa la clave"))

intento= 0
while clave !=333:
    if intento ==2:
        print("se acabo")
        break
    
    print("contraseña incorrecta")
    clave = int(input("ingresa la clave"))
    intento += 1

if clave ==333:
    print("acceso completado")

