import random
while True:
    
    Nombre_machine = ["Robert","Albert", "Braulio","Mariano","Alex"]

    machine = random.choice(Nombre_machine)   

    nombre = str(input(f" Hola!! soy {machine}, y vos, ¿Como te llamas?\n"))

    user = str(input(f"{nombre}, elige: Piedra, papel o tijera ...\n")).lower()

    user2 = [ "piedra","tijera", "papel"]

    resultado = random.choice(user2)

    def juego (a,b):
        
        name = nombre[-1]

        if a == b :
            print (f"Empate!, {machine } eligió {resultado}")

        elif a == "piedra" and b == "tijera":
            print (f"Ganasteeeeeeeeee {nombre + str(name) + str(name) + str(name)} , {machine} eligió {resultado}")
                     
        elif a == "piedra" and b == "papel":
            print (f"Noooo te ganó {machine}, {machine} había eligido {resultado}")
             
        elif a == "papel" and b == "piedra":
            print (f"Bestiaaaaa ganasteee {nombre + str(name) + str(name) + str(name)}, {machine} eligió {resultado}")
               
        elif a == "papel" and b == "tijera":
            print (f"Ganó {machine} :( , {machine} eligió {resultado}, suerte la proxima ;)")
              
        elif a == "tijera" and b == "papel":
            print (f"Biennnn ahí, {nombre + str(name) + str(name) + str(name) } ganasteeee , {machine} eligió {resultado}")
              
        elif a == "tijera" and b == "piedra":
            print (f" {machine}: jajajajaj perdisteee, yo elegí {resultado}")
              
        else:
            print ("Coloque piedra papel o tijera,intente nuevamente...")
    
    juego(user,resultado)
    
    jugar_de_nuevo = input("Querés jugar de vuelta? Si/No:  ")
        
    if jugar_de_nuevo.lower() == "no":
        print(f"Gracias por jugar {nombre}")
        break
    
    