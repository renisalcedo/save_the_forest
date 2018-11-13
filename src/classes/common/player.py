from .character import Character
from .sprites import Sprite
import pygame
from .Config import Configuration

sx = Configuration().get_config('SCREEN_WIDTH')

class Projectile(pygame.sprite.Sprite):
    def __init__(self, pos, weapon, damage, *sprite_groups):
        super().__init__(*sprite_groups)
        self.image = weapon
        self.rect = self.image.get_rect(center=pos)
        self.pos = pygame.math.Vector2(pos)
        self.vel = pygame.math.Vector2(420, 0)
        self.damage = 10

    def update(self, dt):
        # Add the velocity to the position vector to move the sprite.
        self.pos += self.vel * dt
        self.rect.center = self.pos  # Update the rect pos.

        if self.pos[0] >= sx:
            self.kill()

class Player(Character):
    def __init__(self, name, weapon, screen, img_set, pos, cost, health=250, spd=5, dfnd=5, atk=5, level=1):
        Character.__init__(self, level, name, cost, health, spd, dfnd, atk)
        self.screen = screen
        self.pos = pos

        # Sprites for Player
        sprite = Sprite(pos, img_set)
        self.sprite_group = pygame.sprite.Group(sprite)

        # Sprites group for weapon
        self.weapon = weapon
        self.weapon_timer = .1
        self.weapon_group = pygame.sprite.Group()

        # Add timing for delay
        self.cooldown = -self.get_status('spd') + 290
        self.last = pygame.time.get_ticks()

        # Sound Effects
        self.shoot_sound = pygame.mixer.Sound('./src/assets/music/Hit.ogg')

    def animate(self, animate):
        self.sprite_group.update(animate)
    
    def load_image(self, name):
        image = pygame.image.load(name)
        self.sprite.add(image)

    def shoot(self):
        # shoots projectile
        now = pygame.time.get_ticks()
        self.sprite_group.draw(self.screen)

        # Shoots projectile
        dt = pygame.time.Clock().tick(60) / 1000
        self.weapon_group.update(dt)
        self.weapon_group.draw(self.screen)

        if now - self.last >= self.cooldown:
            self.animate(True)
            self.last = now

        self.weapon_timer -= dt
        if self.weapon_timer <= 0:
            self.weapon_timer = -self.get_status('spd') + 6

            # Adds Projectile to projectile group
            Projectile(self.pos, self.weapon, self.get_status('atk'), self.weapon_group)
            self.shoot_sound.play()

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