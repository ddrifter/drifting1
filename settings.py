"""Contains the class Settings with all of the major settings for the game."""
import pygame

class Settings():
    """Defines the class for the game's settings."""
    def __init__(self):
        """Initializes the game's settings."""
        self.swidth = 1200
        self.sheight = 800
        self.bg_color = (255, 255, 255)

        # Gravity variable/constant and jump variable with under_var and on_top var for checking 
        # the relations of the player and the platforms in the Player class
        self.grav_var = 0.9
        self.grav_const = 1.2
        self.jump_var = 3
        self.under_var = 0
        self.on_top = 0

        # Player counters for checking proximity to either left or right side of a platform
        self.moving_left_counter = 0
        self.moving_right_counter = 0

        # Enemy settings
        self.enemy_max_health = 100
        self.enemy_speed = 1.2
        self.enemy_speed_multiplier = 1
        self.enemy_level_1_dist_from_player = 400

        # Enemy counter for delay in the generation of new enemies
        self.enemy_counter = 0
        self.enemy_counter_threshold = 700
        