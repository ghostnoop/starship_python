import pygame_menu
from pygame_menu.themes import Theme

from config import settings
from models import Score


def menu_loader(HEIGHT, WIDTH):
    def set_side(value, difficulty):
        settings.player_side[0] = difficulty
        pass

    def start_the_game():
        menu.disable()
        pass

    def scores_open():
        menu.disable()
        Score.open_score(WIDTH, HEIGHT + 200)
        menu.enable()
        pass

    myimage = pygame_menu.baseimage.BaseImage(
        image_path="static/images/background/backv3.png",
        drawing_mode=pygame_menu.baseimage.IMAGE_MODE_FILL,
    )

    mytheme = Theme(  # transparent background
        title_bar_style=pygame_menu.widgets.MENUBAR_STYLE_NONE)
    mytheme.background_color = myimage

    menu = pygame_menu.Menu(HEIGHT, WIDTH, '', theme=mytheme)

    menu.add_button('Play', start_the_game)
    menu.add_text_input('Name :', default='player')
    menu.add_selector('Your side :', [('light', 1), ('dark', 2)], onchange=set_side)
    # print(settings.player_side[0])
    menu.add_button('Scores', scores_open)
    menu.add_button('Quit', pygame_menu.events.EXIT)

    return menu
