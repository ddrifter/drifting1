import pygame

def update_screen(screen, sett, player):
    """Update the screen with every new frame, draw all the elements on screen."""

    screen.fill(sett.bg_color)
    player.blitme()

    pygame.display.flip()