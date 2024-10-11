from time import sleep
from random import randint
import os

map1 = [["Forest", "Forest", "Forest", "Forest", "Exit"],
        ["Cabin", "Forest", "Forest", "Forest", "Forest"],
        ["Forest", "Forest", "Forest", "Forest", "Forest"],
        ["Mountain", "Mountain", "Forest", "Forest", "Forest"],
        ["Mountain", "Mountain", "Forest", "Forest", "Forest"]]

def clearTerminal():
    os.system('cls' if os.name == 'nt' else "printf '\033c'")

print("Welcome to Escape the Forest")
sleep(5)
clearTerminal()

print("You can:\n")
print(" ----------------\n",
      "|1. Play       |\n",
      "----------------\n",
      "|2. See Credits|\n"
      " ----------------\n")