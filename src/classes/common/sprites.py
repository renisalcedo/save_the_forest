import pygame
import sys

class Sprite(pygame.sprite.Sprite):
    # pygame.sprite.Sprite =  Simple base class for visible game objects
    def __init__(self, pos, img_set, hp, id):
        #pygame.sprite.Sprite.__init__(self): rewriting it as following:
        super(Sprite, self).__init__()
        self.img_set = img_set
        self.index = 0
        self.image = self.img_set[self.index]
        self.rect = self.image.get_rect(center=pos)
        self.hp = hp
        self.id = id

    # adding one image to an array of images
    def add(self, img):
        img_set.append(img)

    # iterating through set of images
    def update(self, animate):
        if animate:
            self.index += 1

        if self.index >= len(self.img_set):
            self.index = 0
        
        self.image = self.img_set[self.index] 
        animate = False

    def receive_damage(self, dmg):
        self.hp -= dmg
        if self.hp <= 0:
            self.kill()