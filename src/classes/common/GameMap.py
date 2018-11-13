from .Config import Configuration

import pygame

sx = Configuration().get_config('SCREEN_WIDTH')

class Tree(pygame.sprite.Sprite):
    def __init__(self, pos, *sprite_groups):
        super().__init__(*sprite_groups)
        self.hp = 150
        self.image = pygame.image.load('./src/assets/maps/forest1/tree.png')
        self.rect = self.image.get_rect(center=pos)

    # Personifies the tree into taking damage
    def damaged(self, dmg):
        self.hp -= dmg
        if self.hp <= 0:
            self.kill()

class GameMap:
    def __init__(self, map):
        self.map = pygame.image.load(map)
        self.tree_groups = pygame.sprite.Group()

        # Add All Trees to group
        Tree([40,280], self.tree_groups)
        Tree([40,360], self.tree_groups)
        Tree([40,437], self.tree_groups)
        Tree([40,500], self.tree_groups)
        Tree([40,586], self.tree_groups)

    def render(self, screen):
        screen.blit(pygame.transform.scale(self.map,(1280, 720)), [0,0])

    def get_tree(self, key):
        return self.trees[key]