import pygame
from pygame.sprite import Sprite

class Player():
    """Defines the class player with the player's propertes."""
    
    def __init__(self, screen):
        """Initializes the player's properties."""
        self.image = pygame.image.load("images/player.bmp")
        self.rect = self.image.get_rect()
        self.screen = screen
        self.screen_rect = self.screen.get_rect()

        self.rect.bottom = self.screen_rect.bottom
        self.rect.centerx = self.screen_rect.centerx

    def blitme(self):
        """Draws the player at its current location."""
        self.screen.blit(self.image, self.rect)