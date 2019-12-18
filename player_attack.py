"""File designed to handle player (fist) attacks."""
import pygame
from pygame.sprite import Sprite

class PlayerFistAttackRight(Sprite):
    """A class designed to handle the player's fist attack."""

    def __init__(self, player, screen):
        """Initializes the image and properties of the fist."""
        super(PlayerFistAttackRight, self).__init__()
        self.image = pygame.image.load('images/fist_right.bmp')
        self.rect = self.image.get_rect()
        self.screen = screen
        
        # Position the right fist image on the right border of the player rect (on the inside,
        # of course)
        #self.rect.right = player.rect.right
        #self.rect.centery = player.rect.centery
        self.rect.right = 0
        self.rect.centery = 0

        # A flag to determine if the player is currently attacking and in which 
        # direction in order to actively change the coordinates of the fist images
        self.attack_right = False

        # A counter used for the number of "frames" in an animation
        self.counter = 0

        # Variables for increasing and decreasing the x-coord of the fist images
        self.increase = 2
        self.decrease = 2

    def blitme(self):
        """A function for drawing the right fist if the player is attacking."""
        if self.attack_right:
            self.screen.blit(self.image, self.rect)


    def player_attacked(self, player):
        """Gradually changes the coordinates of the fist to the right so as to appear as if it is moving."""
        if self.attack_right:
            if self.counter < 20:
                self.rect.right = player.rect.right + self.increase
                self.rect.centery = player.rect.centery
                self.increase += 1.2
                self.counter += 0.5
            if self.counter > 19 and self.counter < 40:
                self.rect.right = player.rect.right - self.decrease
                self.rect.centery = player.rect.centery
                self.decrease += 0.5
                self.counter += 0.5
            if self.counter > 39:
                # If this condition is satisfied then reset all the values for future use
                self.counter = 0
                self.increase = 2
                self.decrease = 2
                self.attack_right = False


class PlayerFistAttackLeft(Sprite):
    """A class designed to handle the player's fist attack."""
        
    def __init__(self, player, screen):
        """Initializes the image and properties of the fist."""
        super(PlayerFistAttackLeft, self).__init__()
        self.image = pygame.image.load('images/fist_left.bmp')
        self.rect = self.image.get_rect()
        self.screen = screen

        self.rect.left = player.rect.left
        self.rect.centery = player.rect.centery

        self.attack_left = False

        self.counter = 0
        self.increase = 2
        self.decrease = 2

    def blitme(self):
        """A function for drawing the left fist if the player is currently attacking."""
        if self.attack_left:
            self.screen.blit(self.image, self.rect)

    def player_attacked(self, player):
        """Gradually changes the coordinates of the fist to the left so as to appear as if it is moving."""
        if self.attack_left:
            if self.counter < 20:
                self.rect.left = player.rect.left - self.increase
                self.rect.centery = player.rect.centery
                self.increase += 1.2
                self.counter += 0.5
            if self.counter > 19 and self.counter < 40:
                self.rect.left = player.rect.left + self.decrease
                self.rect.centery = player.rect.centery
                self.decrease += 0.5
                self.counter += 0.5
            if self.counter > 39:
                # If this condition is satisfied then reset all the values for future use
                self.counter = 0
                self.increase = 2
                self.decrease = 2
                self.attack_left = False
                