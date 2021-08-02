import minesweeper as ms

def initBot():
    difficulty = int(input("Enter Minesweeper difficulty (0 or 1): "))
    if difficulty == 0:
        ms.playGame(9,10)
    if difficulty == 1:
        ms.playGame(16, 40)
    