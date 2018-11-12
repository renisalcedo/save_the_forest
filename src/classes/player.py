from Character import Character
from sprites import Sprite
import pygame

class Player(Character):
    def __init__(self, weapon, sprite):
        Character.__init__(self)
        self.weapon = weapon
        self.sprite = sprite 
    
    def load_image(self, name):
        image = pygame.image.load(name)
        return image

    def shoot(self):
        ##shoots projectile

        atk = self.self.stats['atk']

        return atk  

        # look for pygames animations // create a seperate function to animate
        # and call it in the shoot method
        # pygame clock
        # equation which accounts for speed, and time

    def defend(self, defense):
        #reflect damage from the attacker 
        
            dmg = ((self.stats['health'] - defense) / defense) + self.stats['atk'] 
            
            self.stats['health'] -= dmg 

            return self.get_status['health']
            return self.

        
        ## subtract defense points from attacker's health 

    def upgrade(self, key, val):
        if self.level < 5:
            self.stat_assign()
    
        self.level += 1





