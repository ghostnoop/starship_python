import pygame
import pygame_menu
import time

from pygame_menu.themes import Theme
from models.LaserGun import *
from models.Menu import menu_loader
from models.Player import *
from models.Enemy import *
from models.Boss import *
from models.Protective_Field import *
from config.settings import *

pygame.init()
clock = pygame.time.Clock()

display = pygame.display.set_mode((WIDTH, HEIGHT + 200))

player_group = pygame.sprite.Group()

background = pygame.image.load("static/images/background/backv3.png")
background = pygame.transform.scale(background, [WIDTH, HEIGHT])

sound1 = pygame.mixer.Sound('static/sound/laser.wav')
sound2 = pygame.mixer.Sound('static/sound/laser_enemy.wav')
sound3 = pygame.mixer.Sound('static/sound/explosion.wav')


def menu_start():
    surface = pygame.display.set_mode((WIDTH, HEIGHT + 200))
    menu = menu_loader(HEIGHT, WIDTH)
    menu.mainloop(surface)


menu_start()

while True:
    def events():
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                # sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    sound1.play()
                    player.shoot()
                    all_sprites.add(player.laser_group)
                    lasers.add(player.laser_group)

                if event.key == pygame.K_s:
                    all_sprites.add(field)

                if event.key == pygame.K_ESCAPE:
                    # pygame.quit()
                    menu_start()
                    return

    all_sprites = pygame.sprite.Group()
    player = Player()
    lasers = pygame.sprite.Group()
    enemy_lasers = pygame.sprite.Group()
    enemy_group = pygame.sprite.Group()
    enemies_with_boss_group = pygame.sprite.Group()
    all_sprites.add(player)

    boss = Boss()
    field = Protective_Field(player)

    tick_timer = 0

    font = pygame.font.Font(None, 32)
    timer = float(time.time())
    # маркер для появления босса
    exists = False


    def save_score():
        f = open("static/scores.csv", "a")
        s = f"{player_name[0]};{player.score}"
        f.write(s + "\n")
        # f.write(player.)


    running = True
    clock.tick(60)

    while running:

        events()
        display.fill(BLACK)

        display.blit(background, (0, 0))
        # display.blit(background,(0,background.get_rect().width))
        # display.blit(bg_imgs[x], (rel_x - bg_imgs[x].get_rect().width, 0))

        # Lose
        if not player.alive():
            running = False
            save_score()
            menu_start()

        tick_timer += 1

        # босс появляется спустя 30 сек
        if float(time.time()) >= timer + 30:
            if not exists:
                enemies_with_boss_group.add(boss)
                all_sprites.add(boss)
                exists = True

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
                    sound2.play()
                    enemy.shoot()
                    enemy_lasers.add(enemy.laser_group)
                    all_sprites.add(enemy.laser_group)

        all_sprites.update()

        hits = pygame.sprite.groupcollide(enemy_group, lasers, True, True)
        for hit in hits:
            # m = Enemy()
            # all_sprites.add(m)
            # enemy_group.add(m)
            # enemies_with_boss_group.add(m)
            sound3.play()
            player.score += min_point

        field.hit(enemy_lasers)
        field.hit(enemy_group)

        player.hit(enemy_group)
        player.hit(enemy_lasers)

        # boss.hit(lasers)
        hits = pygame.sprite.spritecollide(boss, lasers, True)
        if hits:
            boss.hearts -= 1
            if boss.hearts <= 0:
                # Won
                boss.kill()
                save_score()
                time.sleep(0.5)
                running = False

        all_sprites.draw(display)

        pygame.draw.line(display, WHITE, (0, HEIGHT), (WIDTH, HEIGHT))

        # information about game
        pl_score = font.render(f'player score: {str(player.score).rjust(5, "0")}', True, GREEN)
        textRect = pl_score.get_rect()
        textRect.center = (WIDTH // 8, HEIGHT + 50)
        display.blit(pl_score, textRect)

        pl_hp = font.render(f"player hp: {player.hearts}", True, GREEN)
        textRect = pl_hp.get_rect()
        textRect.center = (WIDTH // 2, HEIGHT + 50)
        display.blit(pl_hp, textRect)
        # set the center of the rectangular object.

        pygame.display.flip()

    # pygame.quit()
