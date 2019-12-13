"""Defines the Enemy superclass and Enemy subclasses."""
import time

import pygame
from pygame.sprite import Sprite

class Enemy(Sprite):
    """Superclass Enemy with its variables and methods."""

    def __init__(self, settings):
        """Initializes the stats of the enemy."""
        super(Enemy, self).__init__()
        #self.max_health = settings.enemy_max_health
        #self.health = self.max_health
        self.image = pygame.image.load("images/enemy1.bmp")