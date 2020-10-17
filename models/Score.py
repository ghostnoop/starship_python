import pygame

pygame.init()
clock = pygame.time.Clock()


def get_score():
    def sort_by_second(val):
        return int(val[1])

    f = open("static/scores.csv", "r")
    tab = [x.replace("\n", "").split(";") for x in f.readlines()[1:]]
    tab.sort(key=sort_by_second)
    return tab


def open_score(WIDTH, HEIGHT):
    tab = get_score()[:10]

    display = pygame.display.set_mode((WIDTH, HEIGHT))
    font = pygame.font.Font(None, 32)
    running = True
    while running:
        clock.tick(20)
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    return

        display.fill((0, 0, 0))
        k = 1
        grap = 50
        i = tab[0]
        for i in tab:
            pl_score = font.render(f'#{k} ; name: {i[0]} ; score: {i[1]}', True, (255, 255, 255))
            textRect = pl_score.get_rect()
            textRect.center = (WIDTH // 2, grap * k)
            display.blit(pl_score, textRect)
            k += 1



        pygame.display.flip()


# open_score()
