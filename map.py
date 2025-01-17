import pygame

class Map:
    def __init__(self, map_data, tile_size, tile_set):
        self.map_data = map_data
        self.tile_size = tile_size
        self.tile_set = tile_set
    
    def render(self, screen):
        pass

    
    #Screen setup
    screen_width, screen_height = 400, 400
    screen = pygame.display.set_mode((screen_width, screen_height))
    pygame.display.set_caption("Pygame Map Example")


    #Load tileset, replace with actual sprites
    floor_tile = pygame.Surface((40, 40))
    floor_tile.fill("green")
    wall_tile = pygame.Surface((40, 40))
    wall_tile.fill("black")

    #Mock testing map
    map_data = [
        [1, 1, 1, 1, 1],
        [1, 0, 0, 0, 1],
        [1, 0, 2, 0, 1],
        [1, 1, 1, 1, 1],
    ]

    #game_map = Map(map_data, (40, 40), tile_set)


    tile_set = {
        0: floor_tile,
        1: wall_tile
    }

