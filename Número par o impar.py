import random

numero = random.choice([2, 4, 6, 8, 10, 12, 14, 16, 18, 20])
intentos = 5


print("adivina el numero par")

while intentos > 0:
    adivina=int(input("ingresa el numero"))
    if adivina % 2 == 1:
        print("escribe numeros pares")
    elif adivina==numero:
        print("felicidades")
        break
   
    elif adivina > numero:
        print("subete")

    elif adivina < numero:
        print("bajete")

    


    intentos -= 1


    

if intentos == 0:
    print("papito noote que quedan intentos ")