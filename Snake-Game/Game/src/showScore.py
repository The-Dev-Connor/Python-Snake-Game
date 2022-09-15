import pygame as pg

import const as c

sc = c.screen


def show_score(choice, color, font, size):
    # Creating font obj score_font
    score_font = pg.font.SysFont(font, size)

    # Creating the display surface obj!
    # Score_Surface
    score_surface = score_font.render(
        'Your Score: ' + str(c.score), True, color)

    # Create a rect obj for the text
    # Surface_obj
    score_rect = score_surface.get_rect()

    # Display Text
    sc.blit(score_surface, score_rect)
