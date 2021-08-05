import minesweeper as ms

def initBot():
    difficulty = int(input("Enter Minesweeper difficulty (0 or 1): "))
    if difficulty == 0:
        playGame(9,10)
    if difficulty == 1:
        playGame(16, 40)

numWin = 0
numLoss = 0
numPlay = 0

#play game        
def playGame(boardSize, numMines):
    global numWin, numLoss
    #boardSize = int(input("Choose the Width of the board: "))
    #numMines = int(input("Choose the number of mines: "))
    gameOver = False
    winner = False
    Board = ms.boardClass(boardSize, numMines)
    x = 0
    y = 0
    Board.makeMove(x, y)
    for i in range(boardSize +1):
        x += 1
        for j in range(boardSize +1):
            y +=1
    
    while not gameOver:
        #print(Board)
        
        Board.makeMove(x, y)
        gameOver = Board.hitMine(x, y)
        if Board.isWinner() and gameOver == False:
            gameOver = True
            winner = True

    print(Board)
    if winner:
        print("Congratulations, You Win!")
        numWin += 1
        endGame(numWin, numLoss)
    else:
        print("You hit a mine, Game Over!")
        numLoss += 1
        endGame(numWin, numLoss)
        
def endGame(numWin, numLoss):
    global numPlay
    f = open("result.txt", "w")
    f.write("\nWins: " + str(numWin))
    f.write("\nLosses: " + str(numLoss))
    f.write("\nTotal: " + str(numWin + numLoss))
    f.close()
    if numPlay != 10:
        playGame()
        numPlay += 1

        
playGame()
initBot()   