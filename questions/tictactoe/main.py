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
        pass

    def place_token(self, x: int, y: int) -> List[list]:
        """
        This function checks whether a move is valid and places a token
        on the board if it is otherwise it requests the user to
        re-place in another location
        """
        pass

    def play_game(self, x: int, y: int):
        pass

