from time import sleep
import colorama
import os
import map

def clearTerminal():
    os.system('cls' if os.name == 'nt' else "printf '\033c'")

def intro():
    print("You find yourself lost in a mysterious forest.")

def displayMap():
    print(map.map1)