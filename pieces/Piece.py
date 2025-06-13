from abc import ABC, abstractmethod


class Piece(ABC):
    def __init__(self, location, color):
        self.location = location
        self.color = color

    def move_to(self, location):
        self.location = location

    @abstractmethod
    def check_options(self, board):
        pass
