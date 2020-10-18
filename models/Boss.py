import random

from config.settings import *
from models.LaserGun import LaserGun
from models.Instance import Instance

class Boss(pygame.sprite.Sprite, Instance):

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)

        if player_side[0] == 1:
            self.image = boss_models[0]
        else:
            self.image = boss_models[1]
        self.rect = self.image.get_rect()
        self.rect.x = WIDTH + 100
        self.rect.y = HEIGHT // 2

        self.hearts = boss_hearts
        self.speed = 3
        self.up = True
        self.laser_group = pygame.sprite.Group()
        self.laser_length = 400
        self.laser_speed = 30

    def update(self):

        Instance.update(self)

        if self.rect.x > WIDTH - self.image.get_width():
            self.rect.x -= 3

        if self.rect.y >= HEIGHT - self.image.get_height():
            self.up = True
        if self.rect.y <= 0:
            self.up = False

        if self.up:
            self.rect.y -= self.speed
        else:
            self.rect.y += self.speed

    def shoot(self):
        laser = LaserGun(self, -1, YELLOW)
        laser.rect.right = self.rect.left + 60
        laser.rect.centery = self.rect.centery
        self.laser_group.add(laser)