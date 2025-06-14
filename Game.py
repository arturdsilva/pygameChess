import pygame

from Board import Board
from pieces import King


class Game:
    """
    Game class that manages the chess game state.
    Acts as the context in the State pattern.
    """

    def __init__(self, screen):
        """
        Initialize a new game
        
        Args:
            screen: Pygame screen surface for rendering
        """
        from Drawer import Drawer
        from states.PlayingState import PlayingState

        self.screen = screen
        self.drawer = Drawer(screen)
        self.board = Board.create_standard_board()
        self.winner = ""
        self.check_color = None
        self.current_state = PlayingState()

    def change_state(self, new_state):
        """
        Change the current game state
        
        Args:
            new_state: New GameState instance to transition to
        """
        self.current_state = new_state

    def handle_events(self):
        """
        Process all game events
        
        Returns:
            Boolean indicating if the game should continue running
        """
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False

            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                from Constants import Constants
                x_coord = event.pos[0] // Constants.TILE_SIZE
                y_coord = event.pos[1] // Constants.TILE_SIZE
                click_location = (x_coord, y_coord)
                self.current_state.handle_click(self, click_location)

            if event.type == pygame.KEYDOWN:
                self.current_state.handle_key(self, event.key)

        return True

    def update(self):
        """Update the game state"""
        self.current_state.update(self)

    def render(self):
        """Render the current game state"""
        self.current_state.render(self)
        pygame.display.flip()

    def reset(self):
        """Reset the game to its initial state"""
        self.board = Board.create_standard_board()
        self.winner = ""
        self.check_color = None

    def check_for_check(self, board):
        """
        Check if any king is in check
        
        Args:
            board: Board instance to check
            
        Returns:
            King piece that is in check, or None
        """
        for piece in board.pieces:
            options = piece.check_options(board)
            for option in options:
                target = board.get_piece_at_location(option)
                if isinstance(target, King):
                    return target
        return None

    @property
    def current_state_name(self):
        """
        Get the name of the current game state
        
        Returns:
            String representing the current state name
        """
        return self.current_state.name
