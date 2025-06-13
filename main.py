# two player chess in python with Pygame!

import pygame
from Constants import Constants
from Drawer import Drawer
from Board import Board
from pieces import Bishop, King, Knight, Pawn, Queen, Rook
from Color import Color


def check_for_check(board):
    for piece in board.pieces:
        options = piece.check_options(board)
        for option in options:
            target = board.get_piece_at_location(option)
            if isinstance(target, King):
                return target
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
run = True
while run:
    timer.tick(Constants.FPS)
    drawer.draw_board(turn_step)
    drawer.draw_pieces(board, turn_step, selected_piece)
    drawer.draw_captured(board)

    king_in_check = check_for_check(board)
    if king_in_check is not None:
        check_color = None
        if king_in_check.color == Color.WHITE:
            check_color = "dark red"
        else:
            check_color = "dark blue"
        drawer.draw_check(king_in_check.location, check_color)

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

    if winner != "":
        game_over = True
        drawer.draw_game_over(winner)

    pygame.display.flip()
pygame.quit()
