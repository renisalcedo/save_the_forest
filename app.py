from src.Game import Game
import pygame

if __name__ == '__main__':
    # Initializes the pygame screen
    pygame.init()
    pygame.display.set_caption("Save the forest")
    screen = pygame.display.set_mode((1280,736))

    # Initializes the Game
    game = Game(screen)
    game.main()