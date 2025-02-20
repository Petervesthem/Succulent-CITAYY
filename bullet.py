import pygame

class Bullet:

    def __init__(self, x, y, target_x, target_y, speed, image_path):
        self.x = x
        self.y = y
        self.speed = speed
        self.image = image_path
        self.rect = self.image.get_rect(topleft =(self.x, self.y))

        target = pygame.Vector2(target_x, target_y)
        pos = pygame.Vector2(self.x,self.y)
        self.speed = (target - pos).normalize() * speed

    def move(self):
        pos = pygame.Vector2(self.x,self.y)
        pos += self.speed
        self.rect.center = pos

    def draw(self, screen):
        screen.blit(self.image,(self.x, self.y))