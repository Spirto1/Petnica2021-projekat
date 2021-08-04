import random
import numpy as np

def setBoard(boardWidth, boardHeight, numMines):
    board = d = np.zeros((boardHeight,boardWidth))
    #Postavljanje mina u tablu
    mineProbability = 1000 * (numMines/(boardWidth * boardHeight))
    for i in range(boardHeight):
        for j in range(boardWidth):
            randomMine = random.randint(1,1000)
            if randomMine < mineProbability and numMines > 0:
                board[i][j] = -1
                numMines -= 1
            else:
                if numMines <= 0:
                    break
    print(board)               
    
setBoard(9,9,10)