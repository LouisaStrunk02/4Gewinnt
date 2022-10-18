class Board:
    def __init__(self):
        self.board = self.createBoard()

    def createBoard(self) -> list[list[str]]:
        placeholder = "_"

        emptyBoard = [
            [placeholder] * 7,
            [placeholder] * 7,
            [placeholder] * 7,
            [placeholder] * 7,
            [placeholder] * 7,
            [placeholder] * 7,
            ["1", "2", "3", "4", "5", "6", "7"]
        ]

        return emptyBoard

    def showBoard(self) -> None:
        for line in self.board:
            for element in line:
                print("|" + element, end="")
            print("|")
