#coding:utf-8
import os
import sys

def clear():
    try:
        if os.name == "nt":
            os.system("cls")
        else:
            os.system("clear")
    except:
        pass

def exit():
    print("\n\r[+] Bye...\n\r")
    sys.exit()

def packageInstaller():
    try:
        os.system("sudo pip install colorama")
        os.system("sudo pip3 install colorama")
        print("\n\r[+] Colorama a été installé avec succès!\n\r")
    except:
        print("/!\ Une erreur s'est produit lors de l'installation de colorama!")

def main():
    clear()
    packageInstaller()

try:
    main()
except KeyboardInterrupt:
    exit()
finally:
    exit()

