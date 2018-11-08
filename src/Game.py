import pygame
from src.classes.common.Button import Button
from src.classes.common.Menu import Menu

class Game:
    def __init__(self, screen):
        # Initial Game Properties
        self.level = 0
        self.playing = True
        self.screen = screen
        self.menu_open = True

    def main(self):
        self.create()
        self.update()

    def create(self):
        color = [22, 160, 133]
        size = (150,50)

        # Add And Load Background into the game
        self.background = pygame.image.load("./src/assets/images/backyard.png")

        # Create the menu for the game
        self.menu = Menu(self.screen, color, size, self.background)
        self.menu.create_menu()

    def update(self):
        while self.playing:
            # All Game Runing Game Events
            self.all_event()

            self.active_menu()

            # Update the graphics in the game
            pygame.display.update()

    def game_over(self):
        pass

    def active_menu(self):
        if self.menu_open:
            self.menu.active()
        else:
            self.screen.blit(self.background, [0,0])

    def level_up(self):
        self.level += 1
        pass

    def menu_state(self):
        if self.menu_open:
            self.menu_open = False
        else:
            self.menu_open = True

    def all_event(self):
        for event in pygame.event.get():
            # Closes the Game on exit
            if event.type == pygame.QUIT:
                self.playing = False

            self.menu.start.on_click(event, self.menu_state)