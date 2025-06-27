import random

numero = random.randint(1,101)

print("adivina el numero entre 1 y 100")

intentos= 7



while intentos  > 0:
    numero1=int(input("ingresa un numero "))
    if numero1 == numero:
        print("felicidades")
    elif numero1 < numero :
        print("sube")
    else:
        print (" baja")

    intentos -= 1


if intentos == 0:
           print(" se acabaron los intentos")

   

        





    