import random

numero = random.randint(1,10)

print("adivina un numero del 1 al 10")

numero1 = 0

while numero1 != numero:
    numero1 = int(input("ingresa un numero "))
    
    if numero1 < numero:
        print("sube")
    elif numero1 > numero:
        print("bajate")

    
   
    

print("felicidades encontraste el numero")



    
    



