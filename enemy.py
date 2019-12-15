"""Defines the Enemy superclass and Enemy subclasses."""
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
        self.health = self.max_health
        self.speed = settings.enemy_speed
        self.speed_multiplier = settings.enemy_speed_multiplier

        # Calculate the enemies x and y coordinates based on the screen dimensions and player position
        self.coords = []
        self.coords = self.get_rect_x_y(settings, player)

        self.rect.x = self.coords[0]
        self.rect.y = self.coords[1]

    def get_rect_x_y(self, settings, player):
        """Calculates the x coordinate of the enemy based on player coords and screen dimensions."""
        # Put a value on player_alien_dist so the while loop starts 
        player_enemy_dist = settings.enemy_level_1_dist_from_player - 1
        coords = []

        while player_enemy_dist < settings.enemy_level_1_dist_from_player:
            # Take any x from the screen
            possible_x = randint(0, self.screen_rect.width)
            # Take any y from the screen
            possible_y = randint(0, self.screen_rect.height)

            #print(possible_x, possible_y)
            # The distance between the player and the enemy is equal to the square root of 
            # player x coord minus enemy x coords, all squared, and added to the 
            # player y coord minus enemy y coord, all squared.
            player_enemy_dist = sqrt((player.x-possible_x)**2 + (player.y-possible_y)**2)
            if player_enemy_dist > settings.enemy_level_1_dist_from_player:
                coords.append(possible_x)
                coords.append(possible_y)
                print(coords[0], coords[1])
                return coords

    def blitme(self):
        """A function for drawing the enemy on screen."""
        self.screen.blit(self.image, self.rect)
