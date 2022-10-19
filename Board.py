class Board:
    def __init__(self):
        self.placeholder = "_"
        self.board = self.create_board()

    def create_board(self) -> list[list[str]]:
        empty_board = [
            [self.placeholder] * 7,
            [self.placeholder] * 7,
            [self.placeholder] * 7,
            [self.placeholder] * 7,
            [self.placeholder] * 7,
            [self.placeholder] * 7,
            ["1", "2", "3", "4", "5", "6", "7"]
        ]

        return empty_board

    def show_board(self) -> None:
        for line in self.board:
            for element in line:
                print("|" + element, end="")
            print("|")

    def is_valid_turn(self, column: int) -> bool:
        column -= 1

        for index, _ in enumerate(self.board):
            if self.board[index][column] != self.placeholder:
                if self.board[index - 1][column] == self.placeholder:
                    return True

        return False

    def add_coin_to_board(self, column: int, player_symbol: str) -> None:
        column -= 1

        for index, _ in enumerate(self.board):
            if self.board[index][column] != self.placeholder:
                if self.board[index - 1][column] == self.placeholder:
                    self.board[index - 1][column] = player_symbol
