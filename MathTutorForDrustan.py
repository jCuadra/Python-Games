#-------------------------------------------------------------------------------
# Name:        Math Tutor pre-K
# Purpose:      help children learn addition and subtraction
#
# Author:      Liam P. Boyle
#
# Created:     06/05/2011
# Copyright:   (c) Liam P. Boyle 2011
# Licence:     <freeware w/ author attribution>
#-------------------------------------------------------------------------------
#!/usr/bin/env python

##Import Statements
import random
#-------------------------------------------------------------------------------

def greeting():
    print ("What is your name?\n")
    plyrName = input()
    print ("Hello, " + plyrName + ", would you like to add and subtract?\n")
    print ("Enter y for yes or n for no\n")
    playAns = input()
    return playAns

def selectMode():
    ModeNum = random.randint(0,1)
    return ModeNum

def additionPractice():
    tries = 1
    num1 = random.randint(0,5)
    num2 = random.randint(0,5)
    answer = num1 + num2
    while tries <= 3:
        print ("What does ", num1, " plus", num2, "equal?\n")
        plyrAnswer = int(input())
        if plyrAnswer == answer:
            break
        else:
            print("That isn't correct.  Please try again\n")
        tries = tries +1
    if plyrAnswer == answer:
        print("Great Job!!!")
    else:
        print("The correct answer is:  ", answer)

def subtractionPractice():
    tries = 1
    num1 = random.randint(0,5)
    num2 = random.randint(0,5)
    if num1 < num2:
        num1, num2 = num2, num1
    answer = num1 - num2
    while tries <= 3:
        print ("What does ", num1, " minus", num2, "equal?\n")
        plyrAnswer = int(input())
        if plyrAnswer == answer:
            break
        else:
            print("That isn't correct.  Please try again\n")
        tries = tries +1
    if plyrAnswer == answer:
        print("Great Job!!!")
    else:
        print("The correct answer is:  ", answer)

def main():
    playAns = greeting()
    while playAns == "y":
        switch = selectMode()
        if switch == 0:
            additionPractice()
        else:
            subtractionPractice()
        print ("Do you want to play some more?\n")
        print ("Enter y for yes or n for no")
        playAns = input()

if __name__ == '__main__':
    main()
## End
