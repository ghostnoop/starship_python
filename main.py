import pygame

from models import Enemy
from models.LaserGun import LaserGun
from models.Player import *
from models.Enemy import *
from config.settings import *

pygame.init()
clock = pygame.time.Clock()
display = pygame.display.set_mode((WIDTH, HEIGHT+200))

player_group = pygame.sprite.Group()


def events():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            # sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                new_laser = LaserGun(player)
                all_sprites.add(new_laser)
                lasers.add(new_laser)

            if event.key == pygame.K_ESCAPE:
                pygame.quit()


all_sprites = pygame.sprite.Group()

player = Player()
lasers = pygame.sprite.Group()
enemy_group = pygame.sprite.Group()
all_sprites.add(player)

tick_timer = 0


running = True
while running:
    clock.tick(60)
    events()

    font = pygame.font.SysFont(None, 30)
    img = font.render("100", True, RED)
    t = img.get_rect(center=(WIDTH / 2, 10))
    display.blit(img, t)

    tick_timer += 1
    if tick_timer > 60:
        tick_timer = 0
        if random.random() < 0.4:
            new_enemy = Enemy()
            all_sprites.add(new_enemy)
            enemy_group.add(new_enemy)

    all_sprites.update()

    hits = pygame.sprite.groupcollide(enemy_group, lasers, True, True)
    for hit in hits:
        m = Enemy()
        all_sprites.add(m)
        enemy_group.add(m)
        player.score += min_point

    hits = pygame.sprite.spritecollide(player, enemy_group, True)
    if hits:
        player.hearts -= 1
        if player.hearts <= 0:
            running = False

    display.fill(BLACK)
    all_sprites.draw(display)
    pygame.display.flip()

pygame.quit()
