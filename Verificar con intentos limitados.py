clave = 333

intentos = 3

print("adivina la clave")

while intentos > 0:
    numero= int(input("ingresa un numero"))
    if numero == clave:
        print("acceso completo")
        break
    elif numero != clave:
        print("te equivocaste")

    intentos  -= 1

if intentos == 0:
    print("se te acabaron los intentos")
        
        

    


