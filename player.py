import pygame
from bullet import Bullet
class Player:

    #constructor
    def __init__(self, x, y, speed, image_path, bullet_image):
        self.x = x
        self.y = y
        self.speed = speed
        self.image = pygame.image.load(image_path)
        self.rect = self.image.get_rect(topleft =(self.x, self.y))
        #self.bullet_image = bullet_image
        self.bullets = []


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
    
    def shoot(self):
        mouse_x, mouse_y = pygame.mouse.get_pos()  # Get cursor position
        bullet = Bullet(self.x + self.rect.width // 2, self.y, mouse_x, mouse_y, speed=10, image=self.bullet_image)
        self.bullets.append(bullet)

    def draw(self, screen):
        screen.blit(self.image,(self.x, self.y))
        for bullet in self.bullets:
            bullet.draw(screen)