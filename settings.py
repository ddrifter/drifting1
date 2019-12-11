"""Contains the class Settings with all of the major settings for the game."""
import pygame

class Settings():
    """Defines the class for the game's settings."""
    def __init__(self):
        """Initializes the game's settings."""
        self.swidth = 1200
        self.sheight = 800
        self.bg_color = (255, 255, 255)

        # Gravity variable and jump variable
        self.grav_var = 1.05
        self.jump_var = 3