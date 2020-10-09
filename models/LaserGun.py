import random

import pygame

from config.settings import *


class LaserGun(pygame.sprite.Sprite):
    def __init__(self, player):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((40, 5))
        self.image.fill(RED)
        self.rect = self.image.get_rect()
        self.pl = player
        if random.randint(0, 1) == 1:
            self.rect.bottom = self.pl.rect.top + 14
        else:
            self.rect.bottom = self.pl.rect.bottom - 5
        self.rect.centerx = player.rect.centerx + 30
        self.speedy = +10

    def update(self):

        self.rect.x += self.speedy
        if self.rect.x >= WIDTH:
            self.kill()
