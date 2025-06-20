import pygame

from Constants import Constants
from assets import Fonts
from Color import Color


class Drawer:
    """
    Responsible for drawing the board, pieces, valid moves and game messages.
    """

    def __init__(self, screen):
        """
        Loads images of the pieces, fonts and prepares the screen for drawing.

        Args:
            screen: Game surface where will be drawn.
        """
        black_queen = pygame.image.load("assets/images/black queen.png")
        black_queen = pygame.transform.scale(
            black_queen, (Constants.PIECE_SURFACE_SIZE, Constants.PIECE_SURFACE_SIZE)
        )
        black_queen_small = pygame.transform.scale(
            black_queen,
            (Constants.SMALL_PIECE_SURFACE_SIZE, Constants.SMALL_PIECE_SURFACE_SIZE),
        )
        black_king = pygame.image.load("assets/images/black king.png")
        black_king = pygame.transform.scale(
            black_king, (Constants.PIECE_SURFACE_SIZE, Constants.PIECE_SURFACE_SIZE)
        )
        black_king_small = pygame.transform.scale(
            black_king,
            (Constants.SMALL_PIECE_SURFACE_SIZE, Constants.SMALL_PIECE_SURFACE_SIZE),
        )
        black_rook = pygame.image.load("assets/images/black rook.png")
        black_rook = pygame.transform.scale(
            black_rook, (Constants.PIECE_SURFACE_SIZE, Constants.PIECE_SURFACE_SIZE)
        )
        black_rook_small = pygame.transform.scale(
            black_rook,
            (Constants.SMALL_PIECE_SURFACE_SIZE, Constants.SMALL_PIECE_SURFACE_SIZE),
        )
        black_bishop = pygame.image.load("assets/images/black bishop.png")
        black_bishop = pygame.transform.scale(
            black_bishop, (Constants.PIECE_SURFACE_SIZE, Constants.PIECE_SURFACE_SIZE)
        )
        black_bishop_small = pygame.transform.scale(
            black_bishop,
            (Constants.SMALL_PIECE_SURFACE_SIZE, Constants.SMALL_PIECE_SURFACE_SIZE),
        )
        black_knight = pygame.image.load("assets/images/black knight.png")
        black_knight = pygame.transform.scale(
            black_knight, (Constants.PIECE_SURFACE_SIZE, Constants.PIECE_SURFACE_SIZE)
        )
        black_knight_small = pygame.transform.scale(
            black_knight,
            (Constants.SMALL_PIECE_SURFACE_SIZE, Constants.SMALL_PIECE_SURFACE_SIZE),
        )
        black_pawn = pygame.image.load("assets/images/black pawn.png")
        black_pawn = pygame.transform.scale(
            black_pawn, (Constants.PAWN_SURFACE_SIZE, Constants.PAWN_SURFACE_SIZE)
        )
        black_pawn_small = pygame.transform.scale(
            black_pawn,
            (Constants.SMALL_PIECE_SURFACE_SIZE, Constants.SMALL_PIECE_SURFACE_SIZE),
        )
        white_queen = pygame.image.load("assets/images/white queen.png")
        white_queen = pygame.transform.scale(
            white_queen, (Constants.PIECE_SURFACE_SIZE, Constants.PIECE_SURFACE_SIZE)
        )
        white_queen_small = pygame.transform.scale(
            white_queen,
            (Constants.SMALL_PIECE_SURFACE_SIZE, Constants.SMALL_PIECE_SURFACE_SIZE),
        )
        white_king = pygame.image.load("assets/images/white king.png")
        white_king = pygame.transform.scale(
            white_king, (Constants.PIECE_SURFACE_SIZE, Constants.PIECE_SURFACE_SIZE)
        )
        white_king_small = pygame.transform.scale(
            white_king,
            (Constants.SMALL_PIECE_SURFACE_SIZE, Constants.SMALL_PIECE_SURFACE_SIZE),
        )
        white_rook = pygame.image.load("assets/images/white rook.png")
        white_rook = pygame.transform.scale(
            white_rook, (Constants.PIECE_SURFACE_SIZE, Constants.PIECE_SURFACE_SIZE)
        )
        white_rook_small = pygame.transform.scale(
            white_rook,
            (Constants.SMALL_PIECE_SURFACE_SIZE, Constants.SMALL_PIECE_SURFACE_SIZE),
        )
        white_bishop = pygame.image.load("assets/images/white bishop.png")
        white_bishop = pygame.transform.scale(
            white_bishop, (Constants.PIECE_SURFACE_SIZE, Constants.PIECE_SURFACE_SIZE)
        )
        white_bishop_small = pygame.transform.scale(
            white_bishop,
            (Constants.SMALL_PIECE_SURFACE_SIZE, Constants.SMALL_PIECE_SURFACE_SIZE),
        )
        white_knight = pygame.image.load("assets/images/white knight.png")
        white_knight = pygame.transform.scale(
            white_knight, (Constants.PIECE_SURFACE_SIZE, Constants.PIECE_SURFACE_SIZE)
        )
        white_knight_small = pygame.transform.scale(
            white_knight,
            (Constants.SMALL_PIECE_SURFACE_SIZE, Constants.SMALL_PIECE_SURFACE_SIZE),
        )
        white_pawn = pygame.image.load("assets/images/white pawn.png")
        white_pawn = pygame.transform.scale(
            white_pawn, (Constants.PAWN_SURFACE_SIZE, Constants.PAWN_SURFACE_SIZE)
        )
        white_pawn_small = pygame.transform.scale(
            white_pawn,
            (Constants.SMALL_PIECE_SURFACE_SIZE, Constants.SMALL_PIECE_SURFACE_SIZE),
        )
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

    def draw_board(self, current_turn):
        """
        Draws the board, lines and text indicating the player's turn.

        Args:
            turn_step: turns of white(0) or black(1) pieces.
        """
        self.screen.fill("dark gray")
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
            status_text = {Color.WHITE: "White's turn!", Color.BLACK: "Black's turn!"}
            self.screen.blit(
                self.fonts["big"].render(status_text[current_turn], True, "black"),
                (20, 820),
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
            self.screen.blit(
                self.fonts["medium"].render("FORFEIT", True, "black"), (810, 830)
            )

    def draw_pieces(self, board, current_turn, selected_piece):
        """
        Draws the pieces on the board and highlights the selected piece.

        Args:
            board: contains the white and black pieces.
            turn_step: turns of white(0) or black(1) pieces.
            selected_piece: selected piece.
        """
        for i, piece in enumerate(board.white_pieces):
            name = type(piece).__name__.lower()
            index = self.piece_list.index(name)
            x, y = piece.location

            if name == "pawn":
                self.screen.blit(
                    self.white_images[0],
                    (x * Constants.TILE_SIZE + 22, y * Constants.TILE_SIZE + 30),
                )
            else:
                self.screen.blit(
                    self.white_images[index],
                    (x * Constants.TILE_SIZE + 10, y * Constants.TILE_SIZE + 10),
                )

            if current_turn == Color.WHITE and piece == selected_piece:
                pygame.draw.rect(
                    self.screen,
                    "red",
                    [
                        x * Constants.TILE_SIZE + 1,
                        y * Constants.TILE_SIZE + 1,
                        Constants.TILE_SIZE,
                        Constants.TILE_SIZE,
                    ],
                    2,
                )

        for i, piece in enumerate(board.black_pieces):
            name = type(piece).__name__.lower()
            index = self.piece_list.index(name)
            x, y = piece.location

            if name == "pawn":
                self.screen.blit(
                    self.black_images[0],
                    (x * Constants.TILE_SIZE + 22, y * Constants.TILE_SIZE + 30),
                )
            else:
                self.screen.blit(
                    self.black_images[index],
                    (x * Constants.TILE_SIZE + 10, y * Constants.TILE_SIZE + 10),
                )

            if current_turn == Color.BLACK and piece == selected_piece:
                pygame.draw.rect(
                    self.screen,
                    "blue",
                    [
                        x * Constants.TILE_SIZE + 1,
                        y * Constants.TILE_SIZE + 1,
                        Constants.TILE_SIZE,
                        Constants.TILE_SIZE,
                    ],
                    2,
                )

    def draw_valid(self, moves, current_turn):
        """
        Draws circles at valid move positions.

        Args:
            moves: list of positions (x, y).
            turn_step: turns of white(0) or black(1) pieces.
        """
        if current_turn == Color.WHITE:
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

    def draw_captured(self, board):
        """
        Shows captured pieces in the side panel.

        Args:
            board (Board): represents the current board state.
        """
        for i in range(len(board.captured_white_pieces)):
            captured_piece = board.captured_white_pieces[i]
            piece_name = type(captured_piece).__name__.lower()
            index = self.piece_list.index(piece_name)
            self.screen.blit(self.small_white_images[index], (825, 5 + 50 * i))
        for i in range(len(board.captured_black_pieces)):
            captured_piece = board.captured_black_pieces[i]
            piece_name = type(captured_piece).__name__.lower()
            index = self.piece_list.index(piece_name)
            self.screen.blit(self.small_black_images[index], (925, 5 + 50 * i))

    def draw_check(self, location, color):
        """
        Highlights the king in check with a blinking outline.

        Args:
            location (tuple): Represents the current position of the piece
                on the squares of the board.
            color: Represents the color of the piece.
        """
        if self.flash_counter < 30:
            self.flash_counter += 1
        else:
            self.flash_counter = 0
        if self.flash_counter < 15:
            pygame.draw.rect(
                self.screen,
                color,
                [
                    location[0] * Constants.TILE_SIZE,
                    location[1] * Constants.TILE_SIZE,
                    Constants.TILE_SIZE,
                    Constants.TILE_SIZE,
                ],
                5,
            )

    def draw_game_over(self, winner):
        """
        Displays game end message with the winner.

        Args:
            winner: text indicating who won.
        """
        pygame.draw.rect(self.screen, "black", [200, 200, 400, 70])
        self.screen.blit(
            self.fonts["default"].render(f"{winner} won the game!", True, "white"),
            (210, 210),
        )
        self.screen.blit(
            self.fonts["default"].render(f"Press ENTER to Restart!", True, "white"),
            (210, 240),
        )
