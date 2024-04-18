import random

# asks for player name
player_1_name = input("This is Sam's Tic Tac Toe game. Welcome, erm, what was your name again? ")
# prints player name back and welcomes them.
print(f"Welcome, {player_1_name}, I hope you enjoy!")

# possible choices for grid array
possibleNumbers = [1,2,3,4,5,6,7,8,9]

# makes two dimensionsal array
gameBoard = [[1,2,3], 
             [4,5,6], 
             [7,8,9]]

# rows and columns variables
rows = 3

columns = 3

# prints gameboard when called
def printGameBoard():
    for x in range(rows):
        print("\n+---+---+---+")
        print("|", end='')
        for y in range(columns):
            print("", gameBoard[x][y], end=' |')
    print("\n+---+---+---+")

def modifyArray(num, turn):
    # corrects user input to match that computers count from 0 not from 1.
    num -= 1
    # addresses each possible number input
    if(num == 0):
        # modifies game board with an if statement. 
        gameBoard[0][0] = turn
    elif(num == 1):
        gameBoard[0][1] = turn
    elif(num == 2):
        gameBoard[0][2] = turn
    elif(num == 3):
        gameBoard[1][0] = turn
    elif(num == 4):
        gameBoard[1][1] = turn
    elif(num == 5):
        gameBoard[1][2] = turn
    elif(num == 6):
        gameBoard[2][0] = turn
    elif(num == 7):
        gameBoard[2][1] = turn
    elif(num == 8):
        gameBoard[2][2] = turn
    else:
        return 'N'

def check_for_winner(gameBoard):
    # x axis

    if(gameBoard[0][0] == 'X' and gameBoard[0][1] == 'X' and gameBoard[0][2] == 'X'):
        return 'X'
    elif(gameBoard[0][0] == 'O' and gameBoard[0][1] == 'O' and gameBoard[0][2] == 'O'):
        return 'O'
    elif(gameBoard[1][0] == 'X' and gameBoard[1][1] == 'X' and gameBoard[1][2] == 'X'):
        return 'X'
    elif(gameBoard[1][0] == 'O' and gameBoard[1][1] == 'O' and gameBoard[1][2] == 'O'):
        return 'O'
    elif(gameBoard[2][0] == 'X' and gameBoard[2][1] == 'X' and gameBoard[2][2] == 'X'):
        return 'X'
    # y axis

    elif(gameBoard[0][0] == 'X' and gameBoard[1][0] == 'X' and gameBoard[2][0] == 'X'):
        return 'X'
    elif(gameBoard[0][0] == 'O' and gameBoard[1][0] == 'O' and gameBoard[2][0] == 'O'):
        return 'O'
    elif(gameBoard[0][1] == 'X' and gameBoard[1][1] == 'X' and gameBoard[2][1] == 'X'):
        return 'X'
    elif(gameBoard[0][1] == 'O' and gameBoard[1][1] == 'O' and gameBoard[2][1] == 'O'):
        return 'O'
    elif(gameBoard[0][2] == 'X' and gameBoard[1][2] == 'X' and gameBoard[2][2] == 'X'):
        return 'X'
    elif(gameBoard[0][2] == 'O' and gameBoard[1][2] == 'O' and gameBoard[2][2] == 'O'):
        return 'O'
    # diagonals

    elif(gameBoard[0][0] == 'X' and gameBoard[1][1] == 'X' and gameBoard[2][2] == 'X'):
        return 'X'
    elif(gameBoard[0][0] == 'O' and gameBoard[1][1] == 'O' and gameBoard[2][2] == 'O'):
        return 'O'
    elif(gameBoard[0][2] == 'X' and gameBoard[1][1] == 'X' and gameBoard[2][0] == 'X'):
        return 'X'
    elif(gameBoard[0][2] == 'O' and gameBoard[1][1] == 'O' and gameBoard[2][0] == 'O'):
        return 'O'

leaveLoop = False
turnCounter = 0

while(leaveLoop == False):
    # player turn
    if(turnCounter % 2 == 0):
        printGameBoard()
        numberPicked = int(input("\n Choose a number [1-9]: "))
        if(numberPicked >= 1 or numberPicked <= 9):
            modifyArray(numberPicked, 'X')
            possibleNumbers.remove(numberPicked)
        else: print('Invalid input, try again.')
        turnCounter += 1
        while turnCounter >= 4:
            game_state = check_for_winner(gameBoard)
            if game_state == 'X':
                print('X has won!')
                exit
            elif game_state == 'O':
                print('O has won. :(')
                exit
            break
                
    # computer turn
    else:
        while(True):
            # cpu chooses random number
            cpuChoice = random.choice(possibleNumbers)
            # let's player know what cpu choice was
            print("\nCpu choice: ", cpuChoice)
            if(cpuChoice in possibleNumbers):
                modifyArray(cpuChoice, 'O')
                possibleNumbers.remove(cpuChoice)
                turnCounter += 1
                break