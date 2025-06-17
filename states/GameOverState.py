import pygame

from states.AbstractGameState import AbstractGameState
from Color import Color


class GameOverState(AbstractGameState):
    """
    State representing the end of the game.
    Handles interactions when the game is over.
    """

    def handle_click(self, game, click_location):
        """
        Handle click event when game is over

        Args:
            game: Game instance
            click_location: Tuple (x, y) representing board coordinates
        """
        # No click handling in game over state
        pass

    def handle_key(self, game, key):
        from states.PlayingState import PlayingState

        """
        Handle keyboard input when game is over
        
        Args:
            game: Game instance
            key: Key code that was pressed
        """
        if key == pygame.K_RETURN:
            # Reset game state on Enter key
            game.reset()
            game.change_state(PlayingState())

    def update(self, game):
        """
        Update game state when game is over

        Args:
            game: Game instance
        """
        # No updates needed in game over state
        pass

    def render(self, game):
        """
        Render the game when game is over

        Args:
            game: Game instance
        """
        # Draw the final board state
        game.drawer.draw_board(Color.WHITE)
        game.drawer.draw_pieces(game.board, Color.WHITE, None)
        game.drawer.draw_captured(game.board)

        # Draw game over message
        game.drawer.draw_game_over(game.winner)

    @property
    def name(self):
        """
        Get the name of this state

        Returns:
            String "GAME_OVER"
        """
        return "GAME_OVER"
