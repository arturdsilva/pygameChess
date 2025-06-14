from abc import ABC, abstractmethod


class AbstractGameState(ABC):
    """
    Abstract base class for game states.
    Implements the State pattern to encapsulate state-specific behavior.
    """

    @abstractmethod
    def handle_click(self, game, click_location):
        """
        Handle mouse click event based on the current state
        
        Args:
            game: Game instance
            click_location: Tuple (x, y) representing board coordinates of the click
        """
        pass

    @abstractmethod
    def handle_key(self, game, key):
        """
        Handle keyboard event based on the current state
        
        Args:
            game: Game instance
            key: Key code that was pressed
        """
        pass

    @abstractmethod
    def update(self, game):
        """
        Update the game state
        
        Args:
            game: Game instance
        """
        pass

    @abstractmethod
    def render(self, game):
        """
        Render the current state
        
        Args:
            game: Game instance
        """
        pass

    @property
    @abstractmethod
    def name(self):
        """
        Get the name of the current state
        
        Returns:
            String representing the state name
        """
        pass
