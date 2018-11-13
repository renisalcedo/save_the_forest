import pygame

class Tree:
    def __init__(self, pos):
        self.hp = 50
        self.pos = pos
        self.tree = pygame.image.load('./src/assets/maps/forest1/tree.png')

    def render(self, screen):
        screen.blit(self.tree, self.pos)

    # Personifies the tree into taking damage
    def damaged(self, dmg):
        self.hp -= dmg
        if self.hp <= 0:
            self.tree = pygame.image.load('./src/assets/maps/forest1/cutted.png')

class GameMap:
    def __init__(self, map):
        self.map = pygame.image.load(map)
        self.trees = {1:Tree([5,255]), 2:Tree([5,328]), 3:Tree([5,397]),
                      4:Tree([5,468]), 5:Tree([5,546])}

    def render(self, screen):
        screen.blit(pygame.transform.scale(self.map,(1280, 720)), [0,0])

        for _,tree in self.trees.items():
            tree.render(screen)

    def get_tree(self, key):
        return self.trees[key]