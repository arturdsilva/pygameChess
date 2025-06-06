import pygame


def load_fonts():
    return {
        "default": pygame.font.Font("freesansbold.ttf", 20),
        "medium": pygame.font.Font("freesansbold.ttf", 40),
        "big": pygame.font.Font("freesansbold.ttf", 50),
    }
