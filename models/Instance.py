import pygame

class Instance():

    def __init__(self, hearts):
        self.hearts = hearts

    def update(self):
        if self.hearts <= 0:
            self.kill()

    def hit(self, group):
        hits = pygame.sprite.spritecollide(self, group, True)
        if hits:
            self.hearts -= 1