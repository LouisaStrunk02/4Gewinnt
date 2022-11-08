from asyncio import constants
from Player import Player
from Board import Board
from StatusValidator import StatusValidator

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
                player_is_winner = StatusValidator.is_win(self.board, player)
                if player_is_winner:
                    return player
                break
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

    def round(self) -> None or Player:
        anzahl_felder: constants = 42
        winner: Player
        self.turn_number += 1

        if self.turn_number > anzahl_felder:
            return Player()

        if self.turn_number % 2 != 0:
            winner = self.turn(self.player1)
        else:
            winner = self.turn(self.player2)

        if winner is not None:
            return winner

    def play(self) -> None:
        winner: Player

        while True:
            winner = self.round()

            if winner is not None:
                break

        self.board.show_board()

        if winner.name == "":
            print("It's a tie!")
        else:
            print(winner.name + " wins the game! Congratulations")
