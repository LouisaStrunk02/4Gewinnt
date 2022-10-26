class Board:
    def __init__(self):
        self.board = self.create_board()

    def create_board(self) -> list[list[str]]:
        placeholder = "_"

        empty_board = [
            [placeholder] * 7,
            [placeholder] * 7,
            [placeholder] * 7,
            [placeholder] * 7,
            [placeholder] * 7,
            [placeholder] * 7,
            ["1", "2", "3", "4", "5", "6", "7"]
        ]

        return empty_board

    def show_board(self) -> None:
        for line in self.board:
            for element in line:
                print("|" + element, end="")
            print("|")
