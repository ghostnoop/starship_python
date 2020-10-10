import random

import pygame
from config.settings import *
from models.LaserGun import LaserGun

class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((20, 20))
        self.image.fill(RED)
        self.rect = self.image.get_rect()
        self.rect.x = random.randrange(WIDTH // 2, WIDTH - self.rect.width)
        self.rect.y = random.randrange(0, HEIGHT)
        self.speedy = random.randrange(1, 5)
        self.speedx = random.randrange(-2, -1)
        self.laser_group = pygame.sprite.Group()

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
        laser = LaserGun(self, -1, RED)
        laser.rect.bottom = self.rect.bottom
        laser.rect.centerx = self.rect.centerx
        self.laser_group.add(laser)