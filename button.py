"""Contains the StartButton class used for generating and drawing the start button."""
import pygame.font
from pygame.sprite import Sprite

class StartButton(Sprite):
    """A class for the start button."""
    def __init__(self, screen, msg):
        """Initializes the properties of the start button."""
        super(StartButton, self).__init__()
        self.screen = screen
        self.screen_rect = self.screen.get_rect()

        self.width, self.height = 300, 100
        self.button_color = (0, 0, 0)
        self.font_color = (200, 0, 0)
        self.font = pygame.font.SysFont(None, 45)

        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect.center = self.screen_rect.center

        self.prep_msg(msg)

    def prep_msg(self, msg):
        """'Start' message turns into a rendered image."""
        self.msg_image = self.font.render(msg, True, self.font_color, self.button_color)
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = self.rect.center

    def draw_button(self):
        """Draws the button."""
        self.screen.fill(self.button_color, self.rect)
        self.screen.blit(self.msg_image, self.msg_image_rect)