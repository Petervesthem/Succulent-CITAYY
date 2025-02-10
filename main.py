import pygame
import map
from player import Player
from enemy import Enemy
# pygame setup
pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True
dt = 0

#player_pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)
player_posx = screen.get_width()/2
player_posy = screen.get_height()/2

player = Player(x=player_posx, y=player_posy,speed=5, image_path="assets/dummy_textures/knight.png")
enemy = Enemy(x=player_posx, y=player_posy,speed=5, image_path="assets/dummy_textures/orc.png")

while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # fill the screen with a color to wipe away anything from last frame
    screen.fill("red")


    pygame.sprite
    #pygame.draw.circle(screen, "red", player_pos, 40)

    keys = pygame.key.get_pressed()
    player.move(keys)
    player.draw(screen)

    enemy.draw(screen)
    

    # flip() the display to put your work on screen
    pygame.display.flip()

    # limits FPS to 60
    # dt is delta time in seconds since last frame, used for framerate-
    # independent physics.
    dt = clock.tick(60) / 1000

pygame.quit()