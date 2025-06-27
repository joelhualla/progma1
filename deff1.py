def chekeo(nombre, nota):
    try:
        nombre= str(nombre)
        nota=float(nota)
        if nota >= 60:
            print(F"TU chamaka del diablo {nombre}, aprobaste con {nota}")
        else:
            print(f"muchacha reporbaste con {nota}")
    except:print("escribie las cosa como ")
    
        

nombre=input("ingresa el nombre ")        
nota=input("ingresa una nota")
        
chekeo(nombre, nota)           
    

  
            
        
       
