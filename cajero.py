dinero = 1000

opcion= 0

while opcion != 4:
    print("bienvenido al cajero")
    print("1. consultar saldo")
    print("2. depositar dinero")
    print("3. retira diner")
    print("4. Salir")

    opcion=int(input("ingresa la opcion"))

    if opcion == 1:
        print(f"su saldo{dinero}")

    elif opcion == 2:
        deposito=int(input("ingresa el monto del deposito"))
        dinero = deposito + dinero
        print(f"su dinero actual es{dinero}")

    elif opcion == 3:
        retiro= int(input("ingresa el monto del retiro"))

        while retiro > dinero:
            print("monto retirado supera monto de la cuenta")
            retiro=int(input("ingresa el monto del retiro"))

        else:
            dinero = dinero =- retiro

    
    

        
    
    elif opcion == 4:
        break
        
print(" adios ")

        

        
        

    








    


