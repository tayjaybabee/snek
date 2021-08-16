import pygame
from snek_inspyred.game.models import Snake, Food
from snek_inspyred.game.audio import Sounds


class Screen(object):
    def __init__(self, width=480, height=480, lock_proportion=True):
        if not isinstance(width, int) or not isinstance(height, int):
            raise TypeError()

        self.width = width
        self.height = height
        self.Grid = self.__Grid(scrn_h=self.height, scrn_w=self.width)
        self.display = pygame.display.set_mode((self.width, self.height), 0, 32)

    class __Grid(object):
        def __init__(self, size: int = 20, scrn_w: int = 480, scrn_h: int = 480):
            self.size = size
            self.width = scrn_h // self.size
            self.height = scrn_w // self.size

        def draw(self, surface):
            for y in range(0, self.height):
                for x in range(0, self.width):
                    if (x + y) %  2 == 0:
                        r = pygame.Rect((x*self.size, y*self.size), (self.size, self.size))
                        pygame.draw.rect(surface, (93, 216, 228), r)
                    else:
                        rr = pygame.Rect((x*self.size, y*self.size), (self.size, self.size))
                        pygame.draw.rect(surface, (84, 194, 205), rr)


def main():
    pygame.init()

    clock = pygame.time.Clock()

    screen = Screen(height=800, width=800)
    display = screen.display
    surface = pygame.Surface(display.get_size())
    surface = surface.convert()

    screen.Grid.draw(surface)

    sound = Sounds()

    snake = Snake(screen)
    food = Food(screen)
    myfont = pygame.font.SysFont('monospace', 16)
    sound.begin_game.play()

    while True:
        clock.tick(10)

        snake.check_keys()
        screen.Grid.draw(surface)
        snake.move()
        if snake.get_head_position() == food.position:
            snake.length += 1
            snake.score += 1

            sound.eat_food.play()

            food.randomize_position()

        snake.draw(surface)
        food.draw(surface)

        display.blit(surface, (0, 0))
        text = myfont.render("Score {0}".format(snake.score), 1, (0, 0, 0))
        display.blit(text, (5, 10))
        pygame.display.update()





