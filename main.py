# File created by: Bennett Anderson

# Project Title: "(Name TBD) Platformer"

'''
Goals:
- Create a mario style platformer 
- Include side scrolling, powerups, mobs, challenges, and levels
- Implement textures and sounds
- Have it work perfectly based on my limited knowledge

'''

import pygame, sys
from settings import *
from tiles import Tile
from level import Level

pygame.init()
screen = pygame.display.set_mode((screen_width, screen_height))
clock = pygame.time.Clock()
#test_tile = pygame.sprite.Group(Tile((100,100),200))
level = Level(level_map,screen)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    screen.fill(SKY)
    #test_tile.draw(screen)
    level.run()

    pygame.display.update()
    clock.tick(60)