import pygame
class Player(pygame.sprite.Sprite):

    #constructor
    def __init__(self, height, width, color):
        pygame.sprite.Sprite.__init__(self)

        self.image = pygame.Surface([height, width])
        self.image.fill(color)

        #update positions by setting x and y values for the rect
        self.rect = self.image.get_rect()
