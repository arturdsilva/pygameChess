from pieces import Bishop, King, Knight, Pawn, Queen, Rook
from Color import Color


class PieceFactory:
    def __init__(self):
        self._piece_types = {
            "pawn": Pawn,
            "rook": Rook,
            "knight": Knight,
            "bishop": Bishop,
            "queen": Queen,
            "king": King
        }

    def create_piece(self, piece_type, location, color):
        """
        Factory method to create chess pieces
        
        Args:
            piece_type: String representing the type of piece
            location: Tuple (x, y) representing the piece's position
            color: Color enum value
            
        Returns:
            A chess piece instance of the specified type
        """
        piece_type = piece_type.lower()

        if not self._is_valid_location(location):
            raise ValueError(
                f"PieceFactory: invalid piece location: {location}")

        piece_class = self._piece_types.get(piece_type)
        if piece_class is None:
            raise ValueError(
                f"PieceFactory: unknown piece type: {piece_type}")

        return piece_class(location, color)

    def _is_valid_location(self, location):
        """Validate if the location is within the board boundaries"""
        x, y = location
        return 0 <= x <= 7 and 0 <= y <= 7
