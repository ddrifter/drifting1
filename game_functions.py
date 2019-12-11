"""
All major game functions for checking events, drawing on screen,
checking for collisions, etc.
"""
import sys

import pygame

def check_keydown_events(event, player, platforms, settings):
    if event.key == pygame.K_q:
        sys.exit()
    if event.key == pygame.K_LEFT:
        # Set the flag moving_left true
        player.moving_left = True
    if event.key == pygame.K_RIGHT:
        # Set the flag moving_right true
        player.moving_right = True
    if event.key == pygame.K_SPACE:
        for platform in platforms:
            # Check if the player is on the bottom of the screen
            # OR if the player has the requirement of being on top of a platform
            # AND within the x-region of the specific platform
            if (abs(player.rect.bottom - settings.sheight) < 3 or 
                (abs(player.rect.bottom - platform.rect.top) < 2 and 
                (player.rect.right > platform.rect.left or player.rect.left < platform.rect.right))):
                player.jumped = True

def check_keyup_events(event, player):
    if event.key == pygame.K_LEFT:
        # Stop moving left
        player.moving_left = False
    if event.key == pygame.K_RIGHT:
        # Stop moving right
        player.moving_right = False

def check_events(player, platforms, settings):
    """Checks for all keypresses and relegates to other more specific functions."""
    for e in pygame.event.get():
        if e.type == pygame.KEYDOWN:
            check_keydown_events(e, player, platforms, settings)
        if e.type == pygame.KEYUP:
            check_keyup_events(e, player)
        if e.type == pygame.QUIT:
            sys.exit()

def update_screen(screen, sett, player, platforms):
    """
    Update the position of all the elements on screen.
    Update the screen with every new frame, draw all the elements on screen.
    *Pay attention to the order of drawing of each element.
    """
    screen.fill(sett.bg_color)

    player.update_moving()
    player.player_gravity(platforms, sett)

    if player.jumped:
        player.jump(platforms, sett)

    # Draw all platforms
    for platform in platforms:
        platform.blitme()

    player.blitme()

    pygame.display.flip()
