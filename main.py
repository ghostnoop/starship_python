import pygame

from models import Enemy
from models.LaserGun import LaserGun
from models.Player import *
from models.Enemy import *
from config.settings import *

pygame.init()
clock = pygame.time.Clock()
display = pygame.display.set_mode((WIDTH, HEIGHT + 200))

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

font = pygame.font.Font(None, 32)

running = True
while running:
    clock.tick(60)

    events()

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

    pygame.draw.line(display,WHITE, (0, HEIGHT), (WIDTH, HEIGHT))

    # information about game
    pl_score = font.render(f'player score: {str(player.score).rjust(5,"0")}', True, GREEN)
    textRect = pl_score.get_rect()
    textRect.center = (WIDTH // 8, HEIGHT + 50)
    display.blit(pl_score, textRect)

    pl_hp = font.render(f"player hp: {player.hearts}", True, GREEN)
    textRect = pl_hp.get_rect()
    textRect.center = (WIDTH // 2, HEIGHT + 50)
    display.blit(pl_hp, textRect)
    # set the center of the rectangular object.

    pygame.display.flip()

pygame.quit()
