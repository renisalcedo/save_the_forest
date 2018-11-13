from .character import Character
from .sprites import Sprite
import pygame
from .Config import Configuration

sx = Configuration().get_config('SCREEN_WIDTH')

class Player(Character):
    def __init__(self, name, weapon, screen, img_set, pos, cost, health=250, spd=5, dfnd=5, atk=5, level=1):
        Character.__init__(self, level, name, cost, health, spd, dfnd, atk)
        self.weapon = weapon
        self.screen = screen
        self.pos = pos # Placeholder for player pos

        sprite = Sprite(img_set)
        self.sprite_group = pygame.sprite.Group(sprite)

    def animate(self, screen):
        self.sprite_group.update()
        self.sprite_group.draw(screen)
    
    def load_image(self, name):
        image = pygame.image.load(name)
        self.sprite.add(image)

    def shoot(self, event):
        ##shoots projectile
        weapon = self.weapon 
        self.sprite_group.update()
        self.animate(self.screen)
        self.screen.blit(weapon, self.pos)
        self.active_projectile(self.pos, weapon, event)

    """ 
    If function keeps the x updating
    put curr x inside the condition
    """
    """
    ADD COLLISION EVENT
    ADDING DAMAGE TO ENEMY ON ITEM COLLISION
    """
    def active_projectile(self, curr_pos, weapon, event):
        curr_pos[0] += 5
        if not self.off_limits(curr_pos[0]):
            self.screen.blit(weapon, curr_pos)

    def off_limits(self, x):
        return True if x > sx else False
        
        # look for pygames animations // create a seperate function to animate
        # and call it in the shoot method
        # pygame clock
        # equation which accounts for speed, and time

    def defend(self):
        #reflect damage from the attacker
        hp, dfnd, atk = self.get_status('health'), self.get_status('dfnd'), self.get_status('atk')

        if hp > dfnd:
            dmg = ((hp - dfnd) // dfnd) + atk
            return dmg
        
        return atk

    def upgrade(self, key, val):
        if self.level < 5:
            self.stat_assign(key, val)
    
        self.level += 1





