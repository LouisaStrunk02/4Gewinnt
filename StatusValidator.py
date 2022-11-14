from Board import Board
from Player import Player

class StatusValidator:
    def __init__(self):
        pass

    @staticmethod
    def is_win(board: Board, player: Player) -> bool:
        is_horizontal_win = StatusValidator.horizontal_win(board,player)
        is_vertical_win = StatusValidator.vertical_win(board, player)
        is_diagonal_win = StatusValidator.diagonal_win(board, player)
        is_win = is_horizontal_win or is_vertical_win or is_diagonal_win

        return is_win

    @staticmethod
    def horizontal_win(board: Board, player: Player) -> bool:
        for row in board.board:
            if StatusValidator.win_sequence(row, player.symbol):
                return True

        return False

    @staticmethod
    def vertical_win(board: Board, player: Player) -> bool:
        vertical_sequences: list[list[str]] = []
        number_of_columns = len(board.board[0])

        for column in range(number_of_columns):
            sequences: list[str] = []
            for row in board.board:
                sequences.append(row[column])

            vertical_sequences.append(sequences)

        for vertical_sequence in vertical_sequences:
            if StatusValidator.win_sequence(vertical_sequence, player.symbol):
                return True

        return False

    @staticmethod
    def diagonal_win(board: Board, player: Player) -> bool:
        board_matrix: list[list[str]] = board.board
        symbol: str = player.symbol

        columns: int = len(board_matrix[0])
        rows: int = len(board_matrix) -1

        for column in range(columns - 3):
            for row in range(rows - 3):
                is_sequence = board_matrix[row][column] == symbol and board_matrix[row + 1][column + 1] == symbol and board_matrix[row + 2][column + 2] == symbol and board_matrix[row + 3][column + 3] == symbol
                if is_sequence:
                    return True

        for column in range(columns - 3):
            for row in range(3, rows):
                is_sequence = board_matrix[row][column] == symbol and board_matrix[row - 1][column + 1] == symbol and board_matrix[row - 2][column + 2] == symbol and board_matrix[row - 3][column + 3] == symbol
                if is_sequence:
                    return True

        return False

    @staticmethod
    def win_sequence(sequence: list[str], player_symbol: str) -> bool:
        win_sequence = player_symbol * 4
        sequence_as_string = str.join("", sequence)

        is_win_sequence = win_sequence in sequence_as_string
        
        return is_win_sequence
