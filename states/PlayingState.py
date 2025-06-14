from Color import Color
from pieces import King
from states.AbstractGameState import AbstractGameState
from states.GameOverState import GameOverState


class PlayingState(AbstractGameState):
    """
    State representing active gameplay.
    Handles game interactions for both players' turns.
    """

    def __init__(self):
        """Initialize the playing state"""
        self.selected_piece = None
        self.valid_moves = []
        self.current_turn = 0  # 0 for white, 1 for black

    @property
    def current_player_color(self):
        """Get the color of the current player"""
        return Color.WHITE if self.current_turn == 0 else Color.BLACK

    @property
    def opponent_color(self):
        """Get the color of the opponent player"""
        return Color.BLACK if self.current_turn == 0 else Color.WHITE

    @property
    def opponent_pieces(self):
        """Get opponent's pieces based on current turn"""
        return lambda \
                board: board.black_pieces if self.current_turn == 0 else board.white_pieces

    @property
    def opponent_locations(self):
        """Get opponent's piece locations based on current turn"""
        return lambda \
                board: board.black_locations if self.current_turn == 0 else board.white_locations

    @property
    def check_color(self):
        """Get the highlight color for king in check"""
        return "dark red" if self.current_player_color == Color.WHITE else "dark blue"

    def handle_click(self, game, click_location):
        """
        Handle click event during gameplay
        
        Args:
            game: Game instance
            click_location: Tuple (x, y) representing board coordinates
        """
        # Check for resign button
        if click_location == (8, 8) or click_location == (9, 8):
            game.winner = "black" if self.current_turn == 0 else "white"
            game.change_state(GameOverState())
            return

        # Get the piece at clicked location
        clicked_piece = game.board.get_piece_at_location(click_location)

        # If current player's piece is clicked, select it
        if clicked_piece and clicked_piece.color == self.current_player_color:
            self.selected_piece = clicked_piece
            self.valid_moves = clicked_piece.check_options(game.board)

        # If a piece is already selected and a valid move is clicked
        elif self.selected_piece and click_location in self.valid_moves:
            self._handle_move(game, click_location)

    def _handle_move(self, game, target_location):
        """
        Handle piece movement and capture logic
        
        Args:
            game: Game instance
            target_location: Tuple (x, y) representing the target location
        """
        # Check for capture
        opponent_locations = self.opponent_locations(game.board)
        if target_location in opponent_locations:
            captured_piece = game.board.get_piece_at_location(target_location)
            game.board.remove_piece(captured_piece)

            # If king is captured, game over
            if isinstance(captured_piece, King):
                game.winner = "white" if self.current_turn == 0 else "black"
                game.change_state(GameOverState())
                return

        # Move the piece
        self.selected_piece.move_to(target_location)

        # Switch turns
        self.current_turn = 1 if self.current_turn == 0 else 0
        self.selected_piece = None
        self.valid_moves = []

    def handle_key(self, game, key):
        """
        Handle keyboard input during gameplay
        
        Args:
            game: Game instance
            key: Key code that was pressed
        """
        # No keyboard handling needed during normal gameplay
        pass

    def update(self, game):
        """
        Update game state during gameplay
        
        Args:
            game: Game instance
        """
        # Check if king is in check
        king_in_check = game.check_for_check(game.board)
        if king_in_check is not None:
            if king_in_check.color == self.current_player_color:
                game.check_color = self.check_color
            else:
                game.check_color = None
        else:
            game.check_color = None

    def render(self, game):
        """
        Render the game during gameplay
        
        Args:
            game: Game instance
        """
        # Draw the board with current turn indicator
        game.drawer.draw_board(self.current_turn)
        game.drawer.draw_pieces(game.board, self.current_turn,
                                self.selected_piece)
        game.drawer.draw_captured(game.board)

        # Draw check indication if needed
        if game.check_color:
            kings = [p for p in game.board.pieces if isinstance(p, King)]
            for king in kings:
                if king.color == self.current_player_color:
                    game.drawer.draw_check(king.location, game.check_color)

        # Draw valid moves for selected piece
        if self.selected_piece:
            game.drawer.draw_valid(self.valid_moves, self.current_turn)

    @property
    def name(self):
        """
        Get the name of this state
        
        Returns:
            String "PLAYING"
        """
        return "PLAYING"
