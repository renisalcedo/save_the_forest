import pygame
from src.classes.common.Button import Button

class Game:
    def __init__(self, screen):
        # Initial Game Properties
        self.level = 0
        self.pause = False
        self.playing = True
        self.screen = screen

    def main(self):
        self.create()
        self.update()

    def create(self):
        # Add And Load Background into the game
        self.background = pygame.image.load("./src/assets/images/backyard.png")
        self.screen.blit(self.background, [0,0])

    def update(self):
        while self.playing:
            # All Game Runing Game Events
            self.all_event()

            # Update the graphics in the game
            pygame.display.update()

    def game_over(self):
        pass

    def menu(self):
        pass

    def level_up(self):
        self.level += 1
        pass

    def all_event(self):
        for event in pygame.event.get():
            # Closes the Game on exit
            if event.type == pygame.QUIT:
                self.playing = False