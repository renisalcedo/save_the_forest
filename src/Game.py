import pygame

class Game:
    def __init__(self):
        # Initial Game Properties
        self.level = 0
        self.pause = False
        self.playing = True

        # Initialize Game Window
        self.window_init("Save the forest", (1280,736))

    def main(self):
        self.create()
        self.update()

    def create(self):
        self.background = pygame.image.load("./src/assets/images/backyard.png")

    def update(self):
        # LOADS THE BACKGROUND INTO THE GAME
        self.screen.blit(self.background, [0,0])
        pygame.display.flip()

        while self.playing:
            # Gets all events in Game
            for event in pygame.event.get():
                # Closes the Game on exit
                if event.type == pygame.QUIT:
                    self.playing = False

    def game_over(self):
        pass

    def menu(self):
        pass

    def level_up(self):
        self.level += 1
        pass

    def window_init(self, title, size):
        pygame.init()
        pygame.display.set_caption(title)
        self.screen = pygame.display.set_mode(size)