import random

from config.settings import *

class LaserGun(pygame.sprite.Sprite):

    def __init__(self, player, side, color):
        self.side = side
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((40, 5))
        self.rect = self.image.get_rect()
        self.speed = 10
        self.image.fill(color)

        if side == 1:
            if random.randint(0, 1) == 1:
                self.rect.bottom = player.rect.top + 14
            else:
                self.rect.bottom = player.rect.bottom - 5
            self.rect.centerx = player.rect.centerx + 30

    def update(self):

        if self.side == 1:
            self.rect.x += self.speed
            if self.rect.x >= WIDTH:
                self.kill()

        if self.side == -1:
            self.rect.x -= self.speed
            if self.rect.x <= 0:
                self.kill()