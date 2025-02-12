import pygame

class Bullet:

    def __init__(self, x, y, speed, image_path):
        self.x = x
        self.y = y
        self.speed = speed
        self.image = image_path
        self.rect = self.image.get_rect(topleft =(self.x, self.y))

    def move(self):
        pass
    
    def draw(self, screen):
        screen.blit(self.image,(self.x, self.y))