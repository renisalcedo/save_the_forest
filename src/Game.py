import pygame

# Relative Imports
from src.classes.common.Button import Button
from src.classes.common.Menu import Menu
from src.classes.common.GameMap import GameMap
from src.classes.monkey import Monkey

class Game:
    def __init__(self, screen):
        # Initial Game Properties
        self.level = 0
        self.playing = True
        self.screen = screen
        self.menu_open = True
        self.clock = pygame.time.Clock() 

    def main(self):
        self.create()
        self.update()

    def create(self):
        color = [22, 160, 133]
        size = (150,50)
        self.monkey = Monkey(self.screen, [0,0])

        # Creates Map
        img_url = './src/assets/maps/forest1/map02.png'
        self.map = GameMap(img_url)

        # Create the menu for the game
        self.menu = Menu(self.screen, color, size, self.map)
        self.menu.create_menu()

    def update(self):
        while self.playing:
            self.clock.tick()

            # All Game Runing Game Events
            self.all_event()

            pygame.display.set_caption("{:.2f}".format(self.clock.get_fps()))

            # Update the graphics in the game
            pygame.display.update()


            self.active_state()

    def game_over(self):
        pass

    def active_state(self):
        if self.menu_open:
            self.menu.active()
        else:
            self.map.render(self.screen)
            
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

            
            self.monkey.shoot_bananas(event)
                
            self.menu.start.on_click(event, self.menu_state)
