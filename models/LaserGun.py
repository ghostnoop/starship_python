import random

from config.settings import *

class LaserGun(pygame.sprite.Sprite):

    def __init__(self, player, side, color):
        self.side = side
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((player.laser_length, 4))
        self.rect = self.image.get_rect()
        self.speed = player.laser_speed
        self.image.fill(color)

    def update(self):

        if self.side == 1:
            self.rect.x += self.speed
            if self.rect.x >= WIDTH:
                self.kill()

        if self.side == -1:
            self.rect.x -= self.speed
            if self.rect.x <= 0:
                self.kill()