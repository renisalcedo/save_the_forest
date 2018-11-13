import pygame

from .common.player import Player
from .common.sprites import Sprite

class Monkey(Player):
    def __init__(self, screen, pos):
        # Loads all Monkey Sprites
        weapon = pygame.image.load("src/assets/sprites/Fruits/Banana.png")
        still = pygame.image.load("src/assets/sprites/Monkey/Jump/Jump1.png")
        jump1 = pygame.image.load("src/assets/sprites/Monkey/Jump/Jump2.png")
        jump2 = pygame.image.load("src/assets/sprites/Monkey/Jump/Jump3.png")
        jump3= pygame.image.load("src/assets/sprites/Monkey/Jump/Jump4.png")
        jump4 = pygame.image.load("src/assets/sprites/Monkey/Jump/Jump5.png")
        jump5 = pygame.image.load("src/assets/sprites/Monkey/Jump/Jump6.png")
        img_set = [still, jump1, jump2, jump3, jump4, jump5]

        # Initializes the Player with monkey Properties
        Player.__init__(self, "Monkey", weapon, screen, img_set, pos, 50)
    
    def shoot_bananas(self, event):
        self.shoot(event)

    def monkey_upgrade(self):
        self.upgrade('spd', 5)
        self.upgrade('atk', 1)