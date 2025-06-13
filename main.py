# two player chess in python with Pygame!

import pygame
from Constants import Constants
from Drawer import Drawer
from Board import Board
from pieces import Bishop, King, Knight, Pawn, Queen, Rook
from Color import Color


def create_white_pieces():
    return [
        Rook((0, 0), Color.WHITE),
        Knight((1, 0), Color.WHITE),
        Bishop((2, 0), Color.WHITE),
        King((3, 0), Color.WHITE),
        Queen((4, 0), Color.WHITE),
        Bishop((5, 0), Color.WHITE),
        Knight((6, 0), Color.WHITE),
        Rook((7, 0), Color.WHITE),
        Pawn((0, 1), Color.WHITE),
        Pawn((1, 1), Color.WHITE),
        Pawn((2, 1), Color.WHITE),
        Pawn((3, 1), Color.WHITE),
        Pawn((4, 1), Color.WHITE),
        Pawn((5, 1), Color.WHITE),
        Pawn((6, 1), Color.WHITE),
        Pawn((7, 1), Color.WHITE),
    ]


def create_black_pieces():
    return [
        Rook((0, 7), Color.BLACK),
        Knight((1, 7), Color.BLACK),
        Bishop((2, 7), Color.BLACK),
        King((3, 7), Color.BLACK),
        Queen((4, 7), Color.BLACK),
        Bishop((5, 7), Color.BLACK),
        Knight((6, 7), Color.BLACK),
        Rook((7, 7), Color.BLACK),
        Pawn((0, 6), Color.BLACK),
        Pawn((1, 6), Color.BLACK),
        Pawn((2, 6), Color.BLACK),
        Pawn((3, 6), Color.BLACK),
        Pawn((4, 6), Color.BLACK),
        Pawn((5, 6), Color.BLACK),
        Pawn((6, 6), Color.BLACK),
        Pawn((7, 6), Color.BLACK),
    ]


# function to check all pieces valid options on board
def check_options(pieces, board):
    all_moves_list = []
    for piece in pieces:
        moves = piece.check_options(board)
        all_moves_list.append(moves)
    return all_moves_list


def check_for_check(pieces, enemy_options):
    for piece in pieces:
        if isinstance(piece, King):
            king_location = piece.location
            for moves in enemy_options:
                if king_location in moves:
                    pos = (
                        king_location[0] * Constants.TILE_SIZE + 1,
                        king_location[1] * Constants.TILE_SIZE + 1,
                    )
                    return pos
    return None


pygame.init()
screen = pygame.display.set_mode([Constants.WIDTH, Constants.HEIGHT])
pygame.display.set_caption("Two-Player Pygame Chess!")
timer = pygame.time.Clock()
# game variables and images
board = Board()
# 0 - whites turn
# 1 - black turn
turn_step = 0
selected_piece = None
valid_moves = []
winner = ""
game_over = False
drawer = Drawer(screen)

# main game loop
black_options = check_options(board.black_pieces, board)
white_options = check_options(board.white_pieces, board)
run = True
while run:
    timer.tick(Constants.FPS)
    drawer.draw_board(turn_step)
    drawer.draw_pieces(board, turn_step, selected_piece)
    drawer.draw_captured(board)

    if turn_step == 0:
        king_pos = check_for_check(board.white_pieces, black_options)
        if king_pos:
            drawer.draw_check(king_pos, "dark red")
    else:
        king_pos = check_for_check(board.black_pieces, white_options)
        if king_pos:
            drawer.draw_check(king_pos, "dark blue")

    if selected_piece is not None:
        valid_moves = selected_piece.check_options(board)
        drawer.draw_valid(valid_moves, turn_step)

    # event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and not game_over:
            x_coord = event.pos[0] // Constants.TILE_SIZE
            y_coord = event.pos[1] // Constants.TILE_SIZE
            click_location = (x_coord, y_coord)

            if turn_step == 0:
                if click_location == (8, 8) or click_location == (9, 8):
                    winner = "black"

                clicked_piece = board.get_piece_at_location(click_location)

                if clicked_piece and clicked_piece.color == Color.WHITE:
                    selected_piece = clicked_piece

                elif selected_piece and click_location in valid_moves:
                    if click_location in board.black_locations:
                        black_piece = board.get_piece_at_location(click_location)
                        board.remove_piece(black_piece)
                        if isinstance(black_piece, King):
                            winner = "white"
                    selected_piece.move_to(click_location)
                    black_options = check_options(board.black_pieces, board)
                    white_options = check_options(board.white_pieces, board)
                    turn_step = 1
                    selected_piece = None
                    valid_moves = []

            elif turn_step == 1:
                if click_location == (8, 8) or click_location == (9, 8):
                    winner = "white"

                clicked_piece = board.get_piece_at_location(click_location)

                if clicked_piece and clicked_piece.color == Color.BLACK:
                    selected_piece = clicked_piece
                elif selected_piece and click_location in valid_moves:
                    if click_location in board.white_locations:
                        white_piece = board.get_piece_at_location(click_location)
                        board.remove_piece(white_piece)
                        if isinstance(white_piece, King):
                            winner = "black"
                    selected_piece.move_to(click_location)
                    black_options = check_options(board.black_pieces, board)
                    white_options = check_options(board.white_pieces, board)
                    turn_step = 0
                    selected_piece = None
                    valid_moves = []

        if event.type == pygame.KEYDOWN and game_over:
            if event.key == pygame.K_RETURN:
                game_over = False
                winner = ""
                board = Board()
                turn_step = 0
                selected_piece = None
                valid_moves = []
                black_options = check_options(board.black_pieces, board)
                white_options = check_options(board.white_pieces, board)

    if winner != "":
        game_over = True
        drawer.draw_game_over(winner)

    pygame.display.flip()
pygame.quit()
