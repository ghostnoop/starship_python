import pygame

from config.settings import *
from models.Instance import *
from models.LaserGun import *

class Player(pygame.sprite.Sprite, Instance):

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.hearts = player_hearts

        if player_side[0] == 1:
            self.image = player_models[0]
        else:
            self.image = tie_models[0]

        self.rect = self.image.get_rect()
        self.rect.centerx = 80
        self.rect.bottom = HEIGHT // 2
        self.speedx = 0
        self.score = 0
        # animate
        self.state_icon = 0
        self.animate_sprite()
        self.laser_group = pygame.sprite.Group()
        self.laser_length = 40
        self.laser_speed = 10

    def update(self):
        Instance.update(self)

        if player_side[0] == 1:
            self.image = player_models[self.state_icon % len(player_models)]
        else:
            self.image = tie_models[self.state_icon % len(tie_models)]
        self.state_icon += 1

        if self.state_icon > 4:
            self.state_icon = 0

        self.speedy = self.speedx = 0
        keystate = pygame.key.get_pressed()

        if keystate[pygame.K_UP]:
            self.speedy = -8
        if keystate[pygame.K_DOWN]:
            self.speedy = 8
        if keystate[pygame.K_RIGHT]:
            self.speedx = 8
        if keystate[pygame.K_LEFT]:
            self.speedx = -8

        self.rect.y += self.speedy
        if self.rect.y >= HEIGHT - self.image.get_height():
            self.rect.y = HEIGHT - self.image.get_height()
        if self.rect.y < 0:
            self.rect.y = 0

        self.rect.centerx += self.speedx
        if self.rect.centerx >= WIDTH - self.image.get_width():
            self.rect.centerx = WIDTH - self.image.get_width()
        if self.rect.centerx - self.image.get_width() // 2 < 0:
            self.rect.centerx = self.image.get_width() // 2

    def shoot(self):
        if player_side[0] == 1:
            laser = LaserGun(self, 1, GREEN)
            if random.randint(0, 1) == 1:
                laser.rect.bottom = self.rect.top + 14
            else:
                laser.rect.bottom = self.rect.bottom - 5
            laser.rect.centerx = self.rect.centerx + 30
        else:
            laser = LaserGun(self, 1, RED)
            if random.randint(0, 1) == 1:
                laser.rect.bottom = self.rect.top + 41
            else:
                laser.rect.bottom = self.rect.bottom - 37
            laser.rect.left = self.rect.right - 7
        self.laser_group.add(laser)

    def score_update(self):
        self.score += 1

    def animate_sprite(self):
        pass