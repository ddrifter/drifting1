"""Class Player with it's properties and functions."""
import pygame
from pygame.sprite import Sprite

class Player(Sprite):
    """Defines the class Player with the player's properties."""
    
    def __init__(self, screen, settings):
        """Initializes the player's properties."""
        super(Player, self).__init__()
        self.image_left = pygame.image.load("images/player_left.bmp")
        self.image_right = pygame.image.load("images/player_right.bmp")
        self.image_damaged_left = pygame.image.load("images/player_lost_life_left.png")
        self.image_damaged_right = pygame.image.load("images/player_lost_life_right.png")

        self.rect = self.image_left.get_rect()
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
        self.moving_left_counter = settings.moving_left_counter
        self.moving_right_counter = settings.moving_right_counter
        self.staying_still = True
        self.jumped = False

        # Flags for determining which player image will be displayed
        # (in the beginning it's the 'right' image)
        self.moved_right = True
        self.moved_left = False

        # Gravity constant and variable, with the jump variable from settings and other 
        # variables that help with jumping constrainst and gravity constrainst
        self.grav_var = settings.grav_var
        self.grav_const = settings.grav_const
        self.jump_var = settings.jump_var
        self.under_var = settings.under_var
        self.on_top = settings.on_top
        self.downward = False

        # Flags for drawing the images of the damaged player
        self.been_damaged_right = False
        self.been_damaged_left = False
        self.damaged_counter = 0
        self.damaged_counter_threshold = 400

    def update_moving(self, platforms):
        """
        Updates the player's position based on the flags moving_left and moving_right and sets the
        moved_left and moved_right flags. Also checks if the player is near any side of any platform 
        and (hopefully) stops movement to that side while the circumstances remain.
        """
        # Set the counters to 0 so they can be increased if the player is near the side of a platform
        self.moving_left_counter = 0
        self.moving_right_counter = 0

        if self.moving_left and self.rect.left > 0:
            for platform in platforms:
                if (abs(self.rect.left - platform.rect.right) < 4 and self.rect.top < platform.rect.bottom
                    and self.rect.bottom > platform.rect.top):
                    # Increase the counter if the player is within the boundaries of the right
                    # side of any platform
                    self.moving_left_counter += 1

            if self.moving_left_counter == 0:   
                if self.damaged_counter > 0:
                    self.x -= 0.9
                    self.rect.x = self.x
                else:     
                    self.x -= 1.5
                    self.rect.x = self.x
            
            # Flags for determining which player image will be displayed
            self.moved_right = False
            self.moved_left = True 

        if self.moving_right and self.rect.right < self.screen_rect.right:
            for platform in platforms:
                if (abs(self.rect.right - platform.rect.left) < 4 and self.rect.top < platform.rect.bottom
                    and self.rect.bottom > platform.rect.bottom):
                    # Increase the counter if the player is within the boundaries of the left
                    # side of any platform
                    self.moving_right_counter += 1
            
            if self.moving_right_counter == 0:
                # If the player lost a life recently -> apply a slowdown
                if self.damaged_counter > 0:
                    self.x += 0.9
                    self.rect.x = self.x
                else:
                    self.x += 1.5
                    self.rect.x = self.x  

             # Flags for determining which player image will be displayed
            self.moved_left = False
            self.moved_right = True 

    def player_gravity(self, platforms, settings, player):
        """Makes the player succeptible to gravitational influence."""
        self.on_top = settings.on_top

        if self.rect.bottom < self.screen_rect.bottom:
            for platform in platforms:
                # Check if the player is in on top of any platform, and, if so, 
                # adjust parameters accordingly so the player can land/stand on the platform
                # > if the downward flag is True then dont go into the conditional and just proceed to
                # > gravity calculations
                if ((abs(self.rect.bottom - platform.rect.top) < 2) and (self.rect.right > platform.rect.left)
                    and (self.rect.left < platform.rect.right) and not self.downward):
                    self.grav_var = settings.grav_var
                    self.jump_var = settings.jump_var
                    self.jumped = False
                    self.on_top += 1
            
            # Performs the gravity calculations if the player is not ontop of a platform
            if self.on_top == 0:
                self.effect_of_gravity()

            # Checks if the player is near the bottom of the screen and resets grav_var and jump_var
            # and turns jumped flag off
            if abs(self.rect.bottom - self.screen_rect.bottom) < 4:
                self.grav_var = settings.grav_var
                self.jump_var = settings.jump_var
                self.jumped = False
                self.downward = False

    def effect_of_gravity(self):
        """Effects of gravity on the player, changes the y-coordinate."""
        self.y += 0.1 + self.grav_var*self.grav_const
        self.rect.y = self.y 
        self.grav_var += 0.01 * self.grav_var   

    def jump(self, platforms, settings):
        """Function for jumping."""
        self.under_var = settings.under_var

        for platform in platforms:
            # Check, for every platform, if the player is positioned right underneath it and stop
            # jumping, reset jump_var and set jumped flag to False
            if (abs(self.rect.top - platform.rect.bottom) < 3 and self.rect.right > platform.rect.left
                and self.rect.left < platform.rect.right):
                self.jump_var = settings.jump_var
                self.jumped = False
                self.under_var += 1
        
        # If the player is not underneath any platform -> jump OR is on top of a platform
        if (self.jump_var >= -6 and self.under_var == 0) or self.on_top > 0:
            self.y -= (5 + self.jump_var) 
            self.rect.y = self.y
            self.jump_var -= 0.1     

    def reset_player(self):
        """Resets the player if he's lost a life."""
        self.rect.x = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom      
      
    def blitme(self):
        """
        Draws the player at its current location keeping in mind the last known direction
        the player was facing to have a uniform player picture displayed without unnecessary
        alteration
        """
        # Drawing the damaged player images if the counter is running
        if self.moved_right and self.damaged_counter > 0:
            self.screen.blit(self.image_damaged_right, self.rect)
        if self.moved_left and self.damaged_counter > 0:
            self.screen.blit(self.image_damaged_left, self.rect)

        # Drawing the usual player images
        if self.moved_right and self.damaged_counter == 0:
            self.screen.blit(self.image_right, self.rect)
        elif self.moved_left and self.damaged_counter == 0:
            self.screen.blit(self.image_left, self.rect)

class PlayerLives(Sprite):
    """A class for drawing thumbnails of player lives."""
    def __init__(self, screen):
        """Initializes with 3 thumbnails."""
        self.screen = screen
        self.image_3_lives = pygame.image.load("images/player_life_3.png")
        self.image_2_lives = pygame.image.load("images/player_life_2.png")
        self.image_1_lives = pygame.image.load("images/player_life_1.png")

        self.rect_3 = self.image_3_lives.get_rect()
        self.rect_2 = self.image_2_lives.get_rect()
        self.rect_1 = self.image_1_lives.get_rect()

        self.rect_1.y = 20
        self.rect_1.x = 20
        self.rect_2.y = 20
        self.rect_2.x = self.rect_3.width + 40
        self.rect_3.y = 20
        self.rect_3.x = self.rect_3.width + self.rect_2.width + 60
        
    def blitme(self, stats):
        """Draws the current number of lives."""
        if stats.lives_left >= 1:
            self.screen.blit(self.image_1_lives, self.rect_1)
        if stats.lives_left >= 2:
            self.screen.blit(self.image_2_lives, self.rect_2)
        if stats.lives_left == 3:
            self.screen.blit(self.image_3_lives, self.rect_3)

