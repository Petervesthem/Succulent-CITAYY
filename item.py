import pygame
from abc import ABC, abstractmethod

class Item:
    def __init__(self, x, y, name, desc, image_path):
        self.x = x
        self.y = y
        self.name = name
        self.desc = desc
        self.image_path = pygame.image.load(image_path)

    def draw(self, screen):
        screen.blit(self.image_path,(self.x, self.y))

    @abstractmethod
    def use(self, player):
        #This should be overwriteen by subclasses.
        raise NotImplementedError("")
    
