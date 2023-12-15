import pygame
from tiles import *
from player import *
from settings import *

# define level class
class Level:

    # level setup
    def __init__(self,level_data,surface):
        self.display_surface = surface
        self.setup_level(level_data)
        # set side scrolling to 0
        self.world_shift = 0

    # define placement of tiles within grid
    def setup_level(self,layout):
        self.tiles = pygame.sprite.Group()
        self.player = pygame.sprite.GroupSingle()

        # row and column system
        for row_index,row in enumerate(layout):
            for col_index,cell in enumerate(row):
                x = col_index * tile_size
                y = row_index * tile_size

                # define letter for grass block tile
                if cell == 'X':
                    tile = Tile((x,y),tile_size)
                    self.tiles.add(tile)
                # define letter for dirt block tile
                if cell == 'D':
                    tile = Tile2((x,y),tile_size)
                    self.tiles.add(tile)
                # define letter for question block tile
                if cell == 'B':
                    tile = Tile3((x,y),tile_size)
                    self.tiles.add(tile)
                # define letter for brick block tile
                if cell == 'R':
                    tile = Tile4((x,y),tile_size)
                    self.tiles.add(tile)
                # define letter for player
                if cell == 'P':
                    player_sprite = Player((x,y))
                    self.player.add(player_sprite)

    # define sidescrolling mechanics
    def scroll_x(self):
        player = self.player.sprite
        player_x = player.rect.centerx
        direction_x = player.direction.x 

        # side scroll forward
        if player_x < screen_width / 4 and direction_x < 0:
            self.world_shift = 8
            player.speed = 0
        # side scroll backward
        elif player_x > screen_width - (screen_width / 1.5) and direction_x > 0:
            self.world_shift = -8
            player.speed = 0
        # idle no scroll
        else:
            self.world_shift = 0
            player.speed = 8

    # apply tile collisions for horizontal movement 
    def horizontal_movement_collision(self):
        player = self.player.sprite
        player.rect.x += player.direction.x * player.speed

        for sprite in self.tiles.sprites():
            if sprite.rect.colliderect(player.rect):
                # collsion from the right
                if player.direction.x < 0:
                    player.rect.left = sprite.rect.right
                # collision from the left
                elif player.direction.x > 0:
                    player.rect.right = sprite.rect.left

    # apply tile collisions for vertical movement
    def vertical_movement_collision(self):
        player = self.player.sprite
        player.apply_gravity()

        for sprite in self.tiles.sprites():
            if sprite.rect.colliderect(player.rect):
                # collision from the top
                if player.direction.y > 0:
                    player.rect.bottom = sprite.rect.top
                    player.direction.y = 0
                # collision from the bottom
                elif player.direction.y < 0:
                    player.rect.top = sprite.rect.bottom
                    player.direction.y = 0

    # run
    def run(self):

        # tile sidescrolling update
        self.tiles.update(self.world_shift)
        # tile draw
        self.tiles.draw(self.display_surface)
        # side scrolling in accordance with player
        self.scroll_x()

        # draw player
        self.player.update()
        self.horizontal_movement_collision()
        self.vertical_movement_collision()
        self.player.draw(self.display_surface)
        
        