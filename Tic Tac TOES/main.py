#Matthew McKinley Tic Tac Toe

import random

#board
wrongspot = True
row1 = ["1", "2", "3"]
row2 = ["4", "5", "6"]
row3 = ["7", "8", "9"]
board = [row1, row2,row3]

for row in board:
    print(row)

def check():
    #tie

    #xrow
    #xcolumn
    #xdiag
    #orow
    #ocolumn
    #odiag

while True:
    wrongspot = True
    playerspot = input("What place would you like to go? (1-9)")
    for rowindex, row in enumerate(board):
        for spotindex, spot in enumerate(row):
            if spot == playerspot:
                board[rowindex][spotindex] = "X"
    check()
    
    for row in board:
        print(row)
    print("")
    while wrongspot == True:
        computer = random.randint(1,10)
        for rowindex, row in enumerate(board):
            for spotindex, spot in enumerate(row):
                if spot == str(computer):
                    board[rowindex][spotindex] = "O"
                    wrongspot = False
    check()
    for row in board:
        print(row)
