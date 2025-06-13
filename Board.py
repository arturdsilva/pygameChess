from Color import Color
from PieceFactory import PieceFactory


class Board:
    def __init__(self):
        self.piece_factory = PieceFactory()

        self.white_pieces = [
            self.piece_factory.create_piece("rook", (0, 0), Color.WHITE),
            self.piece_factory.create_piece("knight", (1, 0), Color.WHITE),
            self.piece_factory.create_piece("bishop", (2, 0), Color.WHITE),
            self.piece_factory.create_piece("king", (3, 0), Color.WHITE),
            self.piece_factory.create_piece("queen", (4, 0), Color.WHITE),
            self.piece_factory.create_piece("bishop", (5, 0), Color.WHITE),
            self.piece_factory.create_piece("knight", (6, 0), Color.WHITE),
            self.piece_factory.create_piece("rook", (7, 0), Color.WHITE),
            self.piece_factory.create_piece("pawn", (0, 1), Color.WHITE),
            self.piece_factory.create_piece("pawn", (1, 1), Color.WHITE),
            self.piece_factory.create_piece("pawn", (2, 1), Color.WHITE),
            self.piece_factory.create_piece("pawn", (3, 1), Color.WHITE),
            self.piece_factory.create_piece("pawn", (4, 1), Color.WHITE),
            self.piece_factory.create_piece("pawn", (5, 1), Color.WHITE),
            self.piece_factory.create_piece("pawn", (6, 1), Color.WHITE),
            self.piece_factory.create_piece("pawn", (7, 1), Color.WHITE),
        ]
        self.black_pieces = [
            self.piece_factory.create_piece("rook", (0, 7), Color.BLACK),
            self.piece_factory.create_piece("knight", (1, 7), Color.BLACK),
            self.piece_factory.create_piece("bishop", (2, 7), Color.BLACK),
            self.piece_factory.create_piece("king", (3, 7), Color.BLACK),
            self.piece_factory.create_piece("queen", (4, 7), Color.BLACK),
            self.piece_factory.create_piece("bishop", (5, 7), Color.BLACK),
            self.piece_factory.create_piece("knight", (6, 7), Color.BLACK),
            self.piece_factory.create_piece("rook", (7, 7), Color.BLACK),
            self.piece_factory.create_piece("pawn", (0, 6), Color.BLACK),
            self.piece_factory.create_piece("pawn", (1, 6), Color.BLACK),
            self.piece_factory.create_piece("pawn", (2, 6), Color.BLACK),
            self.piece_factory.create_piece("pawn", (3, 6), Color.BLACK),
            self.piece_factory.create_piece("pawn", (4, 6), Color.BLACK),
            self.piece_factory.create_piece("pawn", (5, 6), Color.BLACK),
            self.piece_factory.create_piece("pawn", (6, 6), Color.BLACK),
            self.piece_factory.create_piece("pawn", (7, 6), Color.BLACK),
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
