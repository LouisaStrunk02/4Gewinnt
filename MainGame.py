from Player import Player
from Board import Board

class MainGame:
    def __init__(self):
        self.player1 = Player()
        self.player2 = Player()
        self.board = Board()

    def getUserName(self, salutation: str) -> str:
         while True:
            userName = input(f"{salutation}: Please enter your name: ")

            inputIsValid = userName.isalpha() and len(userName) > 0
            if inputIsValid:
                return userName
            else:
                print(f"Your input '{userName}' is invalid. Please try again")

    def prepareGame(self) -> None:
        self.player1.name = self.getUserName("Player 1")
        self.player1.symbol = "x"
        self.player2.name = self.getUserName("Player 2")
        self.player2.symbol = "o"

