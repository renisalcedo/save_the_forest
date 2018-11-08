import pygame
import sys

def load_image(name):
    image = pygame.image.load(name)
    #load new image from a file
    return image

class TestSprite(pygame.sprite.Sprite):
    # pygame.sprite.Sprite =  Simple base class for visible game objects
    def __init__(self):