from Player import Player
from Board import Board

class MainGame:
    def __init__(self):
        self.player1: Player = Player()
        self.player2: Player = Player()
        self.board: Board = Board()
        self.turn_number = 0

    def get_user_name(self, salutation: str) -> str:
         while True:
            user_name: str = input(f"{salutation}: Please enter your name: ")

            input_is_valid: bool = user_name.isalpha() and len(user_name) > 0
            if input_is_valid:
                return user_name
            else:
                print(f"Your input " + user_name + " is invalid. Please try again")

    def prepare_game(self) -> None:
        self.player1.name = self.get_user_name("Player 1")
        self.player1.symbol = "x"
        self.player2.name = self.get_user_name("Player 2")
        self.player2.symbol = "o"

    def turn(self, player: Player) -> None:
        self.board.show_board()

        while True:
            column: int = self.get_column_input(player.name)
            is_valid_turn: bool = self.board.is_valid_turn(column)

            if is_valid_turn:
                self.board.add_coin_to_board(column, player.symbol)

                return
            else:
                print("You can't put a coin in column " + str(column) + ". Try again.")

    def get_column_input(self, player_name: str) -> int:
        while True:
            try:
                column_input = int(input(player_name + ", select a column to put your coin: "))

                input_is_valid = 1 <= column_input <= 7
                if input_is_valid:
                    return column_input
                else:
                    print("Invalid input. Please try again")
            except ValueError:
                print("Please enter an integer.")

    def round(self) -> None:
        self.turn_number += 1
        if self.turn_number % 2 != 0:
            self.turn(self.player1)
        else:
            self.turn(self.player2)

    def play(self) -> None:
        while True:
            self.round()
