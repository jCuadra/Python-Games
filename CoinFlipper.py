#-------------
# Name:        CoinFlipper based off example found in PyGame Tutorial
# Purpose:      why the heck not
#
# Author:      Liam P Boyle  ##prog needs finished
#
# Created:     06/05/2011
# Copyright:   (c) Liam P Boyle 2011
# Licence:     <>
#-------------
#!/usr/bin/env python

## Import statements
import random

def main():
    print("I will flip a coin 1000 times.")
    print("Guess how many times it will come up heads.")
    print("press ENTER to begin\n")
    input()
    flips = 0
    heads = 0
    while flips < 1000:
        if random.randint(0,1) == 1:
            heads = heads + 1
        flips = flips + 1
        if flips == 100:
            print("At 100 hundred ")

if __name__ == '__main__':
    main()
