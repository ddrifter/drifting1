"""
Defines the class Platform for all platforms (which can be child-classes
of the class Platform)
"""
import pygame
from pygame.sprite import Sprite

class Platform(Sprite):

    def __init__(self, screen, setx, sety):
        """Initializes a basic platform."""
        super(Platform, self).__init__()
        self.image = pygame.image.load('images/basic_platform.bmp')
        self.rect = self.image.get_rect()
        self.screen = screen

        # Sets the platform's position with the values provided when making an object
        self.rect.x = setx
        self.rect.y = sety

    def blitme(self):
        """Draw the latest image."""
        self.screen.blit(self.image, self.rect)
