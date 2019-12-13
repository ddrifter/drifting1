"""
All major game functions for checking events, drawing on screen,
checking for collisions, etc.
"""
import sys

import pygame
import pygame.sprite
from pygame.sprite import Group

from enemy import Enemy

def check_keydown_events(event, player, platforms, settings):
    """A function handling keydown events."""
    if event.key == pygame.K_q:
        sys.exit()

    if event.key == pygame.K_LEFT:
        # Set the flag moving_left true if the player is not close to the left side of the platform
        counter = 0
        for platform in platforms:
            if (abs(player.rect.left - platform.rect.right) < 4 and player.rect.top < platform.rect.bottom
                and player.rect.bottom > platform.rect.bottom):
                player.moving_left = False
                counter += 1
        # If there are no instances of the player being too close to the left side of the platform
        # then the player can move to the left
        if counter == 0:
            player.moving_left = True

    if event.key == pygame.K_RIGHT:
        # Set the flag moving_right true if the player is not close to the left side of the platform
        counter = 0
        for platform in platforms:
            if (abs(player.rect.right - platform.rect.left) < 4 and player.rect.top < platform.rect.bottom
                and player.rect.bottom > platform.rect.bottom):
                player.moving_right = False
                counter += 1
        # If there are no instances of the player being too close to the right side of the platform
        # then the player can move to the right
        if counter == 0:
            player.moving_right = True

    if event.key == pygame.K_SPACE:
        for platform in platforms:
            # Check if the player is on the bottom of the screen
            # OR if the player has the requirement of being on top of a platform
            if (abs(player.rect.bottom - settings.sheight) < 3 or abs(player.rect.bottom - platform.rect.top) < 2):
                player.jumped = True

    if event.key == pygame.K_DOWN:
        # Checks if the player is on a platform and starts falling to a lower level
        if player.on_top > 0:
            player.downward = True
            player.effect_of_gravity()
            
def check_keyup_events(event, player):
    """A function handling keyup events."""
    if event.key == pygame.K_LEFT:
        # Stop moving left
        player.moving_left = False
    if event.key == pygame.K_RIGHT:
        # Stop moving right
        player.moving_right = False
    if event.key == pygame.K_DOWN:
        # Resets the downward flag
        player.downward = False

def check_events(player, platforms, settings):
    """Checks for all keypresses and relegates to other more specific functions."""
    for e in pygame.event.get():
        if e.type == pygame.KEYDOWN:
            check_keydown_events(e, player, platforms, settings)
        if e.type == pygame.KEYUP:
            check_keyup_events(e, player)
        if e.type == pygame.QUIT:
            sys.exit()

def add_enemy(screen, player, sett):
    """Adds an enemy when the requirements are fullfiled."""
    enemies = Group()
    enemy = Enemy(sett)
    enemies.add(enemy)

def update_screen(screen, sett, player, platforms):
    """
    Update the position of all the elements on screen.
    Update the screen with every new frame, draw all the elements on screen.
    *Pay attention to the order of drawing of each element.
    """
    screen.fill(sett.bg_color)

    player.update_moving()

    if player.jumped:
        player.jump(platforms, sett)

    # Draw all platforms
    for platform in platforms:
        platform.blitme()

    player.blitme()

    pygame.display.flip()
