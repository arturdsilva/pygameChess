# two player chess in python with Pygame!
# part one, set up variables images and game loop

import pygame
from Constants import Constants
from Drawer import Drawer
from pieces import Bishop, King, Knight, Pawn, Queen, Rook

def create_white_pieces():
    return [
        Rook((0, 0), 'white'), Knight((1, 0), 'white'), Bishop((2, 0), 'white'),
        King((3, 0), 'white'), Queen((4, 0), 'white'), Bishop((5, 0), 'white'),
        Knight((6, 0), 'white'), Rook((7, 0), 'white'),
        Pawn((0, 1), 'white'), Pawn((1, 1), 'white'), Pawn((2, 1), 'white'), Pawn((3, 1), 'white'),
        Pawn((4, 1), 'white'), Pawn((5, 1), 'white'), Pawn((6, 1), 'white'), Pawn((7, 1), 'white'),
    ]

def create_black_pieces():
    return [
        Rook((0, 7), 'black'), Knight((1, 7), 'black'), Bishop((2, 7), 'black'),
        King((3, 7), 'black'), Queen((4, 7), 'black'), Bishop((5, 7), 'black'),
        Knight((6, 7), 'black'), Rook((7, 7), 'black'),
        Pawn((0, 6), 'black'), Pawn((1, 6), 'black'), Pawn((2, 6), 'black'), Pawn((3, 6), 'black'),
        Pawn((4, 6), 'black'), Pawn((5, 6), 'black'), Pawn((6, 6), 'black'), Pawn((7, 6), 'black'),
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

pygame.init()
screen = pygame.display.set_mode([Constants.WIDTH, Constants.HEIGHT])
pygame.display.set_caption('Two-Player Pygame Chess!')
timer = pygame.time.Clock()
# game variables and images
white_pieces = create_white_pieces()
white_locations = [(0, 0), (1, 0), (2, 0), (3, 0), (4, 0), (5, 0), (6, 0), (7, 0),
                   (0, 1), (1, 1), (2, 1), (3, 1), (4, 1), (5, 1), (6, 1), (7, 1)]
black_pieces = create_black_pieces()
black_locations = [(0, 7), (1, 7), (2, 7), (3, 7), (4, 7), (5, 7), (6, 7), (7, 7),
                   (0, 6), (1, 6), (2, 6), (3, 6), (4, 6), (5, 6), (6, 6), (7, 6)]
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
                white_locations = [(0, 0), (1, 0), (2, 0), (3, 0), (4, 0), (5, 0), (6, 0), (7, 0),
                                   (0, 1), (1, 1), (2, 1), (3, 1), (4, 1), (5, 1), (6, 1), (7, 1)]
                black_pieces = create_black_pieces()
                black_locations = [(0, 7), (1, 7), (2, 7), (3, 7), (4, 7), (5, 7), (6, 7), (7, 7),
                                   (0, 6), (1, 6), (2, 6), (3, 6), (4, 6), (5, 6), (6, 6), (7, 6)]
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
