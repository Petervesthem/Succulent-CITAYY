import pygame
class Player:

    #constructor
    def __init__(self, x, y, speed, image_path):
        self.x = x
        self.y = y
        self.speed = speed
        self.image = pygame.image.load(image_path)
        self.rect = self.image.get_rect(topleft =(self.x, self.y))


    def move (self,keys):
        if keys[pygame.K_a]:
            self.x -= self.speed
        if keys[pygame.K_d]:
            self.x += self.speed
        if keys[pygame.K_w]:
            self.y -= self.speed
        if keys[pygame.K_s]:
            self.y += self.speed

        #updating the collision rectangle
        self.rect.topleft = (self.x, self.y)

    def draw(self, screen):
        screen.blit(self.image,(self.x, self.y))