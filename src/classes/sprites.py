import pygame
import sys

class Sprite(pygame.sprite.Sprite):
    # pygame.sprite.Sprite =  Simple base class for visible game objects
    def __init__(self):
        #pygame.sprite.Sprite.__init__(self): rewriting it as following:
        super(Sprite, self).__init__()
        self.img_set = []
        self.index = 0
        self.image = self.img_set[index]

    # adding one image to an array of images
    def add(self, img):
        img_set.append(img)

    # iterating through set of images
    def update(self):
        self.index += 1
        if self.index == len(self.img_set):
            self.index = 0
        
        self.image = self.img_set[self.index] 

    def animate(self, screen):
        self.update()
        self.draw(screen)

    