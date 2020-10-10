import pygame
import time

from models.LaserGun import *
from models.Player import *
from models.Enemy import *
from models.Boss import *
from config.settings import *

pygame.init()
clock = pygame.time.Clock()
display = pygame.display.set_mode((WIDTH, HEIGHT+200))
# display = pygame.display.set_mode((WIDTH, HEIGHT))

player_group = pygame.sprite.Group()

def events():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            # sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                new_laser = LaserGun(player, 1, GREEN)
                all_sprites.add(new_laser)
                lasers.add(new_laser)

            if event.key == pygame.K_ESCAPE:
                pygame.quit()


all_sprites = pygame.sprite.Group()

player = Player()
lasers = pygame.sprite.Group()
enemy_lasers = pygame.sprite.Group()
enemy_group = pygame.sprite.Group()
enemies_with_boss_group = pygame.sprite.Group()
all_sprites.add(player)

boss = Boss()

tick_timer = 0

timer = float(time.time())
# маркер для появления босса
exists = False

running = True
while running:
    clock.tick(60)
    events()

    font = pygame.font.SysFont(None, 30)
    img = font.render("100", True, RED)
    t = img.get_rect(center=(WIDTH / 2, 10))
    display.blit(img, t)

    tick_timer += 1

    # босс появляется спустя 30 сек
    if float(time.time()) >= timer + 30:
        if not exists:
            enemies_with_boss_group.add(boss)
            all_sprites.add(boss)
            exists = True

    # # босс не появится, пока не наберешь опр. кол-во очков
    # if not exists and player.score == 1000:
    #     all_sprites.add(boss)
    #     exists = True

    if tick_timer > 60:
        tick_timer = 0
        if random.random() < 0.4:
            new_enemy = Enemy()
            all_sprites.add(new_enemy)
            enemies_with_boss_group.add(new_enemy)
            enemy_group.add(new_enemy)

    if tick_timer == 0:
        for enemy in enemies_with_boss_group:
            if random.random() <= 0.5:
                enemy.shoot()
                enemy_lasers.add(enemy.laser_group)
                all_sprites.add(enemy.laser_group)

    all_sprites.update()

    hits = pygame.sprite.groupcollide(enemy_group, lasers, True, True)
    for hit in hits:
        m = Enemy()
        all_sprites.add(m)
        enemy_group.add(m)
        enemies_with_boss_group.add(m)
        player.score += min_point

    hits_1 = pygame.sprite.spritecollide(player, enemy_group, True)
    hits_2 = pygame.sprite.spritecollide(player, enemy_lasers, True)
    if hits_1 or hits_2:
        player.hearts -= 1
        if player.hearts <= 0:
            running = False

    hits = pygame.sprite.spritecollide(boss, lasers, True)
    if hits:
        boss.hearts -= 1
        if boss.hearts <= 0:
            boss.kill()

    display.fill(BLACK)
    all_sprites.draw(display)
    pygame.display.flip()

pygame.quit()