import pygame
from tiles import *
from player import *

class Level:
    def __init__(self,level_data,surface):
        # level setup
        self.display_surface = surface
        self.setup_level(level_data)

    def setup_level(self,layout):
        self.tiles = pygame.sprite.Group()
        self.player = pygame.sprite.GroupSingle()

        for row_index,row in enumerate(layout):
            for col_index,cell in enumerate(row):
                x = col_index * tile_size
                y = row_index * tile_size

                if cell == 'X':
                    tile = Tile((x,y),tile_size)
                    self.tiles.add(tile)
                if cell == 'B':
                    tile = Tile2((x,y),tile_size)
                    self.tiles.add(tile)
                if cell == 'P':
                    player_sprite = Player((x,y))
                    self.player.add(player_sprite)

    def run(self):

        # tile sidescrolling update
        self.tiles.update(-1)
        # tile draw
        self.tiles.draw(self.display_surface)

        # draw player
        self.player.update()
        self.player.draw(self.display_surface)