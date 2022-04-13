"""
In this section will cover creating a basic tic tac toe game
Prerequiste knowledge:
    - Classes in Python:
        - https://docs.python.org/3/tutorial/classes.html
        - https://www.w3schools.com/python/python_classes.asp
"""
from typing import List


class TicTacToe:
    player_a = "X"
    player_b = "O"


    def __init__(self):
        # self.position_map = {1:(0,0),2:(0,1),3:(0,2),4:(1,0),5:(1,1),6:(1,2),7:(2,0),8:(2,1),9:(2,2)}
        self.board = []
    def build_initial_board(self) -> List[list]:
        """
        This function is used to generate the initial tic
        tac toe board which is a 3 * 3 board
        -------------
        |   |   |   |
        -------------
        |   |   |   |
        -------------
        |   |   |   |
        -------------
        """

        self.board = [["-","-","-"],["-","-","-"],["-","-","-"]]
        print(self.board)

    def print_board(self):
        for row in self.board:
            print(" | ".join(row))
        pass

    def place_token(self):
        if user_input > 9 or user_input  < 1 or type(user_input) != int:
            print("Please enter a valid number betweeb 1 and 9 ")
        #import pdb; pdb.set_trace()

        self.board[0][0] == 0
        self.board[0][1] == 1
        self.board[0][2] == 2
        self.board[1][0] == 3
        self.board[1][1] == 4
        self.board[0][2] == 5
        self.board[2][0] == 6
        self.board[2][1] == 7
        self.board[2][2] == 8
         # x,y = self.position_map[user_input]#same way as indexing

        # if self.board[x][y] == '-':
        #     self.board[x][y] = 'x'
            # if x is has played now its 'o' turn.
    pass

    def swap_user(self):
        for row in self.board:
            for i in row:
                    if self.board[0][0] == '-':
                        self.board[0][0] = 'player_a'

                    elif self.board[0][2] == '-':
                        self.board[0][2] = 'player_a'

                    elif self.board[1][1] == '-':
                        self.board[1][1] = 'player_a'

                    elif self.board[2][0] == '-':
                        self.board[2][0] = 'player_a'

                    elif self.board[2][2] == '-':
                        self.board[2][2] = 'player_a'

                    elif self.board[0][1] == '-':
                        self.board[0][1] = 'player_b'

                    elif self.board[1][0] == '-':
                        self.board[1][0] = 'player_b'

                    elif self.board[1][2] == '-':
                        self.board[1][2] = 'player_b'

                    elif self.board[2][1] == '-':
                        self.board[2][1] = 'player_b'
                    else:
                        print("Invalid choice")


    def winner(self):
        # checking winner
        if self.board[0][0] == self.board[0][1] == self.board[0][2] != "-" :
                print("Game over!")
        elif self.board[1][0] == self.board[1][1] == self.board[1][2] != "-" :
                print("Game over!")
        elif self.board[2][0] == self.board[2][1] == self.board[2][2] != "-":
                print("Game over!")
        elif self.board[0][0] == self.board[1][0] == self.board[2][0] != "-":
                print("Game over!")
        elif self.board[0][1] == self.board[1][1] == self.board[2][1] != "-":
            print("Game over!")
        elif self.board[0][2] == self.board[1][2] == self.board[2][2] != "-":
                print("Game over!")
        elif self.board[0][0] == self.board[1][1] == self.board[2][2] != "-":
                print("Game over!")
        elif self.board[0][2] == self.board[1][1] == self.board[2][2] != "-":
                print("Game over!")
        else:
            print("Try again")

    def play_game(self):

        pass

if __name__ == "__main__":
    user_input = int(input("Enter a number between 1 to 9 "))
    user_input -= 1
    board = TicTacToe()
    print(board.build_initial_board())
    print(board.print_board())
    print(board.place_token())

