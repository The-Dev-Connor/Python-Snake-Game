import pygame as pg

# The Window size!
WINDOW_X = 720
WINDOW_Y = 480

# Defining Colors
black = pg.Color(0, 0, 0)
white = pg.Color(255, 255, 255)
red = pg.Color(255, 0, 0)
green = pg.Color(0, 255, 0)
blue = pg.Color(0, 0, 255)

# The score of the game
score = 0

# Load teh music file!
music = '../assets/music/8-bit.mp3'

# Load teh background for the game!
bg = pg.image.load('../assets/images/bg(1).png')

# Define the width and heght of the screen
screen = pg.display.set_mode((WINDOW_X, WINDOW_Y))
