"""Main program file for the game, contains calls to all major functions."""

import pygame

from settings import Settings
from player import Player
import game_functions as gf

def run_game():
    pygame.init()
    sett = Settings()
    screen = pygame.display.set_mode((sett.swidth, sett.sheight))
    pygame.display.set_caption("Arena-brawler Roguelike")
    
    player = Player(screen)

    while True: 
        # Game loop.
        gf.update_screen(screen, sett, player)


run_game()
