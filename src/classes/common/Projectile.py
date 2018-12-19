import pygame
from .Config import Configuration

sx = Configuration().get_config('SCREEN_WIDTH') - 1000

class Projectile(pygame.sprite.Sprite):
    def __init__(self, pos, weapon, damage, *sprite_groups):
        super().__init__(*sprite_groups)
        self.image = weapon
        self.rect = self.image.get_rect(center=pos)
        self.pos = pygame.math.Vector2(pos)
        self.vel = pygame.math.Vector2(420, 0)
        self.damage = damage

    def update(self, dt):
        # Add the velocity to the position vector to move the sprite.
        self.pos += self.vel * dt
        self.rect.center = self.pos  # Update the rect pos.

        if self.pos[0] >= sx:
            self.kill()