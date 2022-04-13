board = [
    ['-','-','-'],
    ['-','-','-'],
    ['-','-','-']
]

user = True  #when true it refers to x
def print_board(board):
    for row in board:
        for slot in row:
            print(f"{slot} ", end ="")
        print()
print_board(board)

def quit(user_input):
    if user_input == "q": 
        print("Thanks for playing ")
        return True
    else: return False

def check_input(user_input):
    #check if its a number
    if not isnum(user_input): return False
    user_input = int(user_input)
    
    #check if its 1 - 9
    if not bounds(user_input):return False
    else:
        return True

def bounds(user_input):
    if user_input > 9 or user_input < 1:
        print ("This number is out of bounds")
        return False 
    else:
        return True
    
def isnum(user_input):
    if not user_input.isnumeric():
        print("not a valid number")
        return False
    else:
         return True

def istaken(coords, board):
    row = coords[0]
    col = coords[1]
    if board[row] [col] != "-":
        print("This position is already taken")
        return True
    else:
        return False

def coordinates(user_input):
    row = int(user_input/3)
    col = user_input
    if col > 2: col = int(col % 3)
    return (row,col)
    
def add_to_board(coords, board,active_user):
    row = coords[0]
    col = coords[1]
    board[row][col] = active_user

def current_user(user):
    if user: return "x"
    else:
        return "o"

while True:
    active_user = current_user(user)
    print_board(board)
    user_input = input("enter a number fron 1 through 9 or enter \"q\" to quit ")
    if quit(user_input):break
    if not check_input(user_input):
        print("Please try again.")
        continue
    user_input = int(user_input) -1
    coords = coordinates(user_input)
    if istaken (coords,board):
        print("please try again")
        continue
    add_to_board(coords,board,active_user)
    user = not user