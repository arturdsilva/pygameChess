from pieces import Piece
from Color import Color


class Knight(Piece):
    def __init__(self, location, color):
        super().__init__(location, color)

    def check_options(self, white_locations, black_locations):
        moves_list = []
        if self.color == Color.WHITE:
            enemies_list = black_locations
            friends_list = white_locations
        else:
            friends_list = black_locations
            enemies_list = white_locations
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
