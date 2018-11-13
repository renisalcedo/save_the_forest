import pygame

class Enemy(pygame.sprite.Sprite):
    def __init__(self, pos, *sprite_groups):
        super().__init__(*sprite_groups)
        """
        Walking resources for Enemy
        """
        walk1 = self.load_image('Walk/bandit1.png')
        walk2 = self.load_image('Walk/bandit2.png')
        walk3 = self.load_image('Walk/bandit3.png')
        walk4 = self.load_image('Walk/bandit4.png')
        walk5 = self.load_image('Walk/bandit5.png')
        walk6 = self.load_image('Walk/bandit6.png')
        walk7 = self.load_image('Walk/bandit7.png')
        walk8 = self.load_image('Walk/bandit8.png')
        self.walk_set = [walk1, walk2, walk3, walk4, walk5, walk6, walk7, walk8]
        self.walk_index = 0
        """
        Attacking resources for Enemy
        """
        atk1 = self.load_image('Attack/bandit0.png')
        atk2 = self.load_image('Attack/bandit1.png')
        atk3 = self.load_image('Attack/bandit2.png')
        atk4 = self.load_image('Attack/bandit3.png')
        atk5 = self.load_image('Attack/bandit4.png')
        atk6 = self.load_image('Attack/bandit5.png')
        atk7 = self.load_image('Attack/bandit6.png')
        atk8 = self.load_image('Attack/bandit7.png')
        self.atk_set = [atk1, atk2, atk3, atk4, atk5, atk6, atk7, atk8]
        self.atk_index = 0 

        # Enemy Properties
        self.image = self.walk_set[self.walk_index]
        self.rect = self.image.get_rect(center=pos)
        self.pos = pygame.math.Vector2(pos)
        self.vel = pygame.math.Vector2(-150, 0)
        self.damage = 50
        self.hp = 250
        self.attacking = False

    def load_image(self, name):
        return pygame.transform.scale(pygame.image.load('./src/assets/sprites/Enemy/' + name), (100, 100))

    # iterating through set of images
    def animate_walk(self, animate):
        if animate:
            self.walk_index += 1

        if self.walk_index >= len(self.walk_set):
            self.walk_index = 0
        
        self.image = self.walk_set[self.walk_index] 
        animate = False

    # iterating through set of images
    def animate_attack(self, animate):
        if animate:
            self.atk_index += 1

        if self.atk_index >= len(self.atk_set):
            self.atk_index = 0
        
        self.image = self.atk_set[self.atk_index] 
        animate = False

    def update(self, dt, target):
        if self.attacking:
            self.animate_attack(True)
        else:
            self.pos += self.vel * dt
            self.rect.center = self.pos
            self.animate_walk(True)

        if self.pos[0] <= 0:
            self.kill()

    def receive_damage(self, dmg):
        self.hp -= dmg

        if self.hp <= 0:
            self.kill()