import pygame as pg
import random as rd

import const as c
from gameOver import game_over
from showScore import show_score

snake_speed = 15
volume = 0.7
sc = c.screen

# Initualize pg
pg.init()
pg.font.init()
pg.mixer.init()

# Set the title of the display!
pg.display.set_caption('Snake ASMR')

# Set the MUSIC!
pg.mixer.music.load(c.music)
pg.mixer.music.set_volume(volume)
# The -1 will loop the music!
pg.mixer.music.play(-1)

# Call the screen varuable
sc

# Define the Snake position and fruits pos
snake_pos = [100, 50]

fruit_pos = [rd.randrange(1, (c.WINDOW_X//10)) * 10,
             rd.randrange(1, (c.WINDOW_Y//10)) * 10]

fruit_spawn = True

# Define the first 4 blocks of the snake body
snake_body = [[100, 50],
              [90, 50],
              [80, 50],
              [70, 50]]

# Setting the default snake direction towards the right
direction = 'RIGHT'
change_to = direction

# Initail Score
c.score

fps = pg.time.Clock()

# Holds all of the game logic
while True:
    # handle key events
    for e in pg.event.get():
        if e.type == pg.KEYDOWN:
            if e.key == pg.K_UP:
                change_to = 'UP'

            elif e.key == pg.K_DOWN:
                change_to = 'DOWN'

            elif e.key == pg.K_LEFT:
                change_to = 'LEFT'

            elif e.key == pg.K_RIGHT:
                change_to = 'RIGHT'

    # If two keysare pssed at the same time
    # we don't want the snake to move into
    # two directions at one
    if change_to == 'UP' and direction != 'DOWN':
        direction = 'UP'

    if change_to == 'DOWN' and direction != 'UP':
        direction = 'DOWN'

    if change_to == 'LEFT' and direction != 'RIGHT':
        direction = 'LEFT'

    if change_to == 'RIGHT' and direction != 'LEFT':
        direction = 'RIGHT'

    # Movingthe snake
    if direction == "UP":
        snake_pos[1] -= 10
    if direction == "DOWN":
        snake_pos[1] += 10
    if direction == "LEFT":
        snake_pos[0] -= 10
    if direction == "RIGHT":
        snake_pos[0] += 10

    # Snake growing mechanic
    # if the fruits and snake collide then scores
    # will be incrementeed by 10
    snake_body.insert(0, list(snake_pos))
    if snake_pos[0] == fruit_pos[0] and snake_pos[1] == fruit_pos[1]:
        c.score += 10
        fruit_spawn = False
    else:
        snake_body.pop()

    if not fruit_spawn:
        fruit_pos = [rd.randrange(1, (c.WINDOW_X//10)) * 10,
                     rd.randrange(1, (c.WINDOW_Y//10)) * 10]

    fruit_spawn = True
    sc.blit(c.bg, (0, 0))

    for pos in snake_body:
        pg.draw.rect(sc, c.green, pg.Rect(pos[0], pos[1], 10, 10))

    pg.draw.rect(sc, c.blue, pg.Rect(fruit_pos[0], fruit_pos[1], 10, 10))

    # Game Over Conditions
    if snake_pos[0] < 0 or snake_pos[0] > c.WINDOW_X-10:
        game_over()
    if snake_pos[1] < 0 or snake_pos[1] > c.WINDOW_Y-10:
        game_over()

    # Touching the snake body
    for square in snake_body[1:]:
        if snake_pos[0] == square[0] and snake_pos[1] == square[1]:
            game_over()

    # display score
    show_score(1, c.white, 'Poppins', 20)

    # Refresh game screen
    pg.display.update()
    # Frame Per Seound / Refresh rate
    fps.tick(snake_speed)
