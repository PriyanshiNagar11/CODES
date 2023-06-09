board = ["_", "_", "_",
         "_", "_", "_",
         "_", "_", "_"]

currentPlayer ="X"
winner = None
gameRunning = True

# Printing the game board 

def printBoard(board):
    print(board[0] + " | " + board[1] + " | " + board[2])
    print("----------")
    print(board[3] + " | " + board[4] + " | " + board[5]) 
    print("----------")
    print(board[6] + " | " + board[7] + " | " + board[8])
    

# Take player input 

def PlayerInput(board):
    inp = int(input("Enter a number 1-9:"))
    if inp >= 1 and inp <= 9 and board[inp-1] == "_": 
        board[inp-1] = currentPlayer
    else:
        print("Player is already in that spot!")    


#Check for win or tie 

def checkHorizontal(board):
    global winner
    if board[0] == board[1] == board[2] and board[0] != "-":
        winner = board[0]
        return True
    elif board[3] == board[4] == board[5] and board[3] != "_":
        winner = board[3]
        return True
    elif board[6] == board[7] == board[8] and board[6] != "_":
        winner = board[6]
        return True
    
def checkVerticl(board):
    global winner
    if board[0] == board[3] == board[6] and board[0] != "_":
        winner = board[0]
        return True
    elif board[1] == board[4] == board[7] and board[1] != "_":
        winner = board[1]
        return True 
    elif board[2] == board[5] == board[8] and board[2] != "_":
        winner = board[2]
        return True
    
def checkDiagnol(board):
    global winner
    if board[0] == board[4] == board[8] and board[0] != "_":
        winner = board[0]
        return True
    elif board[2] == board[4] == board[6] and board[2] !="_":
        winner = board[2]
        return True
    
def checkTie(board):
    global gameRunning
    if "_" not in board:
      printBoard(board)
      print ("It is a tie!")
      gameRunning = False

def checkWin():
    global gameRunning
    if checkHorizontal(board) or checkVerticl(board) or checkDiagnol(board):
        printBoard(board)
        print(f"The winner is {winner}")
        gameRunning = False
        

    
#Switch the player

def switchPlayer():
    global currentPlayer
    if currentPlayer == "X":
        currentPlayer = "O"
    else:
        currentPlayer = "X"


#Check for win or tie again 


while gameRunning:
    printBoard(board)
    PlayerInput(board)
    checkWin()
    if winner != None:
      break
    checkTie(board)
    switchPlayer()

