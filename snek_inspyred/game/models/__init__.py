import pygame
import random
import sys

from snek_inspyred.helpers import State

pygame.init()

PAUSE_TEXT = pygame.font.SysFont('Consolas', 32).render('Pause', True, pygame.color.Color('Black'))



class Snake(object):

    class MoveMatrix:
        def __init__(self):
            """
            Create a new instance of the move matrix which is made up of attributes for turning reference
            """
            self.UP = (0, -1)
            self.DOWN = (0, 1)
            self.LEFT = (-1, 0)
            self.RIGHT = (1, 0)

    def __init__(self, screen):
        """

        Create a new instance of the player class, in the case o this game our player class is 'Snake'

        """
        # Give it it's moving rules
        self._move = self.MoveMatrix()
        self.length = 1
        self.positions = [((screen.width / 2), (screen.height / 2))]
        self.direction = random.choice([self._move.UP, self._move.DOWN, self._move.LEFT, self._move.RIGHT])
        self.color = (17, 24, 47)
        self.grid = screen.Grid
        self.screen = screen
        self.score = 0
        self.state = State()

    def get_head_position(self):
        """

        Return the positions that the snake takes up on the grid.

        Returns:
            self.positions: The positions on the grid that the snake takes up.

        """
        return self.positions[0]

    def turn(self, point):
        """

        Turn the snake in a given direction.

        Args:
            point: The direction (ex. self._move.UP) you'd like the snake to turn.

        Returns:
            None

        """
        if self.length > 1 and (point[0] * -1, point[1] * -1) == self.direction:
            return
        else:
            self.direction = point

    def move(self):
        """

        Move the snake in the direction it's currently headed

        Returns:
            None

        """
        cur = self.get_head_position()
        x, y = self.direction
        new = (((cur[0] + (x*self.grid.size)) % self.screen.width), (cur[1] + (y*self.grid.size)) % self.screen.height)
        if len(self.positions) > 2 and new in self.positions[2:]:
            self.reset()
        else:
            self.positions.insert(0, new)
            if len(self.positions) > self.length:
                self.positions.pop()

    def check_keys(self):
        """

        Listen for specific keyboard events and move the snake accordingly.

        Returns:
            None

        """
        paused = False
        for event in pygame.event.get():
            print(event.type)

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    if self.state.is_paused():
                        self.state.unpause()
                    else:
                        self.state.pause()

            if not self.state.is_paused():

                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP:
                        self.turn(self._move.UP)
                    elif event.key == pygame.K_DOWN:
                        self.turn(self._move.DOWN)
                    elif event.key == pygame.K_LEFT:
                        self.turn(self._move.LEFT)
                    elif event.key == pygame.K_RIGHT:
                        self.turn(self._move.RIGHT)

    def reset(self):
        """

        Set the snake to default values

        Returns:
            None

        """
        self.length = 1
        self.positions = [((self.screen.width / 2), (self.screen.height / 2))]
        self.direction = random.choice([self._move.UP, self._move.DOWN, self._move.LEFT, self._move.RIGHT])
        self.score = 0

    def draw(self, surface):
        """

        Draw the snake on the board.

        Args:
            surface: A surface object

        Returns:
            None

        """
        for p in self.positions:
            r = pygame.Rect((p[0], p[1]), (self.grid.size, self.grid.size))
            pygame.draw.rect(surface, self.color, r)


class Food(object):
    def __init__(self, screen):
        """

        Create a new instance of the 'Food' class which are the assets that represent the 'food' that the snake eats
        in order to gain points for the gameplay loop.

        """
        self.position = (0, 0)
        self.color = (196, 72, 72)
        self.screen = screen
        self.randomize_position()

    def randomize_position(self):
        """

        Pick a new (random) location on the playing surface in which to appear as incentive for the player.

        Returns:
            None

        """
        self.position = (random.randint(0, self.screen.Grid.width - 1) * self.screen.Grid.size, random.randint(0, self.screen.Grid.height - 1) * self.screen.Grid.size)

    def draw(self, surface):
        """

        Draw at the given location, appearing for the player as incentive.

        Args:
            surface: A surface object.

        Returns:
            None

        """
        r = pygame.Rect((self.position[0], self.position[1]), (self.screen.Grid.size, self.screen.Grid.size))
        pygame.draw.rect(surface, self.color, r)
        pygame.draw.rect(surface, (196, 72, 72), r, 1)
