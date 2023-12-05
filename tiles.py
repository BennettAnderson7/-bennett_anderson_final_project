import pygame
from settings import *
import os

# setup asset folders here - images sounds etc.
game_folder = os.path.dirname(__file__)
img_folder = os.path.join(game_folder, 'images')
snd_folder = os.path.join(game_folder, 'sounds')

class Tile(pygame.sprite.Sprite):
    def __init__(self,pos,size):
        super().__init__()
        self.image = pygame.Surface((size,size))
        #self.image.fill('green')
        self.image = pygame.image.load(os.path.join(img_folder, 'mario_grass_tile.png')).convert()
        self.rect = self.image.get_rect(topleft = pos)