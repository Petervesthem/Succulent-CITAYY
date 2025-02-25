import pygame
from statmanager import StatManager
from coin import Coin
from healthpot import HealthPotion
from armor import Armor
from item import Item

class GameManager:
    def __init__(self):
        self.items = pygame.sprite.Group()
        self.enemies = pygame.sprite.Group()
        self.bullets = pygame.sprite.Group()
        self.obstacles = pygame.sprite.Group

        self.items.add(Coin(100,200), HealthPotion(300,400), Armor(500,600))
    
    def check_collisions(self):
        self.check_player_item_collision()
    
    def check_player_item_collision(self):
        collided_items = pygame.sprite.spritecollide(self.player, self.items, True)

        for item in collided_items:
            if isinstance(item, Coin):
                break
            if isinstance(item,HealthPotion):
                pass
            if isinstance(item, Armor):
                pass

    def update(self):
        ###Updating all the game objects
        self.check_collisions()
        self.items.update()
        self.enemies.update()
        self.bullets.update()
    

    def draw(self,screen):
        ###Drawing all the game objects
        screen.fill((0,0,0))#will later be map drawn here
        self.items.draw(screen)
        self.enemies.draw(screen)
        self.bullets.draw(screen)
        pygame.display.flip()


