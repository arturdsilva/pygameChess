from pieces import Piece
from Color import Color


class Queen(Piece):
    """
    Represents the queen piece, which moves any number of squares in any
    direction: vertically, horizontally, or diagonally.
    """

    def __init__(self, location, color):
        """
        Initializes the queen piece.

        Args:
            location (tuple): Represents the current position of the piece
                on the squares of the board.
            color: Represents the color of the piece.
        """

        super().__init__(location, color)

    def check_options(self, board):
        """
        Check all valid movement options for the queen from its current position.

        Args:
            board (Board): represents the current board state.
        Returns:
            List[Tuple[int, int]]: moves_list (A list of valid (row, column)
            positions the queen can legally move to)
        """

        moves_list = []
        if self.color == Color.WHITE:
            enemies_list = board.black_locations
            friends_list = board.white_locations
        else:
            friends_list = board.black_locations
            enemies_list = board.white_locations
        for i in range(8):  # 8 directions
            path = True
            chain = 1
            if i == 0:
                x = 0
                y = 1
            elif i == 1:
                x = 0
                y = -1
            elif i == 2:
                x = 1
                y = 0
            elif i == 3:
                x = -1
                y = 0
            elif i == 4:
                x = 1
                y = -1
            elif i == 5:
                x = -1
                y = -1
            elif i == 6:
                x = 1
                y = 1
            else:
                x = -1
                y = 1

            while path:
                if (
                    (self.location[0] + (chain * x), self.location[1] + (chain * y))
                    not in friends_list
                    and 0 <= self.location[0] + (chain * x) <= 7
                    and 0 <= self.location[1] + (chain * y) <= 7
                ):
                    moves_list.append(
                        (self.location[0] + (chain * x), self.location[1] + (chain * y))
                    )
                    if (
                        self.location[0] + (chain * x),
                        self.location[1] + (chain * y),
                    ) in enemies_list:
                        path = False
                    chain += 1
                else:
                    path = False
        return moves_list
