import pygame

from .common.player import Player
from .common.sprites import Sprite

class Monkey(Player):
    def __init__(self, screen, pos):
        # Loads all Monkey Sprites
        weapon = pygame.transform.scale(pygame.image.load("src/assets/sprites/Fruits/Banana.png"), (50, 50))
        still = pygame.transform.scale(pygame.image.load("src/assets/sprites/Monkey/Jump/Jump1.png"), (100,100))
        jump1 = pygame.transform.scale(pygame.image.load("src/assets/sprites/Monkey/Jump/Jump2.png"), (100,100))
        jump2 = pygame.transform.scale(pygame.image.load("src/assets/sprites/Monkey/Jump/Jump3.png"), (100,100))
        jump3 = pygame.transform.scale(pygame.image.load("src/assets/sprites/Monkey/Jump/Jump4.png"), (100,100))
        jump4 = pygame.transform.scale(pygame.image.load("src/assets/sprites/Monkey/Jump/Jump5.png"), (100,100))
        jump5 = pygame.transform.scale(pygame.image.load("src/assets/sprites/Monkey/Jump/Jump6.png"), (100,100))
        img_set = [still, jump1, jump2, jump3, jump4, jump5]

        # Initializes the Player with monkey Properties
        Player.__init__(self, "Monkey", weapon, screen, img_set, pos, 50)
   
    def shoot_bananas(self):
        self.shoot()

    def monkey_upgrade(self):
        self.upgrade('spd', 5)
        self.upgrade('atk', 1)