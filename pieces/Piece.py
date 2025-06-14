from abc import ABC, abstractmethod


class Piece(ABC):
    """
    Represents a generic piece on a chess board.
    """
    def __init__(self, location, color):
        """
        Initializes the piece.

        Args:
            location (tuple): Represents the current position of the piece
                on the squares of the board.
            color: Represents the color of the piece.
        """
        self.location = location
        self.color = color

    def move_to(self, location):
        """
        Updates the piece position to the new selected square.

        Args:
            location (tuple): Represents the new selected position
                of the piece on the squares of the board.
        """
        self.location = location

    @abstractmethod
    def check_options(self, board):
        """
        Check all valid movement options for the selected piece from its current position.

        Args:
            board (Board): represents the current board state.
        Returns:
            List[Tuple[int, int]]: moves_list (A list of valid (row, column)
            positions the queen can legally move to)
        """
        pass
