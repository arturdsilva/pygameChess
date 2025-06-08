from pieces import Piece


class Pawn(Piece):
    def __init__(self, location, color):
        super().__init__(location, color)

    def check_options(self, white_locations, black_locations):
        moves_list = []
        x, y = self.location

        if self.color == "white":
            if (
                (x, y + 1) not in white_locations
                and (x, y + 1) not in black_locations
                and y < 8
            ):
                moves_list.append((x, y + 1))
            if (
                (x, y + 2) not in white_locations
                and (x, y + 2) not in black_locations
                and y == 1
            ):
                moves_list.append((x, y + 2))
            if (x + 1, y + 1) in black_locations:
                moves_list.append((x + 1, y + 1))
            if (x - 1, y + 1) in black_locations:
                moves_list.append((x - 1, y + 1))
        else:
            if (
                (x, y - 1) not in white_locations
                and (x, y - 1) not in black_locations
                and y > 0
            ):
                moves_list.append((x, y - 1))
            if (
                (x, y - 2) not in white_locations
                and (x, y - 2) not in black_locations
                and y == 6
            ):
                moves_list.append((x, y - 2))
            if (x + 1, y - 1) in white_locations:
                moves_list.append((x + 1, y - 1))
            if (x - 1, y - 1) in white_locations:
                moves_list.append((x - 1, y - 1))
        return moves_list
