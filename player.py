"""Class Player with it's properties and functions."""
import pygame
from pygame.sprite import Sprite

class Player(Sprite):
    """Defines the class Player with the player's propertes."""
    
    def __init__(self, screen, settings):
        """Initializes the player's properties."""
        super(Player, self).__init__()
        self.image = pygame.image.load("images/player.bmp")
        self.rect = self.image.get_rect()
        self.screen = screen
        self.screen_rect = self.screen.get_rect()

        # Center the player in the middle bottom position of the screen
        self.rect.bottom = self.screen_rect.bottom
        self.rect.centerx = self.screen_rect.centerx

        # Set a custom marker for finer speed adjustments later on 
        self.x = self.rect.x
        self.y = self.rect.y

        # Flags for moving and jumping
        self.moving_left = False
        self.moving_right = False
        self.jumped = False

        # Gravity constant and variable, with the jump variable from settings
        self.grav_var = settings.grav_var
        self.grav_const = settings.grav_const
        self.jump_var = settings.jump_var

    def update_moving(self):
        """Updates the player's position based on the flags moving_left and moving_right."""
        if self.moving_left and self.rect.left > 0:
            self.x -= 1.5
            self.rect.x = self.x
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += 1.5
            self.rect.x = self.x  

    def player_gravity(self, platforms, settings):
        """Makes the player succeptible to gravitational influence."""
        if self.rect.bottom < self.screen_rect.bottom:
            for platform in platforms:
                # Check if the player is in on top (needs fixing) of any platform, and, if so, 
                # adjust parameters accordingly so the player can land/stand on the platform
                if ((abs(self.rect.bottom - platform.rect.top) < 3) and (self.rect.right > platform.rect.left)
                    and (self.rect.left < platform.rect.right)):
                        self.grav_var = settings.grav_var
                        self.jump_var = settings.jump_var
                        self.jumped = False

            # Performs the gravity calculations
            self.y += 0.1 + self.grav_var*self.grav_const
            self.rect.y = self.y 
            self.grav_var += 0.008 * self.grav_const

            # Checks if the player is near the bottom of the screen and turns gravity and jumped flag off
            if abs(self.rect.bottom - self.screen_rect.bottom) < 4:
                self.grav_var = settings.grav_var
                self.jump_var = settings.jump_var
                self.jumped = False

    def jump(self, platforms, settings):
        """Function for jumping."""
        for platform in platforms:
            # Check, for every platform, if the player is positioned right underneath it and stop
            # jumping, reset jump_var and set jumped flag to False
            if (abs(self.rect.top - platform.rect.bottom) < 3 and self.rect.right > platform.rect.left
                and self.rect.left < platform.rect.right):
                self.jump_var = settings.jump_var
                self.jumped = False
                break
        
        if self.jump_var > -5:
            self.y -= (5 + self.jump_var) 
            self.rect.y = self.y
            self.jump_var -= 0.1           
            print(self.jump_var)  

    def blitme(self):
        """Draws the player at its current location."""
        self.screen.blit(self.image, self.rect)