from Color import Color
from BoardBuilder import BoardBuilder


class Board:
    """
    Represents a chess board with white and black pieces.
    Uses a Builder pattern for construction (see BoardBuilder).
    """

    def __init__(self):
        """Initialize an empty board"""
        self.white_pieces = []
        self.black_pieces = []
        self.captured_white_pieces = []
        self.captured_black_pieces = []

    @classmethod
    def create_standard_board(cls):
        """
        Factory method to create a standard chess board
        
        Returns:
            Board: A standard chess board with all pieces in starting positions
        """
        builder = BoardBuilder()
        return builder.build_standard_board().build(cls)

    @classmethod
    def create_empty_board(cls):
        """
        Factory method to create an empty chess board
        
        Returns:
            Board: An empty chess board with no pieces
        """
        builder = BoardBuilder()
        return builder.build(cls)

    @property
    def pieces(self):
        """Get all pieces on the board"""
        return self.white_pieces + self.black_pieces

    @property
    def white_locations(self):
        """Get all locations occupied by white pieces"""
        return [piece.location for piece in self.white_pieces]

    @property
    def black_locations(self):
        """Get all locations occupied by black pieces"""
        return [piece.location for piece in self.black_pieces]

    def get_piece_at_location(self, location):
        """
        Get the piece at a specific board location
        
        Args:
            location: Tuple (x, y) representing the position to check
            
        Returns:
            The piece at the specified location or None if empty
        """
        for piece in self.pieces:
            if piece.location == location:
                return piece
        return None

    def remove_piece(self, piece):
        """
        Remove a piece from the board and add it to captured pieces
        
        Args:
            piece: The piece to remove
        """
        if piece in self.white_pieces:
            self.white_pieces.remove(piece)
            self.captured_white_pieces.append(piece)
        elif piece in self.black_pieces:
            self.black_pieces.remove(piece)
            self.captured_black_pieces.append(piece)
