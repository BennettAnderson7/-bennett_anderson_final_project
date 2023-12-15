# File created by: Bennett Anderson 12/14/23

# content from kids can code: http://kidscancode.org/blog/
# content from Clear Code: https://www.youtube.com/@ClearCode

# Project Title: "Platformer"

'''
Goals:
- Create a mario style platformer based on tiles
- Include side scrolling, powerups, mobs, challenges, and levels
- Implement textures and sounds
- Have it work perfectly based on my limited knowledge

'''

# import libraries and modules
import pygame, sys
from settings import *
from tiles import *
from level import Level


pygame.init()
# define screen size
screen = pygame.display.set_mode((screen_width, screen_height))
# initiate game clock
clock = pygame.time.Clock()
#test_tile = pygame.sprite.Group(Tile((200,100),200))
level = Level(level_map,screen)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    
    # apply color to screen
    screen.fill(SKY)
    #test_tile.draw(screen)
    level.run()

    # initiate update
    pygame.display.update()
    clock.tick(60)