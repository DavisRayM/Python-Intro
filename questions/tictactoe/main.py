"""
In this section will cover creating a basic tic tac toe game
Prerequiste knowledge:
    - Classes in Python:
        - https://docs.python.org/3/tutorial/classes.html
        - https://www.w3schools.com/python/python_classes.asp
"""
from typing import List


class TicTacToe:
    def __init__(self):
        self._build_intial_board()
        self.current_round = 0
        self.position_map = {1:(0,0),2:(0,1),3:(0,2),4:(1,0),5:(1,1),6:(1,2),7:(2,0),8:(2,1),9:(2,2)}


    def _build_initial_board(self):

        self.board = [["-","-","-"],["-","-","-"],["-","-","-"]]

    def print_board(self):
        for row in self.board:
            print(" | ".join(row))
        pass

    def _validate_move(self,cell_no):
        #checks if its a valid number
        if cell_no > 9 or cell_no<1:
            raise ValueError("Please enter a valid number between 1 to 9")
        x, y = self.position_map.get(cell_no)
        #checks if cell is occupied
        if self.board[x][y] != "-":
            raise ValueError(f"Cell is already occupied by player {self.board[x][y]}")

    def _get_current_user(self):
        if self.current_round %2 == 0 :
            return'o'
        else:
            return 'x'
    def place_token(self,cell_no):
        self._validate_move(cell_no)
        x,y =self.position_map.get(cell_no)
        current_player = self._get_current_user()
        self.board[x][y] = current_player
        self.print_board()

    def check_win(self):
        if self.board[0][0] == self.board[0][1] == self.board[0][2] and self.board[0][0] != "-" :
                return True
        elif self.board[1][0] == self.board[1][1] == self.board[1][2] and self.board[1][0] != "-" :
                return True
        elif self.board[2][0] == self.board[2][1] == self.board[2][2] and self.board[2][0] != "-":
                return True
        elif self.board[0][0] == self.board[1][0] == self.board[2][0] and self.board[0][0] != "-":
                return True
        elif self.board[0][1] == self.board[1][1] == self.board[2][1] and self.board[0][1] != "-":
            return True
        elif self.board[0][2] == self.board[1][2] == self.board[2][2] and self.board[0][2] != "-":
                return True
        elif self.board[0][0] == self.board[1][1] == self.board[2][2] and self.board[0][0] != "-":
                return True
        elif self.board[0][2] == self.board[1][1] == self.board[2][2] and self.board[0][2] != "-":
                return True
        else:
            return False

    def play_game(self):
        game_ongoing = True
        while game_ongoing:
            self.current_round += 1
            current_player = self._get_current_user()
            try:
                user_input= input(f"Player{current_player}, Enter a number between 1 to 9:")
                self.place_token(int(user_input))
            except ValueError as e:
                print(e)
                user_input = input(f"Player{current_player}, Enter a number between 1 to 9: ")
                self.place_token(int(user_input))


                if self.check_win():
                    print(f"Player {current_player} wins! Game Over")
                    game_ongoing = False

if __name__ == "__main__":
    TicTacToe().play_game()
