from pieces import Piece
from Color import Color


class Bishop(Piece):
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
        for i in range(4):  # up-right, up-left, down-right, down-left
            path = True
            chain = 1
            if i == 0:
                x = 1
                y = -1
            elif i == 1:
                x = -1
                y = -1
            elif i == 2:
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
