opcion = 0

while opcion != 3:
    print("Menu:")
    print("1. saludar hola:")
    print("2. la tablas:")
    print("3. salir:")

    opcion=int(input("ingresa una opcion"))

    if opcion == 1:
        print("hola como esta")

    elif opcion == 2:
        numero = int(input("ingrese un numero"))
        i = 1
        while i <=10:
            resultado =numero * i
            print(f"la tabla de {numero} x {i} es igual", resultado)

            i += 1

    elif opcion == 3:
        break

    else:
        print("ingresa un opcion correcta")
        
        
    

    
    
        
        

print("adios")
   
  

     