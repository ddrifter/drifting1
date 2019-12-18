"""
All major game functions for checking events, drawing on screen,
checking for collisions, etc.
"""
import sys
import time

import pygame
import pygame.sprite

from enemy import Enemy, EnemyMovement

def check_keydown_events(event, player, platforms, settings, player_attack_left, player_attack_right):
    """A function handling keydown events."""
    if event.key == pygame.K_q:
        sys.exit()

    if event.key == pygame.K_LEFT:
        # Set the flag moving_left True 
        player.moving_left = True

    if event.key == pygame.K_RIGHT:
        # Set the flag moving_right True 
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

    if event.key == pygame.K_a:
        # Commences the player attack if the player is not already attacking
        if not player_attack_right.attack_right or not player_attack_left.attack_left:
            if player.moved_right:
                player_attack_right.attack_right = True

            elif player.moved_left:
                player_attack_left.attack_left = True

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

def check_events(player, platforms, settings, player_attack_left, player_attack_right, stats, start_button):
    """Checks for all keypresses and relegates to other more specific functions."""
    for e in pygame.event.get():
        if e.type == pygame.KEYDOWN:
            check_keydown_events(e, player, platforms, settings, player_attack_left, player_attack_right)
        if e.type == pygame.KEYUP:
            check_keyup_events(e, player)
        if e.type == pygame.QUIT:
            sys.exit()
        if e.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            check_play_button(stats, mouse_x, mouse_y, start_button)

def check_play_button(stats, mouse_x, mouse_y, start_button):
    """If the game isn't running, start."""
    mouse_button_collision = start_button.rect.collidepoint(mouse_x, mouse_y)
    if mouse_button_collision and not stats.game_active:
        stats.game_active = True
        pygame.mouse.set_visible(False)


def add_enemy(screen, player, sett, enemies, enemy_counter, enemy_counter_threshold):
    """Adds an enemy when the requirements are fullfiled."""
    if enemy_counter == enemy_counter_threshold:
        enemy = Enemy(sett, screen, player)
        enemies.add(enemy)


def update_screen(screen, sett, player, platforms, enemies, enemy_counter, enemy_counter_threshold,
                    stats, player_attack_left, player_attack_right, enemy_movement, lives, start_button):
    """
    Update the position of all the elements on screen.
    Update the screen with every new frame, draw all the elements on screen.
    *Pay attention to the order of drawing of each element.
    """
    screen.fill(sett.bg_color)

    player.update_moving(platforms)

    # Draw all platforms
    for platform in platforms:
        platform.blitme()

    # Draw the start button if the game isn't running
    if not stats.game_active:
        start_button.draw_button()
        pygame.mouse.set_visible(True)

    # Game started
    if stats.game_active:
        # Periodically adds enemies on screen
        add_enemy(screen, player, sett, enemies, enemy_counter, enemy_counter_threshold)
            
        # Perform enemy movement
        for enemy in enemies:
            enemy_movement.enemy_movement(enemy, player)

        enemies.draw(screen)
            
        # The conditions for entering into these functions are inside the player_attack_ classes
        player_attack_left.player_attacked(player)
        player_attack_right.player_attacked(player)
        player_attack_left.blitme()
        player_attack_right.blitme()

        # Since pygame's inbuilt funtions for collision detection do not work with classes that have
        # no explicitly defined (and used) rect attribute, which in this case I see as unfortunate 
        # because I can't think of a way to implement both the left and the right fist attack in the same
        # class using a single rect, so now there are two classes> PlayerFistAttackRight and PlayerFistAttackLeft
        # (both have explicitly defined rect, for future use)
        enemy_left = None
        enemy_right = None
        if player_attack_left.attack_left == True or player_attack_right.attack_right == True:
            enemy_left = pygame.sprite.spritecollideany(player_attack_left, enemies)
            enemy_right = pygame.sprite.spritecollideany(player_attack_right, enemies)
        if enemy_left:
            stats.score += enemy_left.total_score
            print(stats.score)
            enemies.remove(enemy_left)
        if enemy_right:
            stats.score += enemy_right.total_score
            print(stats.score)
            enemies.remove(enemy_right)

        if pygame.sprite.spritecollideany(player, enemies):
            stats.lives_left -= 1
            for enemy in enemies:
                enemies.remove(enemy)
            if stats.lives_left == 0:
                stats.game_active = False
                stats.reset_stats(sett)

        # Draws thumbnails for players lives
        lives.blitme(stats)

        if player.jumped:
            player.jump(platforms, sett)

    player.blitme()

    pygame.display.flip()
