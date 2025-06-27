import random

numero1 = random.randint(1,20)
intento = 5
print("tiene que adivinar un numero del 1 al 20 ")

while intento > 0:
    numero2= int(input(f"ingresa un numero tienes {intento} intentos"))
    if numero2 == numero1:
        print("felicidades lo adivinaste waton")
        break
    elif numero2 < numero1:
        print ("te falta calle pa subete")
    elif numero2 > numero1:
        print ("muxa aura paaaaaa baja un poco porfaa")

    intento -=1
   

if intento == 0:
    print("se acabo" )
    print(f"el numero era {numero1}")
    

        
        





       


    




