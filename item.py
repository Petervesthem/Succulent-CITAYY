import pygame
from abc import ABC, abstractmethod

class Item:
    def __init__(self, x, y, name, desc, image_path):
        pass

    def draw(self, screen):
        pass

    @abstractmethod
    def use(self, player):
        #This should be overwriteen by subclasses.
        raise NotImplementedError("")
    
