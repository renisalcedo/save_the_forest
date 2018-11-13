import pygame
from .common.Config import Configuration
# Will display the current money amount 
# Use the money amount for buying players
# Add opacity to things not buyable
# Original color for buyable things
# Creates instance of bough item and return it
# keep array of all bough items
# 

class Shop:
    def __init__(self):
        self.money = 100
        self.config = Configuration()
        self.sw, self.sh, self.cx, self.cy = self.config.get_all_config()

        # Set all Custom configs before usage
        self.set_custom_config()

        self.font = self.config.get_custom('menu_font')

        # Load all Shop sprites
        self.coin = pygame.image.load('./src/assets/sprites/coins.png')

    def render_shop(self, screen):
        screen.blit(self.font.render(str(self.money), True, (52, 73, 94)), 
                        (self.cx, self.cy))

    def set_custom_config(self):
        # Sets custom configs
        self.config.add_config('posx', self.cx)
        self.config.add_config('posy', self.cy)
        self.config.add_config('menu_font', pygame.font.SysFont('Arial', 25))