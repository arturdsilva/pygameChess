from Color import Color
from PieceFactory import PieceFactory


class BoardBuilder:
    """
    Builder pattern implementation for creating Board objects.
    Provides a fluent interface for board construction and configuration.
    """

    def __init__(self):
        """Initialize a new BoardBuilder with empty piece collections"""
        self.piece_factory = PieceFactory()
        self.white_pieces = []
        self.black_pieces = []
        self.captured_white_pieces = []
        self.captured_black_pieces = []

    def add_piece(self, piece_type, location, color):
        """
        Add a specific piece to the board
        
        Args:
            piece_type: String representing the type of piece
            location: Tuple (x, y) representing the piece's position
            color: Enum value representing the piece's color
            
        Returns:
            self for method chaining
        """
        piece = self.piece_factory.create_piece(piece_type, location, color)
        if color == Color.WHITE:
            self.white_pieces.append(piece)
        else:
            self.black_pieces.append(piece)
        return self

    def add_back_rank(self, color, line=None):
        """
        Add the back rank pieces (rook, knight, bishop, etc.)

        Args:
            color: Enum value representing the color of the pieces
            line: Integer representing the line where the rank will be inserted
        
        Returns:
            self for method chaining
        """
        if line is None:
            if color == Color.WHITE:
                line = 0
            else:
                line = 7
        pieces_order = ["rook", "knight", "bishop", "king", "queen", "bishop",
                        "knight", "rook"]
        for i, piece_type in enumerate(pieces_order):
            self.add_piece(piece_type, (i, line), color)
        return self

    def add_pawns(self, color, line=None):
        """
        Add a line of pawns at the initial position

        Args:
            color: Enum value representing the color of the pieces
            line: Integer representing the line where the rank will be inserted
        
        Returns:
            self for method chaining
        """
        if line is None:
            if color == Color.WHITE:
                line = 1
            else:
                line = 6
        for i in range(8):
            self.add_piece("pawn", (i, line), color)
        return self

    def set_captured_pieces(self, white_captured=None, black_captured=None):
        """
        Set captured pieces
        
        Args:
            white_captured: List of captured white pieces
            black_captured: List of captured black pieces
            
        Returns:
            self for method chaining
        """
        if white_captured is not None:
            self.captured_white_pieces = white_captured
        if black_captured is not None:
            self.captured_black_pieces = black_captured
        return self

    def set_standard_board(self):
        """
        Build a standard chess board with all pieces in starting positions
        
        Returns:
            self for method chaining
        """
        return (self.add_back_rank(Color.WHITE)
                .add_pawns(Color.WHITE)
                .add_back_rank(Color.BLACK)
                .add_pawns(Color.BLACK))

    def build(self, board_class):
        """
        Build and return the configured Board
        
        Args:
            board_class: The Board class to instantiate
            
        Returns:
            A fully configured Board instance
        """
        board = board_class()
        board.white_pieces = self.white_pieces
        board.black_pieces = self.black_pieces
        board.captured_white_pieces = self.captured_white_pieces
        board.captured_black_pieces = self.captured_black_pieces
        return board
