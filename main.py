from time import sleep
from random import randint
import os

map1 = [["Forest", "Forest", "Forest", "Forest", "Exit"],
        ["Cabin", "Forest", "Forest", "Forest", "Forest"],
        ["Forest", "Forest", "Forest", "Forest", "Forest"],
        ["Mountain", "Mountain", "Forest", "Forest", "Forest"],
        ["Mountain", "Mountain", "Forest", "Forest", "Forest"]]

print("Welcome to Escape the Forest")
os.system('cls' if os.name == 'nt' else "printf '\033c'")
