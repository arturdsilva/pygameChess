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
    
    def add_white_back_rank(self):
        """
        Add the white back rank pieces (rook, knight, bishop, etc.)
        
        Returns:
            self for method chaining
        """
        pieces_order = ["rook", "knight", "bishop", "king", "queen", "bishop", "knight", "rook"]
        for i, piece_type in enumerate(pieces_order):
            self.add_piece(piece_type, (i, 0), Color.WHITE)
        return self
    
    def add_white_pawns(self):
        """
        Add all white pawns
        
        Returns:
            self for method chaining
        """
        for i in range(8):
            self.add_piece("pawn", (i, 1), Color.WHITE)
        return self
    
    def add_black_back_rank(self):
        """
        Add the black back rank pieces (rook, knight, bishop, etc.)
        
        Returns:
            self for method chaining
        """
        piece_types = ["rook", "knight", "bishop", "king", "queen", "bishop", "knight", "rook"]
        for x, piece_type in enumerate(piece_types):
            self.add_piece(piece_type, (x, 7), Color.BLACK)
        return self
    
    def add_black_pawns(self):
        """
        Add all black pawns
        
        Returns:
            self for method chaining
        """
        for x in range(8):
            self.add_piece("pawn", (x, 6), Color.BLACK)
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
    
    def build_standard_board(self):
        """
        Build a standard chess board with all pieces in starting positions
        
        Returns:
            self for method chaining
        """
        return (self.add_white_back_rank()
                .add_white_pawns()
                .add_black_back_rank()
                .add_black_pawns())
    
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
