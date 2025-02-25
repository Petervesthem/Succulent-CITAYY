import pygame
from statmanager import StatManager
class Enemy:
#This Enemy class is supposed to be a more generic class, implementing more enemy types later
   #constructor
    def __init__(self, x, y, health, speed, attack_power, image_path):
        self.x = x
        self.y = y
        self.stat = StatManager(health, speed, attack_power)
        self.image = pygame.image.load(image_path)
        self.rect = self.image.get_rect(topleft =(self.x, self.y))
        self.enemies = []

    #should implement following/tracing the player
    def move (self):
        pass

        #updating the collision rectangle
        self.rect.topleft = (self.x, self.y)

    def draw(self, screen):
        screen.blit(self.image,(self.x, self.y))

