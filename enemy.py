"""Defines the Enemy superclass."""
from math import sqrt
from random import randint

import pygame
from pygame.sprite import Sprite

class Enemy(Sprite):
    """Superclass Enemy with its variables and methods."""

    def __init__(self, settings, screen, player):
        """Initializes the stats of the enemy."""
        super(Enemy, self).__init__()
        self.image = pygame.image.load("images/enemy1.bmp")
        self.rect = self.image.get_rect()
        self.screen = screen
        self.screen_rect = self.screen.get_rect()

        # Enemy stats
        self.max_health = settings.enemy_max_health
        self.curr_health = self.max_health
        self.speed_multiplier = settings.enemy_speed_multiplier
        self.score = settings.enemy_score
        self.score_multiplier = settings.enemy_score_multiplier
        self.total_score = self.score * self.score_multiplier

        # Calculate the enemies x and y coordinates based on the screen dimensions and player position
        self.coords = []
        self.coords = self.get_rect_x_y(settings, player)

        self.rect.x = self.coords[0]
        self.rect.y = self.coords[1]

        # Used for movement calculations
        self.x = self.rect.x
        self.y = self.rect.y

    def get_rect_x_y(self, settings, player):
        """Calculates the x coordinate of the enemy based on player coords and screen dimensions."""
        # Put a value on player_alien_dist so the while loop can start 
        player_enemy_dist = settings.enemy_level_1_dist_from_player - 1
        coords = []

        while player_enemy_dist < settings.enemy_level_1_dist_from_player:
            # Take any x from the screen
            possible_x = randint(0, self.screen_rect.width + 200)
            # Take any y from the screen
            possible_y = randint(0, self.screen_rect.height + 200)

            # The distance between the player and the enemy is equal to the square root of 
            # player x coord minus enemy x coords, all squared, and added to the 
            # player y coord minus enemy y coord, all squared.
            player_enemy_dist = sqrt((player.x-possible_x)**2 + (player.y-possible_y)**2)
            if player_enemy_dist > settings.enemy_level_1_dist_from_player:
                coords.append(possible_x)
                coords.append(possible_y)
                return coords

    def blitme(self):
        """A function for drawing the enemy on screen."""
        self.screen.blit(self.image, self.rect)

class EnemyMovement():
    """Defines the movement of the basic enemy type."""
    def __init__(self):

        # Variables for storing distance from player
        self.dist_from_player_x = 0
        self.dist_from_player_y = 0

        # Coeficients for enemy movement
        self.x_dir_coef = 0
        self.y_dir_coef = 0

        # Variables containing movement steps based on coeficients and player-enemy distance
        self.x_move_step = 0
        self.y_move_step = 0

    def get_directions(self, player, enemy):
        """
        Determines the coeficient to multiply with the distance step in moving towards the player,
        it can be either 1, -1, or 0 (if the enemy's and the player's x or y coord are equal).
        """
        if enemy.rect.x > player.rect.x:
            self.x_dir_coef = -1
        elif enemy.rect.x < player.rect.x:
            self.x_dir_coef = 1
        elif enemy.rect.x == player.rect.x:
            self.x_dir_coef = 0

        if enemy.rect.y > player.rect.y:
            self.y_dir_coef = -1
        elif enemy.rect.y < player.rect.y:
            self.y_dir_coef = 1
        elif enemy.rect.y == player.rect.y:
            self.y_dir_coef = 0

    def enemy_movement(self, enemy, player):
        """Changes enemy coordinates based on movement coeficients and player-enemy distance."""
        # Gets movement coeficients
        self.get_directions(player, enemy)

        # Get distances of the enemy's x and y coord from the player's x and y coord
        self.dist_from_player_x = abs(enemy.rect.x - player.rect.x)
        self.dist_from_player_y = abs(enemy.rect.y - player.rect.y)

        # Define movement steps
        self.x_move_step = (self.dist_from_player_x / 400) * enemy.speed_multiplier
        self.y_move_step = (self.dist_from_player_y / 400) * enemy.speed_multiplier

        # Slightly increase the speed if the enemy is very close to the player
        if self.x_move_step < 1:
            self.x_move_step += 0.35
        if self.y_move_step < 1:
            self.y_move_step += 0.35

        enemy.x += self.x_dir_coef * self.x_move_step
        enemy.y += self.y_dir_coef * self.y_move_step
        enemy.rect.x = enemy.x
        enemy.rect.y = enemy.y



