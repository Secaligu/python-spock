import random

choose_flag = True

while choose_flag:
    jugador = input("escoge entere piedra papel o tijeras spock lagarto").lower().strip()
    if jugador == "piedra":
        print("escojiste piedra")
        elecion = "piedra"
        choose_flag = False
    
    elif jugador == "papel":
        print("escogiste papel")
        elecion = "papel"
        choose_flag = False
    
    elif jugador == "tijeras":
        print("escogiste tijeras")
        elecion = "tijeras"
        choose_flag = False
   
    elif jugador == "spock":
        print("escogiste spock")
        elecion = "spock"
        choose_flag = False
   
    elif jugador == "lagarto":
        print("escogiste lagarto")
        elecion = "lagarto"
        choose_flag = False    
    else:
        print("opcion no existe")

elecion_PC = random.choice(["piedra", "papel", "tijeras", "spock","lagarto" ])
print(f"pvp {elecion} vs {elecion_PC}")

if elecion_PC == elecion:
    print("empate")
    #papel vs#
elif elecion_PC == "papel" and elecion == "piedra":
    print("perdiste")
elif elecion_PC == "papel" and elecion == "tijeras":
    print("ganaste")
elif elecion_PC == "papel" and elecion == "spock":
    print("perdiste")
elif elecion_PC == "papel" and elecion == "lagarto":
    print("ganaste")
    #piedra vs#
elif elecion_PC == "piedra" and elecion == "tijeras":
    print("perdiste")
elif elecion_PC == "piedra" and elecion == "lagarto":
    print("perdiste")
elif elecion_PC == "piedra" and elecion == "papel":
    print("ganaste")
elif elecion_PC == "piedra" and elecion == "spock":
    print("ganaste")

    #tijeras vs#
elif elecion_PC == "tijeras" and elecion == "piedra":
    print("ganaste")
elif elecion_PC == "tijeras" and elecion == "papel":
    print("perdistes")
elif elecion_PC == "tijeras" and elecion == "spock":
    print("ganaste")
elif elecion_PC == "tijeras" and elecion == "lagarto":
    print("perdistes")
    #spock vs#
elif elecion_PC == "spock" and elecion == "lagarto":
    print("ganaste")
elif elecion_PC == "spock" and elecion == "tijeras":
    print("perdistes")
elif elecion_PC == "spock" and elecion == "papel":
    print("ganaste")
elif elecion_PC == "spock" and elecion == "piedra":
    print("perdistes")
    #lagarto vs
elif elecion_PC == "lagarto" and elecion == "piedra":
    print("ganaste")
elif elecion_PC == "lagarto" and elecion == "spock":
    print("perdistes")
elif elecion_PC == "lagarto" and elecion == "tijeras":
    print("ganaste")
elif elecion_PC == "lagarto" and elecion == "papel":
    print("perdistes")

