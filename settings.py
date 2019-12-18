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

        # Other player settings
        self.max_player_lives = 3

        # Enemy settings
        self.enemy_max_health = 100
        self.enemy_speed = 1.2 # Not needed
        self.enemy1_speed_multiplier = 1
        self.enemy2_speed_multiplier = 1.35
        self.enemy3_speed_multiplier = 1.7
        self.enemy_level_1_dist_from_player = 400
        self.enemy_level_2_dist_from_player = 300
        self.enemy_level_3_dist_from_player = 250
        self.enemy1_score = 10
        self.enemy2_score = 15
        self.enemy3_score = 40
        self.enemy1_score_multiplier = 1
        self.enemy2_score_multiplier = 2
        self.enemy3_score_multiplier = 3

        # Count of enemy1's for 1 enemy2
        self.enemy1_for_enemy2_thresh = 3
        self.enemy1_for_enemy2_count = 0
        self.enemy2_for_enemy3_thresh = 3
        self.enemy2_for_enemy3_count = 0

        # Enemy counter for delay in the generation of new enemies
        self.enemy_counter = 0
        self.enemy_counter_threshold = 300
        