opcion = 0 

while opcion !=4:
    print(" ¿que desea hacer? ")
    print(" 1. sumar dos numeros ")
    print(" 2. restar dos numeros ")
    print(" 3. multiplicar dos numeros ")
    print("4. salir")

    opcion = int(input("elije una opcion "))

    if opcion == 1:
        a = int(input("ingresa el primer numero"))
        b = int(input("ingresa el segundo numero"))
        resultado = a + b 
        print(f"el resultado de la suma de {a} + {b} =", resultado)

    elif opcion == 2:
        a = int(input("ingresa el primer numero"))
        b = int(input("ingresa el segundo numero"))
        resultado = a - b 
        print(f"el resultado de la resta de {a} - {b} = ", resultado)

    elif opcion == 3:
        a = int(input("ingresa el primer numero"))
        b = int(input("ingresa el segundo numero"))
        resultado = a * b 
        print(f"el resultado de la multiplicacion de {a} x {b} es = ", resultado)

    elif opcion == 4:
        print("adios")
        break

    else:
        print("elije una opcion correcta")

        
        

    










         

    

       





    

