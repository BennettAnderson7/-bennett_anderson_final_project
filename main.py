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

pygame.init()
screen = pygame.display.set_mode((screen_width, screen_height))
clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

screen.fill('black')
