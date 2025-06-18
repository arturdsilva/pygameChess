# two player chess in python with Pygame!

import pygame

from Constants import Constants
from Game import Game


def main():
    """
    Main game entry point
    """
    pygame.init()
    screen = pygame.display.set_mode([Constants.WIDTH, Constants.HEIGHT])
    pygame.display.set_caption("Two-Player Pygame Chess!")
    timer = pygame.time.Clock()

    game = Game(screen)

    # Main game loop
    running = True
    while running:
        # Limit frame rate
        timer.tick(Constants.FPS)

        # Process events
        running = game.handle_events()

        # Update game state
        game.update()

        # Render
        game.render()

    pygame.quit()


if __name__ == "__main__":
    main()
