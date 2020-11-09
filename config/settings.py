import pygame

# display
WIDTH = 1280
HEIGHT = 720

# colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)

player_name = ["player"]
player_side = [1]
min_point = 100
player_hearts = 5
player_models = [
    pygame.transform.scale(pygame.image.load("static/images/x_wing/x1.png"), [195, 128]),
    pygame.transform.scale(pygame.image.load("static/images/x_wing/x2.png"), [195, 128]),
    pygame.transform.scale(pygame.image.load("static/images/x_wing/x3.png"), [195, 128]),
    pygame.transform.scale(pygame.image.load("static/images/x_wing/x4.png"), [195, 128]),
]
tie_models = [
    pygame.transform.scale(pygame.image.load("static/images/tie/tie1.png"), [187, 100]),
    pygame.transform.scale(pygame.image.load("static/images/tie/tie2.png"), [187, 100]),
    pygame.transform.scale(pygame.image.load("static/images/tie/tie3.png"), [187, 100]),
    pygame.transform.scale(pygame.image.load("static/images/tie/tie4.png"), [187, 100]),
]
boss_hearts = 15
boss_models = [
    pygame.transform.scale(pygame.image.load("static/images/imperial.png"), [230, 145]),
    pygame.transform.scale(pygame.image.load("static/images/falcon.png"), [220, 168])
]
field_hearts = 3
