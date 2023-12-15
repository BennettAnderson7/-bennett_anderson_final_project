import pygame
from settings import *
from tiles import *

# define player class
class Player(pygame.sprite.Sprite):

    # player psotion
    def __init__(self,pos):
        super().__init__()
        #self.image = pygame.Surface((32,64))
        #self.image.fill(RED)
        self.image = pygame.image.load(os.path.join(img_folder, 'mario_sprite.png')).convert()
        # apply texture
        self.rect = self.image.get_rect(topleft = pos)

        # player movement
        self.direction = pygame.math.Vector2(0,0)
        # player movement constants
        self.speed = 8
        self.gravity = 0.8
        self.jump_speed = -16

    # define key inputs    
    def get_input(self):
        keys = pygame.key.get_pressed()

        # horizontal movement inputs
        if keys[pygame.K_d]:
            self.direction.x = 1
        elif keys[pygame.K_a]:
            self.direction.x = -1
        else:
            self.direction.x = 0

        # jump input
        if keys[pygame.K_SPACE]:
            self.jump()

    # apply gravity
    def apply_gravity(self):
        self.direction.y += self.gravity
        self.rect.y += self.direction.y

    # apply jump mechanics
    def jump(self):
        self.direction.y = self.jump_speed

    # initiate player update
    def update(self):
        self.get_input()
        