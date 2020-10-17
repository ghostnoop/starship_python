import pygame

from config.settings import *
from models.Instance import *

class Player(pygame.sprite.Sprite, Instance):

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.hearts = player_hearts
        self.image = player_models[0]

        # self.image = pygame.Surface((50, 40))
        # self.image.fill(GREEN)
        self.rect = self.image.get_rect()
        self.rect.centerx = 80
        self.rect.bottom = HEIGHT // 2
        self.speedx = 0
        self.score = 0
        # animate
        self.state_icon = 0
        self.animate_sprite()

    def update(self):
        Instance.update(self)

        self.image = player_models[self.state_icon % len(player_models)]
        self.state_icon += 1

        if self.state_icon > len(player_models):
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

    def score_update(self):
        self.score += 1

    def animate_sprite(self):
        pass