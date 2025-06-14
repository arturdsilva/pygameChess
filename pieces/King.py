from pieces import Piece
from Color import Color


class King(Piece):
    """
    Represents the king piece, which moves one square in any direction.
    """

    def __init__(self, location, color):
        """
        Initializes the king piece.

        Args:
            location (tuple): Represents the current position of the piece
                on the squares of the board.
            color: Represents the color of the piece.
        """
        super().__init__(location, color)

    def check_options(self, board):
        """
        Check all valid movement options for the king from its current position.

        Args:
            board (Board): represents the current board state.
        Returns:
            List[Tuple[int, int]]: moves_list (A list of valid (row, column)
            positions the king can legally move to)
        """
        moves_list = []
        if self.color == Color.WHITE:
            enemies_list = board.black_locations
            friends_list = board.white_locations
        else:
            friends_list = board.black_locations
            enemies_list = board.white_locations
        # 8 squares to check for kings, they can go one square any direction
        targets = [(1, 0), (1, 1), (1, -1), (-1, 0), (-1, 1), (-1, -1), (0, 1), (0, -1)]
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
