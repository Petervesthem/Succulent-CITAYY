import pygame
import map
from player import Player
from enemy import Enemy
from bullet import Bullet
from healthpot import HealthPotion
from coin import Coin
import random

# pygame setup
pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True
dt = 0

#player_pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)
player_posx = screen.get_width()/2
player_posy = screen.get_height()/2
bullets = []

player = Player(x=player_posx, y=player_posy,image_path="assets/dummy_textures/mockplayer.png")
healthpot = HealthPotion(x=random.randint(1,1280), y=random.randint(1,720),name= "Health Potion", 
                         desc="Heals for 20HP", image_path="assets/dummy_textures/healthpot.png")

#TODO: In the future Items in general should be randomly spawn not just one coin one healthpot
coin = Coin(x=random.randint(1,1280), y=random.randint(1,720), name="Coin", desc="great value", image_path="assets/dummy_textures/coin.png")
#enemy = Enemy(x=player_posx, y=player_posy,speed=5, image_path="assets/dummy_textures/mockenemy.png")

enemyCount = 5
enemyList = [] 
for i in range(enemyCount):
    enemies = Enemy(x=random.randint(1,1280), y=random.randint(1,720),speed=5, attack_power=5, health=20, image_path="assets/dummy_textures/mockenemy.png")
    enemyList.append(enemies)

    

while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            player.shoot(bullets)
        

    # fill the screen with a color to wipe away anything from last frame
    screen.fill("green")


    pygame.sprite
    #pygame.draw.circle(screen, "red", player_pos, 40)



    keys = pygame.key.get_pressed()
    player.move(keys)

    for bullet in bullets[:]:
        bullet.move()
        bullet.draw(screen)
        #Checking if out of bounds --> screen
        if not screen.get_rect().colliderect(bullet.rect):
            bullets.remove(bullet)
            
    


    player.draw(screen)
    healthpot.draw(screen)
    coin.draw(screen)

   
    for enemy in enemyList:
        enemy.draw(screen)
    

    # flip() the display to put your work on screen
    pygame.display.flip()

    # limits FPS to 60
    # dt is delta time in seconds since last frame, used for framerate-
    # independent physics.
    dt = clock.tick(60) / 1000

pygame.quit()