# two player chess in python with Pygame!
# part one, set up variables images and game loop

import pygame
from Constants import Constants
from Drawer import Drawer
from pieces import Bishop, King, Knight, Pawn, Queen, Rook
from Color import Color

def create_white_pieces():
    return [
        Rook((0, 0), Color.WHITE), Knight((1, 0), Color.WHITE), Bishop((2, 0), Color.WHITE),
        King((3, 0), Color.WHITE), Queen((4, 0), Color.WHITE), Bishop((5, 0), Color.WHITE),
        Knight((6, 0), Color.WHITE), Rook((7, 0), Color.WHITE),
        Pawn((0, 1), Color.WHITE), Pawn((1, 1), Color.WHITE), Pawn((2, 1), Color.WHITE), Pawn((3, 1), Color.WHITE),
        Pawn((4, 1), Color.WHITE), Pawn((5, 1), Color.WHITE), Pawn((6, 1), Color.WHITE), Pawn((7, 1), Color.WHITE),
    ]

def create_black_pieces():
    return [
        Rook((0, 7), Color.BLACK), Knight((1, 7), Color.BLACK), Bishop((2, 7), Color.BLACK),
        King((3, 7), Color.BLACK), Queen((4, 7), Color.BLACK), Bishop((5, 7), Color.BLACK),
        Knight((6, 7), Color.BLACK), Rook((7, 7), Color.BLACK),
        Pawn((0, 6), Color.BLACK), Pawn((1, 6), Color.BLACK), Pawn((2, 6), Color.BLACK), Pawn((3, 6), Color.BLACK),
        Pawn((4, 6), Color.BLACK), Pawn((5, 6), Color.BLACK), Pawn((6, 6), Color.BLACK), Pawn((7, 6), Color.BLACK),
    ]

# function to check all pieces valid options on board
def check_options(pieces, white_locations, black_locations):
    all_moves_list = []
    for piece in pieces:
        moves = piece.check_options(white_locations, black_locations)
        all_moves_list.append(moves)
    return all_moves_list

# check for valid moves for just selected piece
def check_valid_moves():
    if turn_step < 2:
        options_list = white_options
    else:
        options_list = black_options
    valid_options = options_list[selection]
    return valid_options

def get_locations(pieces):
    return [p.location for p in pieces]

pygame.init()
screen = pygame.display.set_mode([Constants.WIDTH, Constants.HEIGHT])
pygame.display.set_caption('Two-Player Pygame Chess!')
timer = pygame.time.Clock()
# game variables and images
white_pieces = create_white_pieces()
white_locations = get_locations(white_pieces)
black_pieces = create_black_pieces()
black_locations = get_locations(black_pieces)
captured_pieces_white = []
captured_pieces_black = []
# 0 - whites turn no selection: 1-whites turn piece selected: 2- black turn no selection, 3 - black turn piece selected
turn_step = 0
selection = 100
valid_moves = []
winner = ''
game_over = False
drawer = Drawer(screen)

# main game loop
black_options = check_options(black_pieces,white_locations, black_locations) 
white_options = check_options(white_pieces, white_locations, black_locations)
run = True
while run:
    timer.tick(Constants.FPS)
    drawer.draw_board(turn_step)
    drawer.draw_pieces(white_pieces, black_pieces, turn_step, selection)
    drawer.draw_captured(captured_pieces_white, captured_pieces_black)
    if turn_step < 2:
        for piece in white_pieces:
            if isinstance(piece, King):
                king_location = piece.location
                for i in range(len(black_options)):
                    if king_location in black_options[i]:
                        position = (king_location[0] * Constants.TILE_SIZE + 1,
                                    king_location[1] * Constants.TILE_SIZE + 1)
                        drawer.draw_check(position, 'dark red')
    else:
        for piece in black_pieces:
            if isinstance(piece, King):
                king_location = piece.location
                for i in range(len(white_options)):
                    if king_location in white_options[i]:
                        position = (king_location[0] * Constants.TILE_SIZE + 1,
                                    king_location[1] * Constants.TILE_SIZE + 1)
                        drawer.draw_check(position, 'dark blue')

    if selection != 100:
        valid_moves = check_valid_moves()
        drawer.draw_valid(valid_moves, turn_step)
    # event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and not game_over:
            x_coord = event.pos[0] // Constants.TILE_SIZE
            y_coord = event.pos[1] // Constants.TILE_SIZE
            click_coords = (x_coord, y_coord)
            if turn_step <= 1:
                if click_coords == (8, 8) or click_coords == (9, 8):
                    winner = 'black'
                if click_coords in white_locations:
                    selection = white_locations.index(click_coords)
                    if turn_step == 0:
                        turn_step = 1
                if click_coords in valid_moves and selection != 100:
                    white_locations[selection] = click_coords
                    white_pieces[selection].move_to(click_coords)
                    if click_coords in black_locations:
                        black_piece = black_locations.index(click_coords)
                        captured_pieces_white.append(black_pieces[black_piece])
                        if isinstance(black_pieces[black_piece], King):
                            winner = 'white'
                        black_pieces.pop(black_piece)
                        black_locations.pop(black_piece)
                    black_options = check_options(black_pieces, white_locations, black_locations) 
                    white_options = check_options(white_pieces, white_locations, black_locations)
                    turn_step = 2
                    selection = 100
                    valid_moves = []
            if turn_step > 1:
                if click_coords == (8, 8) or click_coords == (9, 8):
                    winner = 'white'
                if click_coords in black_locations:
                    selection = black_locations.index(click_coords)
                    if turn_step == 2:
                        turn_step = 3
                if click_coords in valid_moves and selection != 100:
                    black_locations[selection] = click_coords
                    black_pieces[selection].move_to(click_coords)
                    if click_coords in white_locations:
                        white_piece = white_locations.index(click_coords)
                        captured_pieces_black.append(white_pieces[white_piece])
                        if isinstance(white_pieces[white_piece], King):
                            winner = 'black'
                        white_pieces.pop(white_piece)
                        white_locations.pop(white_piece)
                    black_options = check_options(black_pieces, white_locations, black_locations) 
                    white_options = check_options(white_pieces, white_locations, black_locations)
                    turn_step = 0
                    selection = 100
                    valid_moves = []
        if event.type == pygame.KEYDOWN and game_over:
            if event.key == pygame.K_RETURN:
                game_over = False
                winner = ''
                white_pieces = create_white_pieces()
                white_locations = get_locations(white_pieces)
                black_pieces = create_black_pieces()
                black_locations = get_locations(black_pieces)
                captured_pieces_white = []
                captured_pieces_black = []
                turn_step = 0
                selection = 100
                valid_moves = []
                black_options = check_options(black_pieces, white_locations, black_locations) 
                white_options = check_options(white_pieces, white_locations, black_locations)

    if winner != '':
        game_over = True
        drawer.draw_game_over(winner)

    pygame.display.flip()
pygame.quit()
