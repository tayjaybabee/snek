import pygame
from pygame import Surface
import sys

# Set some default constants up.

# Let's define default screen dimensions
SCREEN_WIDTH, SCREEN_HEIGHT = (480,  480)

# The size of our grid
GRIDSIZE = 20

# Using the size of grid we want with the dimensions of our screen we can get both the height and width of the in-laid
# grid
GRID_WIDTH, GRID_HEIGHT = (SCREEN_HEIGHT / GRIDSIZE, SCREEN_WIDTH / GRIDSIZE)

# Games need buttons, and buttons need a purpose.
# The purpse of the arrow keys is to move the snek within the MoveMatrix
UP, DOWN = ((0, -1), (0, 1))
LEFT, RIGHT = ((-1, 0), (1, 0))

