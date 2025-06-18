from Color import Color
from pieces import Bishop, King, Knight, Pawn, Queen, Rook


class Board:
    """
    Represents a chess board with white and black pieces.
    Uses a Builder pattern for construction (see BoardBuilder).
    """

    def __init__(self):
        """
        Initialize an empty board
        """
        self.white_pieces = []
        self.black_pieces = []
        self.captured_white_pieces = []
        self.captured_black_pieces = []
        self.piece_types = {
            "pawn": Pawn,
            "rook": Rook,
            "knight": Knight,
            "bishop": Bishop,
            "queen": Queen,
            "king": King,
        }
        self.build_standard_board()

    def build_standard_board(self):
        """
        Build a standard chess board with all pieces in starting positions
        """
        self.add_back_rank(Color.BLACK, 7)
        self.add_pawns(Color.BLACK, 6)
        self.add_pawns(Color.WHITE, 1)
        self.add_back_rank(Color.WHITE, 0)

    @property
    def pieces(self):
        """
        Get all pieces on the board
        """
        return self.white_pieces + self.black_pieces

    @property
    def white_locations(self):
        """
        Get all locations occupied by white pieces
        """
        return [piece.location for piece in self.white_pieces]

    @property
    def black_locations(self):
        """
        Get all locations occupied by black pieces
        """
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

    def add_piece(self, piece_type, location, color):
        """
        Add a specific piece to the board

        Args:
            piece_type: String representing the type of piece
            location: Tuple (x, y) representing the piece's position
            color: Enum value representing the piece's color
        """
        piece_type = piece_type.lower()
        piece_class = self.piece_types.get(piece_type)
        piece = piece_class(location, color)
        if color == Color.WHITE:
            self.white_pieces.append(piece)
        else:
            self.black_pieces.append(piece)

    def add_pawns(self, color, line):
        """
        Add a line of pawns at the initial position

        Args:
            color: Enum value representing the color of the pieces
            line: Integer representing the line where the rank will be inserted
        """
        for i in range(8):
            self.add_piece("pawn", (i, line), color)

    def add_back_rank(self, color, line):
        """
        Add the back rank pieces (rook, knight, bishop, etc.)

        Args:
            color: Enum value representing the color of the pieces
            line: Integer representing the line where the rank will be inserted
        """
        pieces_order = [
            "rook",
            "knight",
            "bishop",
            "king",
            "queen",
            "bishop",
            "knight",
            "rook",
        ]
        for i, piece_type in enumerate(pieces_order):
            self.add_piece(piece_type, (i, line), color)

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
