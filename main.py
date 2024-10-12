from time import sleep
from random import randint
import os
import game

print("Welcome to Escape the Forest")
sleep(5)
game.clearTerminal()

print("You can:\n")
print(" ----------------\n",
      "|1. Play       |\n",
      "----------------\n",
      "|2. See Credits|\n"
      " ----------------\n")
choice1 = input("Choose:")

if choice1 == "1":
    sleep(1)
    game.clearTerminal()
    game.intro()