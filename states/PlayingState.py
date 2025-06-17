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
        self.current_turn = Color.WHITE

    @property
    def current_player_color(self):
        """Get the color of the current player"""
        return self.current_turn

    @property
    def opponent_color(self):
        """Get the color of the opponent player"""
        return Color.BLACK if self.current_turn == Color.WHITE else Color.WHITE

    @property
    def opponent_pieces(self):
        """Get opponent's pieces based on the current turn"""
        return lambda board: (
            board.black_pieces
            if self.current_turn == Color.WHITE
            else board.white_pieces
        )

    @property
    def opponent_locations(self):
        """Get opponent's piece locations based on the current turn"""
        return lambda board: (
            board.black_locations
            if self.current_turn == Color.WHITE
            else board.white_locations
        )

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
        if click_location == (8, 8) or click_location == (9, 8):
            game.winner = "black" if self.current_turn == Color.WHITE else "white"
            game.change_state(GameOverState())
            return

        clicked_piece = game.board.get_piece_at_location(click_location)

        if clicked_piece and clicked_piece.color == self.current_player_color:
            self.selected_piece = clicked_piece
            self.valid_moves = clicked_piece.check_options(game.board)

        elif self.selected_piece and click_location in self.valid_moves:
            self._handle_move(game, click_location)

    def _handle_move(self, game, target_location):
        """
        Handle piece movement and capture logic

        Args:
            game: Game instance
            target_location: Tuple (x, y) representing the target location
        """
        opponent_locations = self.opponent_locations(game.board)
        if target_location in opponent_locations:
            captured_piece = game.board.get_piece_at_location(target_location)
            game.board.remove_piece(captured_piece)
            if isinstance(captured_piece, King):
                game.winner = "white" if self.current_turn == Color.WHITE else "black"

        self.selected_piece.move_to(target_location)

        self.current_turn = (
            Color.BLACK if self.current_turn == Color.WHITE else Color.WHITE
        )
        self.selected_piece = None
        self.valid_moves = []

        if game.winner != "":
            game.change_state(GameOverState())
            return

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
        game.drawer.draw_board(self.current_turn)
        game.drawer.draw_pieces(game.board, self.current_turn, self.selected_piece)
        game.drawer.draw_captured(game.board)

        if game.check_color:
            kings = [p for p in game.board.pieces if isinstance(p, King)]
            for king in kings:
                if king.color == self.current_player_color:
                    game.drawer.draw_check(king.location, game.check_color)

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
