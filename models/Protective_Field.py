from config.settings import *
from models.Instance import Instance

class Protective_Field(pygame.sprite.Sprite, Instance):

    def __init__(self, player):
        pygame.sprite.Sprite.__init__(self)
        Instance.__init__(self, field_hearts)
        self.image = pygame.Surface((200, 200))
        pygame.draw.circle(self.image, BLUE, (self.image.get_rect().x + self.image.get_width() // 2,
                                              self.image.get_rect().y + self.image.get_height() // 2), 100)
        self.rect = self.image.get_rect()
        self.image.set_alpha(60)
        self.player = player
        self.time = 0

    def new_field(self):
        self.hearts = field_hearts
        self.time = 0

    def update(self):
        self.time += 1
        self.rect.center = self.player.rect.center

        if self.hearts <= 0 or self.time == 1000:
            self.kill()
            self.new_field()