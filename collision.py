#TODO: Check if bullets collide with enemies, enemy takes damage
#Check if Player collides with enemy, then player takes damages
#Check if Player collides with items such as Coins, HealthPotions, and Armor/maybe weapons
#Check if Player collides with obstacles

from statmanager import StatManager
from player import Player
from enemy import Enemy
import pygame

class Collision:

    def check_bullet_enemy_collision(enemy,bullet):
        for bullet in Player.bullets:
            for enemy in Enemy.enemies:
                if bullet.rect.colliderect(enemy.rect):
                    enemy.statmanager.take_damage(10)
                    bullet.remove()
                    break


    def check_player_enemy_collision(enemy,player):
        for enemy in Enemy.enemes:
            player.rect.colliderect(enemy.rect)
            player.statmanager.take_damage(10)

    def check_player_item_collision(player, items):
        