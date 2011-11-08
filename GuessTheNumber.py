#-------------
# Name:        Guess The Number from PyGame Tutorial
# Purpose:      Learning to program
#
# Author:      Liam P Boyle
#
# Created:     05/05/2011
# Copyright:   (c) Liam P. Boyle 2011
# Licence:     <your licence>
#-------------
#!/usr/bin/env python

def main():
    ## This is a guess the Number game

    import random

    guessesTaken = 0

    print ("Hello, what is your name?")
    myName = input()

    number = random.randint(1,20)
    print ("Well, " + myName + ", I am thinking of a number between 1 and 20.")
    while guessesTaken < 6:
        print ("Take a guess")
        guess = input()
        guess = int(guess)
        guessesTaken = guessesTaken + 1
        if guess < number:
            print("Your guess is too low")
        if guess > number:
            print("Your guess is too high")
        if guess == number:
            break
    if guess == number:
        guessesTaken = str(guessesTaken)
        print ("Good Job " + myName + "! You guessed my number in " + guessesTaken + " tries.")
    if guess != number:
        number = str(number)
        print ("No.  The number I was thinking of was " + number)

if __name__ == '__main__':
    main()
## End
