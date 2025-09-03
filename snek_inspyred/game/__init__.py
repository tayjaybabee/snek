import sys
import pygame
from snek_inspyred.game.models import Snake, Food
from snek_inspyred.game.audio import Sounds
from snek_inspyred.game.highscore import load_high_scores


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


def show_high_scores(display, screen):
    """Display the stored high scores until the user presses 'B'."""
    font = pygame.font.SysFont('monospace', 24)
    back_text = font.render('B - Back', True, (255, 255, 255))
    clock = pygame.time.Clock()
    while True:
        display.fill((0, 0, 0))
        title = font.render('High Scores', True, (255, 255, 255))
        display.blit(title, (screen.width // 2 - title.get_width() // 2, 50))
        scores = load_high_scores()
        for idx, score in enumerate(scores):
            text = font.render(f"{idx + 1}. {score}", True, (255, 255, 255))
            display.blit(text, (screen.width // 2 - text.get_width() // 2, 100 + idx * 30))
        display.blit(back_text, (screen.width // 2 - back_text.get_width() // 2, screen.height - 80))
        pygame.display.update()
        clock.tick(15)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN and event.key == pygame.K_b:
                return


def start_screen(display, screen):
    """Show the start menu with options to start or view high scores."""
    font = pygame.font.SysFont('monospace', 32)
    clock = pygame.time.Clock()
    while True:
        display.fill((0, 0, 0))
        title = font.render('SNEK', True, (255, 255, 255))
        start_text = font.render('S - Start Game', True, (255, 255, 255))
        high_text = font.render('H - High Scores', True, (255, 255, 255))
        display.blit(title, (screen.width // 2 - title.get_width() // 2, screen.height // 2 - 100))
        display.blit(start_text, (screen.width // 2 - start_text.get_width() // 2, screen.height // 2))
        display.blit(high_text, (screen.width // 2 - high_text.get_width() // 2, screen.height // 2 + 40))
        pygame.display.update()
        clock.tick(15)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_s:
                    return
                if event.key == pygame.K_h:
                    show_high_scores(display, screen)

def main():
    pygame.init()

    clock = pygame.time.Clock()

    screen = Screen(height=800, width=800)
    display = screen.display
    start_screen(display, screen)
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





