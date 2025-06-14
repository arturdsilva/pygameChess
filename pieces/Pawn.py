from pieces import Piece
from Color import Color


class Pawn(Piece):
    """
    Represents the pawn piece, which moves forward one square or two squares
    from the initial position and captures diagonally.
    """

    def __init__(self, location, color):
        """
        Initializes the pawn piece.

        Args:
            location (tuple): Represents the current position of the piece
                on the squares of the board.
            color: Represents the color of the piece.
        """

        super().__init__(location, color)

    def check_options(self, board):
        """
        Check all valid movement options for the pawn from its current position.

        Args:
            board (Board): represents the current board state.
        Returns:
            List[Tuple[int, int]]: moves_list (A list of valid (row, column)
            positions the pawn can legally move to)
        """

        moves_list = []
        x, y = self.location
        white_locations = board.white_locations
        black_locations = board.black_locations

        if self.color == Color.WHITE:
            if (
                (x, y + 1) not in white_locations
                and (x, y + 1) not in black_locations
                and y < 8
            ):
                moves_list.append((x, y + 1))
            if (
                (x, y + 2) not in white_locations
                and (x, y + 2) not in black_locations
                and y == 1
            ):
                moves_list.append((x, y + 2))
            if (x + 1, y + 1) in black_locations:
                moves_list.append((x + 1, y + 1))
            if (x - 1, y + 1) in black_locations:
                moves_list.append((x - 1, y + 1))
        else:
            if (
                (x, y - 1) not in white_locations
                and (x, y - 1) not in black_locations
                and y > 0
            ):
                moves_list.append((x, y - 1))
            if (
                (x, y - 2) not in white_locations
                and (x, y - 2) not in black_locations
                and y == 6
            ):
                moves_list.append((x, y - 2))
            if (x + 1, y - 1) in white_locations:
                moves_list.append((x + 1, y - 1))
            if (x - 1, y - 1) in white_locations:
                moves_list.append((x - 1, y - 1))
        return moves_list
