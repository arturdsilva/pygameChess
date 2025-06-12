from pieces import Piece
from Color import Color


class Rook(Piece):
    def __init__(self, location, color):
        super().__init__(location, color)

    def check_options(self, board):
        moves_list = []
        if self.color == Color.WHITE:
            enemies_list = board.black_locations
            friends_list = board.white_locations
        else:
            friends_list = board.black_locations
            enemies_list = board.white_locations
        for i in range(4):  # down, up, right, left
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
            else:
                x = -1
                y = 0
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
