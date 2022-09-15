import pygame as pg
import time

import const as c

sc = c.screen


def game_over():
    # Creating font obj my_font
    my_font = pg.font.SysFont('Poppins', 50, False, True)

    # Creating the text surface in which text
    # will be drawn
    game_over_surface = my_font.render(
        "Score: " + str(c.score), True, c.white
    )

    # Cerating a rect obj for the text
    # surface obj
    game_over_rect = game_over_surface.get_rect()

    # Setting the position of the text
    game_over_rect.midtop = (c.WINDOW_X/2, c.WINDOW_Y/4)

    # Blit will be draw the text on screen
    sc.blit(game_over_surface, game_over_rect)
    pg.display.flip()

    # After 2 sec we will close the game
    time.sleep(2)

    # Deactivating the python libray
    pg.quit()

    # End the program
    quit()
