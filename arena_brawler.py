"""Main program file for the game, contains calls to all major functions."""
import time

import pygame
from pygame.sprite import Group

from settings import Settings
from player import Player
from platforms import Platform
import game_functions as gf

def run_game():
    """
    Initialize pygame, make player and platform objects, and run the game loop.
    """
    pygame.init()
    sett = Settings()
    screen = pygame.display.set_mode((sett.swidth, sett.sheight))
    pygame.display.set_caption("Arena-brawler Roguelike")
    
    player = Player(screen, sett)
    platforms = Group()
    # Platform(screen, x, y)
    platform_1 = Platform(screen, 100, sett.sheight - 200)
    platform_2 = Platform(screen, sett.swidth - platform_1.rect.width - 100, 
                            sett.sheight - 200)
    platform_3 = Platform(screen, (sett.swidth/2) - (platform_1.rect.width/2), 
                            sett.sheight - 400)
    
    # Add platform_x to platforms
    platforms.add(platform_1)
    platforms.add(platform_2)
    platforms.add(platform_3)

    while True: 
        # Game loop.
        player.player_gravity(platforms, sett, player)
        gf.check_events(player, platforms, sett)
        gf.update_screen(screen, sett, player, platforms)
        gf.add_enemy(screen, player, sett)

run_game()
