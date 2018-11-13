import pygame
from .common.Config import Configuration
from .monkey import Monkey

class Shop:
    def __init__(self, screen):
        self.money = 100
        self.config = Configuration()
        self.sx, self.sy = 133, 90
        self.prices = {'monkey': 50}
        self.screen = screen
        self.move = False
        self.prev_pos = 0

        # Set all Custom configs before usage
        self.set_custom_config()

        self.font = self.config.get_custom('menu_font')

        # Load all Shop sprites
        self.coin = pygame.transform.scale(pygame.image.load('./src/assets/sprites/coin.png'), (50, 50))
        self.monkey = pygame.transform.scale(pygame.image.load('./src/assets/sprites/Monkey/monkey.png'), (50, 50))

        # ALL BUYING OBJECTS
        self.buy_monkey = pygame.Rect((self.sx+128, self.sy-8), (50, 50))

    def render_shop(self):
        # MONEY DISPLAY
        self.screen.blit(self.font.render(str(self.money), True, (241, 196, 15)),
                        (self.sx, self.sy))
        self.screen.blit(self.coin, [self.sx-65, self.sy-8])

        # MONKEY DISPLAY
        self.screen.blit(self.font.render(str(self.prices['monkey']), True, 
        (241, 196, 15) if self.money >= self.prices['monkey'] else (189, 195, 199)), (self.sx+204, self.sy))
        self.screen.blit(self.monkey, [self.sx+128, self.sy-8])

    def set_custom_config(self):
        # Sets custom configs
        self.config.add_config('menu_font', pygame.font.SysFont('Arial', 28))

    def shop_event(self, event, all_players):
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = event.pos

            if self.buy_monkey.collidepoint(mouse_pos):
                self.prev_pos = mouse_pos

                if self.money >= self.prices['monkey']:
                    self.money -= self.prices['monkey']
                    # A Monkey was bough
                    self.move = True

            if self.move and mouse_pos != self.prev_pos:
                if event.type == pygame.MOUSEBUTTONDOWN:
                    pos = list(event.pos)
                    pos[1] -= 10
                    # all_players.append(Monkey(self.screen, pos))
                    id = len(all_players)
                    all_players.append(Monkey(self.screen, pos, id))
                    self.move = False

    def set_money(self, amount):
        self.money += amount

    def time_money(self, money_up):
        if money_up:
            self.set_money(5)