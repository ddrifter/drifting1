"""Main program file for the game, contains calls to all major functions."""
import pygame
from pygame.sprite import Group

from settings import Settings
from player import Player
from platforms import Platform
import game_functions as gf
from stats import GameStats
from player_attack import PlayerFistAttackRight, PlayerFistAttackLeft

def run_game():
    """
    Initialize pygame, make player and platform objects, and run the game loop.
    """
    pygame.init()
    sett = Settings()
    stats = GameStats(sett)
    screen = pygame.display.set_mode((sett.swidth, sett.sheight))
    pygame.display.set_caption("Arena-brawler Roguelike")
    
    player = Player(screen, sett)
    platforms = Group()
    enemies = Group()
    player_attack_right = PlayerFistAttackRight(player, screen)
    player_attack_left = PlayerFistAttackLeft(player, screen)

    platform_1 = Platform(screen, 100, sett.sheight - 200)
    platform_2 = Platform(screen, sett.swidth - platform_1.rect.width - 100, 
                            sett.sheight - 200)
    platform_3 = Platform(screen, (sett.swidth/2) - (platform_1.rect.width/2), 
                            sett.sheight - 400)
    
    # Add platform_x to platforms
    platforms.add(platform_1)
    platforms.add(platform_2)
    platforms.add(platform_3)

    enemy_counter = sett.enemy_counter
    enemy_counter_threshold = sett.enemy_counter_threshold

    while True: 
        # Game loop.
        enemy_counter += 1
        player.player_gravity(platforms, sett, player)
        gf.check_events(player, platforms, sett, player_attack_left, player_attack_right)
        gf.update_screen(screen, sett, player, platforms, enemies, enemy_counter, enemy_counter_threshold,
                            stats, player_attack_left, player_attack_right)
        if enemy_counter == enemy_counter_threshold:
            enemy_counter = sett.enemy_counter

run_game()
