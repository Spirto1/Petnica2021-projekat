import minesweepersim as ms

def initBot():
    difficulty = int(input("Enter Minesweeper difficulty (0,1 or 2): "))
    if difficulty == 0:
        ms.setBoard(9,9,10)
    if difficulty == 1:
        ms.setBoard(16,16,40)
    if difficulty == 1:
        ms.setBoard(16,30,29)

numWin = 0
numLoss = 0
numPlay = 0

initBot()   