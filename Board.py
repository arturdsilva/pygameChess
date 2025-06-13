from pieces import Bishop, King, Knight, Pawn, Queen, Rook
from Color import Color


class Board:
    def __init__(self):
        self.white_pieces = [
            Rook((0, 0), Color.WHITE),
            Knight((1, 0), Color.WHITE),
            Bishop((2, 0), Color.WHITE),
            King((3, 0), Color.WHITE),
            Queen((4, 0), Color.WHITE),
            Bishop((5, 0), Color.WHITE),
            Knight((6, 0), Color.WHITE),
            Rook((7, 0), Color.WHITE),
            Pawn((0, 1), Color.WHITE),
            Pawn((1, 1), Color.WHITE),
            Pawn((2, 1), Color.WHITE),
            Pawn((3, 1), Color.WHITE),
            Pawn((4, 1), Color.WHITE),
            Pawn((5, 1), Color.WHITE),
            Pawn((6, 1), Color.WHITE),
            Pawn((7, 1), Color.WHITE),
        ]
        self.black_pieces = [
            Rook((0, 7), Color.BLACK),
            Knight((1, 7), Color.BLACK),
            Bishop((2, 7), Color.BLACK),
            King((3, 7), Color.BLACK),
            Queen((4, 7), Color.BLACK),
            Bishop((5, 7), Color.BLACK),
            Knight((6, 7), Color.BLACK),
            Rook((7, 7), Color.BLACK),
            Pawn((0, 6), Color.BLACK),
            Pawn((1, 6), Color.BLACK),
            Pawn((2, 6), Color.BLACK),
            Pawn((3, 6), Color.BLACK),
            Pawn((4, 6), Color.BLACK),
            Pawn((5, 6), Color.BLACK),
            Pawn((6, 6), Color.BLACK),
            Pawn((7, 6), Color.BLACK),
        ]
        self.captured_white_pieces = []
        self.captured_black_pieces = []

    @property
    def pieces(self):
        return self.white_pieces + self.black_pieces

    @property
    def white_locations(self):
        return [piece.location for piece in self.white_pieces]

    @property
    def black_locations(self):
        return [piece.location for piece in self.black_pieces]

    def get_piece_at_location(self, location):
        for piece in self.pieces:
            if piece.location == location:
                return piece
        return None

    def remove_piece(self, piece):
        if piece in self.white_pieces:
            self.white_pieces.remove(piece)
            self.captured_white_pieces.append(piece)
        elif piece in self.black_pieces:
            self.black_pieces.remove(piece)
            self.captured_black_pieces.append(piece)
