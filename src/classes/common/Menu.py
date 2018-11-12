import pygame
from .Config import Configuration
from .Button import Button

class Menu:
    def __init__(self, screen, color, size, background):
        self.color = color
        self.size = size
        self.screen = screen
        self.background = background
        self.config = Configuration()
        self.sw, self.sh, self.cx, self.cy = self.config.get_all_config()

    def create_menu(self):
        self.set_custom_config()
        
        # Initialize the CUSTOM configuration values
        posx = self.config.get_custom('posx')
        posy = self.config.get_custom('posy')

        # CREATES THE PANE AND BUTTONS
        self.menu_pane = pygame.Rect((posx, posy), (400, 200))

        self.start = Button(self.screen, self.color, (self.cx-70, self.cy-60), self.size)
        self.scores = Button(self.screen, self.color, (self.cx-70, self.cy+20), self.size)

    def active(self):
        # Activate Buttons and Background
        self.background.render(self.screen)

        # Pane for the options
        pygame.draw.rect(self.screen, [39, 174, 96], self.menu_pane)

        # Activate Menu Text and Buttons
        font = self.config.get_custom('menu_font')

        self.start.flip()
        self.scores.flip()

        self.screen.blit(font.render("Start", True, (52, 73, 94)), 
                        (self.cx-23, self.cy-50))
        self.screen.blit(font.render("Scores", True, (52, 73, 94)), 
                        (self.cx-30, self.cy+28))

    def set_custom_config(self):
        # Sets custom configs
        self.config.add_config('posx', self.cx-190)
        self.config.add_config('posy', self.cy-100)
        self.config.add_config('menu_font', pygame.font.SysFont('Arial', 25))