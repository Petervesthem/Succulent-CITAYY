import pygame
class Enemy:

   #constructor
    def __init__(self, x, y, speed, image_path):
        self.x = x
        self.y = y
        self.speed = speed
        self.image = pygame.image.load(image_path)
        self.rect = self.image.get_rect(topleft =(self.x, self.y))

    #should implement following/tracing the player
    def move (self):
        pass

        #updating the collision rectangle
        self.rect.topleft = (self.x, self.y)

    def draw(self, screen):
        screen.blit(self.image,(self.x, self.y))

