from pieces import Piece
from Color import Color


class Knight(Piece):
    """
    Represents the knight piece, which moves in an L-shape: two squares in one
    direction and then one square perpendicular.
    """

    def __init__(self, location, color):
        """
        Initializes the knight piece.

        Args:
            location (tuple): Represents the current position of the piece
                on the squares of the board.
            color: Represents the color of the piece.
        """

        super().__init__(location, color)

    def check_options(self, board):
        """
        Check all valid movement options for the knight from its current position.

        Args:
            board (Board): represents the current board state.
        Returns:
            List[Tuple[int, int]]: moves_list (A list of valid (row, column)
            positions the knight can legally move to)
        """

        moves_list = []
        if self.color == Color.WHITE:
            enemies_list = board.black_locations
            friends_list = board.white_locations
        else:
            friends_list = board.black_locations
            enemies_list = board.white_locations
        # 8 squares to check for knights, they can go two squares in one direction and one in another
        targets = [
            (1, 2),
            (1, -2),
            (2, 1),
            (2, -1),
            (-1, 2),
            (-1, -2),
            (-2, 1),
            (-2, -1),
        ]
        for i in range(8):
            target = (
                self.location[0] + targets[i][0],
                self.location[1] + targets[i][1],
            )
            if (
                target not in friends_list
                and 0 <= target[0] <= 7
                and 0 <= target[1] <= 7
            ):
                moves_list.append(target)
        return moves_list
