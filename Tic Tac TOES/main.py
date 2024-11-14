#Matthew McKinley Tic Tac Toe

import random

#board
computer = random.randint(1,10)
row1 = [" 1 | 2 | 3 "]
row2 = [" 4 | 5 | 6 "]
row3 = [" 7 | 8 | 9 "]
board = [row1, row2,row3]
for row in board:
    print(row)

playerspot = int(input("What place would you like to go? (1-9)"))

for row in board:
    for spot in row:
        if spot == playerspot:
            row = row.replace(spot, "X")
        
for row in board:
    print(row)