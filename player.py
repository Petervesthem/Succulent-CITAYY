import pygame
from bullet import Bullet
from statmanager import StatManager
class Player:

    #constructor
    def __init__(self, x, y, image_path):
        self.x = x
        self.y = y
        self.stat = StatManager(100, 5, 5)
        self.image = pygame.image.load(image_path)
        self.rect = self.image.get_rect(topleft =(self.x, self.y))
        self.bullets = []


    def move (self,keys):
        if keys[pygame.K_a]:
            self.x -= self.stat.speed
        if keys[pygame.K_d]:
            self.x += self.stat.speed
        if keys[pygame.K_w]:
            self.y -= self.stat.speed
        if keys[pygame.K_s]:
            self.y += self.stat.speed

        #updating the collision rectangle
        self.rect.topleft = (self.x, self.y)
    
    def shoot(self, bullets):
        mouse_x, mouse_y = pygame.mouse.get_pos()  # Get cursor position
        bullet_image=pygame.image.load("assets/dummy_textures/bullet.png")
        bullet = Bullet(x=self.x + self.rect.width // 2,
                        y=self.y,
                        target_x=mouse_x,
                        target_y=mouse_y,
                        speed=10,
                        image_path=bullet_image)
        bullets.append(bullet)
    

    def pickUp(self, item):
        pass

    def draw(self, screen):
        screen.blit(self.image,(self.x, self.y))
        for bullet in self.bullets:
            bullet.draw(screen)