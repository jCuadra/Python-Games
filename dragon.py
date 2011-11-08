#-------------
# Name:        Dragon Realm from the PyGame tutorial
# Purpose:      Learning to program
#
# Author:      Liam P Boyle
#
# Created:     06/05/2011
# Copyright:   (c) Liam P Boyle 2011
# Licence:     <>
#-------------
#!/usr/bin/env python
#-------------

## Import Statements

import random
import time
##-------------

## Global Variable Initializatins and Function definitions

def displayIntro():
    print ("You are on a planet full of dragons.  In front of you,")
    print ("you see two caves.  In one cave the dragon is friendly")
    print ("and will share his treasure with you.  The other dragon")
    print ("is greedy and hungry, and will eat you on sight.\n")

def chooseCave():
    cave = ""
    while cave != "1" and cave != "2":
        print ("Which cave will you go into (1 or 2)")
        cave = input()

    return cave

def checkCave(chosenCave):
    print ("You approach the cave...")
    time.sleep(2)
    print ("It is dark and spooky...")
    time.sleep(2)
    print("A large dragon jumps out in front of you!  He opens his jaws and...")
    print()
    time.sleep(2)
    friendlyCave = random.randint(1,2)
    if chosenCave == str(friendlyCave):
        print("He gives you his treasure.")
    else:
        print("He gobbles you up!")
#-------------

## Main Program Logic
def main():
    playAgain = "yes"
    while playAgain == "yes" or playAgain == "y":
        displayIntro()
        caveNumber = chooseCave()
        checkCave(caveNumber)
        prompt = "Do you want to play again: yes/no?"
        playAgain = input(prompt)

if __name__ == '__main__':
    main()
##End
#-------------