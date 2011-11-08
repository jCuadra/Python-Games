#-------------------------------------------------------------------------------
# Name:        Tic Tac Toe
# Purpose:      practice prog from PyGame tutorial
#
# Author:      Liam P. Boyle
#
# Created:     05/18/2011
# Copyright:   (c) Liam P. Boyle 2011
# Licence:     <>
#-------------------------------------------------------------------------------
#!/usr/bin/env python

# Import statements
import random
#-------------------------------------------------------------------------------

def drawBoard(board):
    # This function prints out the board that it was passed.
    # "board" is a list of 10 strings representing the board (ignore index 0)
    print(' | |')
    print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9])
    print(' | |')
    print('-----------')
    print(' | |')
    print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6])
    print(' | |')
    print('-----------')
    print(' | |')
    print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3])
    print(' | |')

#-------------------------------------------------------------------------------

def inputPlayerLetter():
    # lets the player type which letter they wish to play.
    # Returns a list with the player's letter as the 1st item & the 'puter's 2nd
    letter = ""
    while not (letter == "X" or letter=="O"):
        print("Do you want to play X or O")
        letter=input().upper()
    # the 1st element in the tuple is player's lett, the 2nd is 'puter's
    if letter=="X":
        return ["X", "O"]
    else:
        return ["O", "X"]

#-------------------------------------------------------------------------------

def whoGoesFirst():
    # randomly choose the player who goes first.
    if random.randint(0,1) == 0:
        return "computer"
    else:
        return "player"

#-------------------------------------------------------------------------------

def playAgain():
    print ("Do you want to play again yes/no?")
    return input().lower().startswith('y')

#-------------------------------------------------------------------------------

def makeMove(board, letter, move):
    board[move] = letter

#-------------------------------------------------------------------------------

def isWinner(board, letter):
    # Given a board & player's letter, this funct returns True if player has won
    return ((board[7]==letter and board[8]==letter and board[9]==letter) or
    (board[4] == letter and board[5] == letter and board[6] == letter) or
    (board[1] == letter and board[2] == letter and board[3] == letter) or
    (board[7] == letter and board[4] == letter and board[1] == letter) or
    (board[8] == letter and board[5] == letter and board[2] == letter) or
    (board[9] == letter and board[6] == letter and board[3] == letter) or
    (board[7] == letter and board[5] == letter and board[3] == letter) or
    (board[9] == letter and board[5] == letter and board[1] == letter))

#-------------------------------------------------------------------------------

def getBoardCopy(board):
    # Make a duplicate of the board list and return the duplicate
    dupeBoard = []
    for i in board:
        dupeBoard.append(i)
    return dupeBoard

#-------------------------------------------------------------------------------

def isSpaceFree(board, move):
    # return true if the passed move is free on the passed board
    return board[move] == " "

#-------------------------------------------------------------------------------

def getPlayerMove(board):
    # Let the player type in his move
    move = " "
    while move not in "1 2 3 4 5 6 7 8 9".split() or not isSpaceFree(board, int(move)):
        print("What is your move? (1-9)")
        move = input()
    return int(move)

#-------------------------------------------------------------------------------

def chooseRandomMoveFromList(board, movesList):
    # returns a valid move from the passed list on the passed board
    # returns None if there is no valid move
    possibleMoves = []
    for i in movesList:
        if isSpaceFree(board, i):
            possibleMoves.append(i)
    if len(possibleMoves) != 0:
        return random.choice(possibleMoves)
    else:
        return None

#-------------------------------------------------------------------------------

def getComputerMove(board, computerLetter):
    # given a board & the puter's letter, determine where to move & return move
    if computerLetter == "X":
        playerLetter = "O"
    else:
        playerLetter = "X"

    # here is AI algorithm for game
    # 1st, check for win on next move
    for i in range(1, 10):
        copy = getBoardCopy(board)
        if isSpaceFree(copy, i):
            makeMove(copy, computerLetter, i)
            if isWinner(copy, computerLetter):
                return i
    # check if player's next move wins & blocks him
    for i in range(1, 10):
        copy = getBoardCopy(board)
        if isSpaceFree(copy, i):
            makeMove(copy, playerLetter, i)
            if isWinner(copy, playerLetter):
                return i
    # try to take one of the corners, if they are free
    move = chooseRandomMoveFromList(board, [1, 3, 7, 9])
    if move != None:
        return move
    # try to take the center if it is free
    if isSpaceFree(board, 5):
        return 5
    # move on one of the sides
    return chooseRandomMoveFromList(board, [2, 4, 6, 8])

#-------------------------------------------------------------------------------

def isBoardFull(board):
    #return True if every space on board has been taken, othewrwise return False
    for i in range(1, 10):
        if isSpaceFree(board, i):
            return False
    return True

#-------------------------------------------------------------------------------

print("Welcome to Tic Tac Toe")
while True:
    # Reset the board
    theBoard = [" "]*10
    playerLetter, computerLetter = inputPlayerLetter()
    turn = whoGoesFirst()
    print ("The " + turn + ' will go first.')
    gameIsPlaying = True
    while gameIsPlaying:
        if turn == "player":
            # Player's turn
            drawBoard(theBoard)
            move = getPlayerMove(theBoard)
            makeMove(theBoard, playerLetter, move)
            if isWinner(theBoard, playerLetter):
                drawBoard(theBoard)
                print("Huzzah!  You have won the game!")
                gameIsPlaying = False
            else:
                if isBoardFull(theBoard):
                    drawBoard(theBoard)
                    print("The game is a tie!")
                    break
                else:
                    turn = "computer"
        else:
            # Computer's turn
            move = getComputerMove(theBoard, computerLetter)
            makeMove(theBoard, computerLetter, move)
            if isWinner(theBoard, computerLetter):
                drawBoard(theBoard)
                print("The computer has beaten you! You lose!")
                gameIsPlaying = False
            else:
                if isBoardFull(theBoard):
                    drawBoard(theBoard)
                    print("The game is a tie!")
                    break
                else:
                    turn = "player"
    if not playAgain():
        break
    
