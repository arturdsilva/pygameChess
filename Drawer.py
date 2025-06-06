import pygame
from Constants import Constants
from assets import Fonts


class Drawer:
    def __init__(self, screen):
        black_queen = pygame.image.load("assets/images/black queen.png")
        black_queen = pygame.transform.scale(black_queen, (80, 80))
        black_queen_small = pygame.transform.scale(black_queen, (45, 45))
        black_king = pygame.image.load("assets/images/black king.png")
        black_king = pygame.transform.scale(black_king, (80, 80))
        black_king_small = pygame.transform.scale(black_king, (45, 45))
        black_rook = pygame.image.load("assets/images/black rook.png")
        black_rook = pygame.transform.scale(black_rook, (80, 80))
        black_rook_small = pygame.transform.scale(black_rook, (45, 45))
        black_bishop = pygame.image.load("assets/images/black bishop.png")
        black_bishop = pygame.transform.scale(black_bishop, (80, 80))
        black_bishop_small = pygame.transform.scale(black_bishop, (45, 45))
        black_knight = pygame.image.load("assets/images/black knight.png")
        black_knight = pygame.transform.scale(black_knight, (80, 80))
        black_knight_small = pygame.transform.scale(black_knight, (45, 45))
        black_pawn = pygame.image.load("assets/images/black pawn.png")
        black_pawn = pygame.transform.scale(black_pawn, (65, 65))
        black_pawn_small = pygame.transform.scale(black_pawn, (45, 45))
        white_queen = pygame.image.load("assets/images/white queen.png")
        white_queen = pygame.transform.scale(white_queen, (80, 80))
        white_queen_small = pygame.transform.scale(white_queen, (45, 45))
        white_king = pygame.image.load("assets/images/white king.png")
        white_king = pygame.transform.scale(white_king, (80, 80))
        white_king_small = pygame.transform.scale(white_king, (45, 45))
        white_rook = pygame.image.load("assets/images/white rook.png")
        white_rook = pygame.transform.scale(white_rook, (80, 80))
        white_rook_small = pygame.transform.scale(white_rook, (45, 45))
        white_bishop = pygame.image.load("assets/images/white bishop.png")
        white_bishop = pygame.transform.scale(white_bishop, (80, 80))
        white_bishop_small = pygame.transform.scale(white_bishop, (45, 45))
        white_knight = pygame.image.load("assets/images/white knight.png")
        white_knight = pygame.transform.scale(white_knight, (80, 80))
        white_knight_small = pygame.transform.scale(white_knight, (45, 45))
        white_pawn = pygame.image.load("assets/images/white pawn.png")
        white_pawn = pygame.transform.scale(white_pawn, (65, 65))
        white_pawn_small = pygame.transform.scale(white_pawn, (45, 45))
        self.white_images = [
            white_pawn,
            white_queen,
            white_king,
            white_knight,
            white_rook,
            white_bishop,
        ]
        self.small_white_images = [
            white_pawn_small,
            white_queen_small,
            white_king_small,
            white_knight_small,
            white_rook_small,
            white_bishop_small,
        ]
        self.black_images = [
            black_pawn,
            black_queen,
            black_king,
            black_knight,
            black_rook,
            black_bishop,
        ]
        self.small_black_images = [
            black_pawn_small,
            black_queen_small,
            black_king_small,
            black_knight_small,
            black_rook_small,
            black_bishop_small,
        ]
        self.screen = screen
        self.fonts = Fonts.load_fonts()
        self.piece_list = ["pawn", "queen", "king", "knight", "rook", "bishop"]
        self.flash_counter = 0

    def draw_board(self, turn_step):
        self.screen.fill('dark gray')
        for i in range(32):
            column = i % 4
            row = i // 4
            if row % 2 == 0:
                pygame.draw.rect(
                    self.screen,
                    "light gray",
                    [
                        600 - (column * 200),
                        row * Constants.TILE_SIZE,
                        Constants.TILE_SIZE,
                        Constants.TILE_SIZE,
                    ],
                )
            else:
                pygame.draw.rect(
                    self.screen,
                    "light gray",
                    [
                        700 - (column * 200),
                        row * Constants.TILE_SIZE,
                        Constants.TILE_SIZE,
                        Constants.TILE_SIZE,
                    ],
                )
            pygame.draw.rect(self.screen, "gray", [0, 800, Constants.WIDTH, 100])
            pygame.draw.rect(self.screen, "gold", [0, 800, Constants.WIDTH, 100], 5)
            pygame.draw.rect(self.screen, "gold", [800, 0, 200, Constants.HEIGHT], 5)
            status_text = [
                "White: Select a Piece to Move!",
                "White: Select a Destination!",
                "Black: Select a Piece to Move!",
                "Black: Select a Destination!",
            ]
            self.screen.blit(
                self.fonts["big"].render(status_text[turn_step], True, "black"), (20, 820)
            )
            for i in range(9):
                pygame.draw.line(
                    self.screen,
                    "black",
                    (0, Constants.TILE_SIZE * i),
                    (800, Constants.TILE_SIZE * i),
                    2,
                )
                pygame.draw.line(
                    self.screen,
                    "black",
                    (Constants.TILE_SIZE * i, 0),
                    (Constants.TILE_SIZE * i, 800),
                    2,
                )
            self.screen.blit(self.fonts["big"].render("FORFEIT", True, "black"), (810, 830))

    def draw_pieces(self, white_pieces, white_locations, black_pieces, black_locations, turn_step, selection):
        for i in range(len(white_pieces)):
            index = self.piece_list.index(white_pieces[i])
            if white_pieces[i] == "pawn":
                self.screen.blit(
                    self.white_images[0],
                    (
                        white_locations[i][0] * Constants.TILE_SIZE + 22,
                        white_locations[i][1] * Constants.TILE_SIZE + 30,
                    ),
                )
            else:
                self.screen.blit(
                    self.white_images[index],
                    (
                        white_locations[i][0] * Constants.TILE_SIZE + 10,
                        white_locations[i][1] * Constants.TILE_SIZE + 10,
                    ),
                )
            if turn_step < 2:
                if selection == i:
                    pygame.draw.rect(
                        self.screen,
                        "red",
                        [
                            white_locations[i][0] * Constants.TILE_SIZE + 1,
                            white_locations[i][1] * Constants.TILE_SIZE + 1,
                            Constants.TILE_SIZE,
                            Constants.TILE_SIZE,
                        ],
                        2,
                    )

        for i in range(len(black_pieces)):
            index = self.piece_list.index(black_pieces[i])
            if black_pieces[i] == "pawn":
                self.screen.blit(
                    self.black_images[0],
                    (
                        black_locations[i][0] * Constants.TILE_SIZE + 22,
                        black_locations[i][1] * Constants.TILE_SIZE + 30,
                    ),
                )
            else:
                self.screen.blit(
                    self.black_images[index],
                    (
                        black_locations[i][0] * Constants.TILE_SIZE + 10,
                        black_locations[i][1] * Constants.TILE_SIZE + 10,
                    ),
                )
            if turn_step >= 2:
                if selection == i:
                    pygame.draw.rect(
                        self.screen,
                        "blue",
                        [
                            black_locations[i][0] * Constants.TILE_SIZE + 1,
                            black_locations[i][1] * Constants.TILE_SIZE + 1,
                            Constants.TILE_SIZE,
                            Constants.TILE_SIZE,
                        ],
                        2,
                    )

    def draw_valid(self, moves, turn_step):
        if turn_step < 2:
            color = "red"
        else:
            color = "blue"
        for i in range(len(moves)):
            pygame.draw.circle(
                self.screen,
                color,
                (
                    (moves[i][0] + 0.5) * Constants.TILE_SIZE,
                    (moves[i][1] + 0.5) * Constants.TILE_SIZE,
                ),
                5,
            )

    def draw_captured(self, captured_pieces_white, captured_pieces_black):
        for i in range(len(captured_pieces_white)):
            captured_piece = captured_pieces_white[i]
            index = self.piece_list.index(captured_piece)
            self.screen.blit(self.small_black_images[index], (825, 5 + 50 * i))
        for i in range(len(captured_pieces_black)):
            captured_piece = captured_pieces_black[i]
            index = self.piece_list.index(captured_piece)
            self.screen.blit(self.small_white_images[index], (925, 5 + 50 * i))

    def draw_check(self, pos, color):
        if self.flash_counter < 30:
            self.flash_counter += 1
        else:
            self.flash_counter = 0
        if self.flash_counter < 15:
            pygame.draw.rect(
                self.screen,
                color,
                [pos[0], pos[1], Constants.TILE_SIZE, Constants.TILE_SIZE],
                5,
            )

    def draw_game_over(self, winner):
        pygame.draw.rect(self.screen, "black", [200, 200, 400, 70])
        self.screen.blit(self.fonts["default"].render(f"{winner} won the game!", True, "white"), (210, 210))
        self.screen.blit(self.fonts["default"].render(f"Press ENTER to Restart!", True, "white"), (210, 240))
