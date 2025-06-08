from pieces import Piece


class King(Piece):
    def __init__(self, location, color):
        super().__init__(location, color)

    def check_options(self, white_locations, black_locations):
        moves_list = []
        if self.color == "white":
            enemies_list = black_locations
            friends_list = white_locations
        else:
            friends_list = black_locations
            enemies_list = white_locations
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
