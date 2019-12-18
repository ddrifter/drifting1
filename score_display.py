"""Contains the class that displays the score."""
import pygame.font

class ScoreDisplay():
    """A class for rendering and displaying the current score."""
    def __init__(self, screen, score):
        self.screen = screen
        self.screen_rect = self.screen.get_rect()

        self.font_color = (150, 20, 20)
        self.width, self.height = 200, 60
        self.font = pygame.font.SysFont(None, 60)
        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.background_color = (255, 255, 255)

        self.rect.top = self.screen_rect.top + 15
        self.rect.centerx = self.screen_rect.centerx

        self.render_score(score)

    def render_score(self, score):
        """Renders the current score."""
        score = str(score)
        self.msg_image = self.font.render(score, True, self.font_color, self.background_color)
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = self.rect.center

    def blitme(self):
        self.screen.fill(self.background_color, self.rect)
        self.screen.blit(self.msg_image, self.msg_image_rect)