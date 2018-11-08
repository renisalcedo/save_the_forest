from src.Game import Game
from src.classes.common.Config import Configuration
import pygame
import os  

if __name__ == '__main__':
    config = Configuration()
    sw, sh = config.get_config('SCREEN_WIDTH'), config.get_config('SCREEN_HEIGHT')

    # Center the window on the center 
    os.environ['SDL_VIDEO_CENTERED'] = '1'

    # Initializes the pygame screen
    pygame.init()
    pygame.display.set_caption("Save the forest")
    screen = pygame.display.set_mode((1280,736))

    # Initializes the Game
    game = Game(screen)
    game.main()