import random

import pygame
from config.settings import *
from models.LaserGun import LaserGun

class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)

        if player_side[0] == 1:
            self.image = pygame.image.load("static/images/tie/sid2.png").convert_alpha()
            self.image = pygame.transform.scale(self.image, [97, 100])
        else:
            self.image = pygame.image.load("static/images/x_wing/x-wing.png").convert_alpha()
            self.image = pygame.transform.scale(self.image, [100, 85])
        self.rect = self.image.get_rect()

        self.rect.x = random.randrange(WIDTH // 2+WIDTH//3, WIDTH - self.rect.width)
        self.rect.y = random.randrange(0, HEIGHT)
        self.speedy = random.randrange(1, 5)
        self.speedx = random.randrange(-2, -1)
        self.laser_group = pygame.sprite.Group()
        self.laser_length = 40
        self.laser_speed = 10

    def update(self):
        self.rect.x += self.speedx
        self.rect.y += self.speedy

        if self.rect.y >= HEIGHT - self.image.get_height():
            self.speedy = random.randrange(-5, -1)
        if self.rect.y <= 0:
            self.speedy = random.randrange(1, 5)

        if self.rect.left < -10:
            self.kill()

    def shoot(self):
        if player_side[0] == 1:
            laser = LaserGun(self, -1, RED)
        else:
            laser = LaserGun(self, -1, GREEN)
        laser.rect.center = self.rect.center
        self.laser_group.add(laser)