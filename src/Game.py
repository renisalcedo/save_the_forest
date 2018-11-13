import pygame
from random import choice

# Relative Imports
from src.classes.common.Button import Button
from src.classes.common.Menu import Menu
from src.classes.common.GameMap import GameMap
from src.classes.Shop import Shop
from src.classes.Enemy import Enemy

class Game:
    def __init__(self, screen):
        # Initial Game Properties
        self.level = 0
        self.playing = True
        self.screen = screen
        self.menu_open = True
        self.clock = pygame.time.Clock() 
        self.all_players = []
        self.last = pygame.time.get_ticks()
        self.money_cooldown = 2500
        self.coin_sound = pygame.mixer.Sound('./src/assets/music/Coin.ogg') 
        self.tree_count = 5
        self.enemies_killed = 0
        self.tree_pos = [[1400, 280], [1400, 360], [1400, 437], [1400,500], [1400,586]]
        self.last_tree_hit = pygame.time.get_ticks()
        self.game_over_prop = False

        # Initializes the enemy Group
        self.enemy_group = pygame.sprite.Group()

    def main(self):
        self.create()
        self.update()

    def create(self):
        pygame.mixer.music.load('./src/assets/music/background_music.ogg')

        color = [22, 160, 133]
        size = (150,50)

        # Creates Map
        img_url = './src/assets/maps/forest1/map02.png'
        self.map = GameMap(img_url)

        # Create the menu for the game
        self.menu = Menu(self.screen, color, size, self.map)
        self.menu.create_menu()

        # Creates Shop
        self.shop = Shop(self.screen)

    def update(self):
        while self.playing:
            # Game FPS (Frame per second)
            self.clock.tick()
            pygame.display.set_caption("{:.2f}".format(self.clock.get_fps()))

            # Active state in the game
            self.active_state()

            # All Game Runing Game Events
            self.all_event()

            if not self.menu_open and not self.game_over_prop:
                if self.tree_count == 0:
                    self.game_over()

                """ All Game Logic Goes Here"""
                # Active Shop
                self.shop.render_shop()

                # Draws Tree and Enemy Group into screen
                self.enemy_group.draw(self.screen)
                self.map.tree_groups.draw(self.screen)

                enemy_hit_tree = pygame.sprite.groupcollide(self.enemy_group, self.map.tree_groups, False, False)
                for enemy, tree in enemy_hit_tree.items():
                    enemy.attacking = True

                    make_damage = False

                    now = pygame.time.get_ticks()
                    if now - self.last_tree_hit >= 200:
                        self.last_tree_hit = now
                        now = pygame.time.get_ticks()
                        make_damage = True

                    if make_damage:
                        make_damage = False
                        tree[0].damaged(enemy.damage)

                        if tree[0].hp <= 0:
                            self.tree_count -= 1
                            enemy.attacking = False

                # Moves New Enemy at a constant speed
                dt = pygame.time.Clock().tick(60) / 1000
                self.enemy_group.update(dt, self.map.tree_groups)

                # Get Money Every now and then
                now = pygame.time.get_ticks()
                if now - self.last >= self.money_cooldown:
                    self.shop.time_money(True)
                    self.coin_sound.play()
                    self.last = now

                    Enemy(choice(self.tree_pos), self.enemy_group)

                # All Players moving
                for player in self.all_players:
                    player.shoot_bananas()

                    banana_hit_enemy = pygame.sprite.groupcollide(player.weapon_group, self.enemy_group, False, False)
                    enemy_hit_player = pygame.sprite.groupcollide(self.enemy_group, player.sprite_group, False, False)

                    for enemy, player in enemy_hit_player.items():
                        now = pygame.time.get_ticks()
                        make_damage = False
                        enemy.attacking = True

                        if now - self.last >= 200:
                            self.last = now
                            now = pygame.time.get_ticks()
                            make_damage = True

                        if make_damage:
                            make_damage = False
                            player[0].receive_damage(enemy.damage)

                            if player[0].hp <= 0:
                                del self.all_players[player[0].id]

                                enemy.attacking = False

                    for banana, enemy in banana_hit_enemy.items():
                        enemy[0].receive_damage(banana.damage)
                        banana.kill()

                        # Money for killing Enemy
                        self.enemies_killed += 1
                        self.shop.money += 10

            # Update the graphics in the game
            pygame.display.update()

    def game_over(self):
        self.game_over_prop = True

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
            # In Game Music
            pygame.mixer.music.play()
            self.menu_open = False
        else:
            self.menu_open = True

    def all_event(self):
        for event in pygame.event.get():
            # Closes the Game on exit
            if event.type == pygame.QUIT:
                self.playing = False

            if self.menu_open:
                self.menu.start.on_click(event, self.menu_state)

            if not self.menu_open:
                self.shop.shop_event(event, self.all_players)