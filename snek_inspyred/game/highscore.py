import os
import sys
from typing import List, Tuple

import pygame

HS_FILE = os.path.join(os.path.dirname(__file__), "high_scores.txt")


def load_high_scores() -> List[Tuple[str, int]]:
    """Return a list of saved high scores sorted descending."""
    if not os.path.exists(HS_FILE):
        return []
    scores = []
    with open(HS_FILE, "r") as handle:
        for line in handle:
            line = line.strip()
            if not line:
                continue
            if "," in line:
                name, score = line.split(",", 1)
                if score.isdigit():
                    scores.append((name, int(score)))
            elif line.isdigit():
                scores.append(("Anonymous", int(line)))
    scores.sort(key=lambda x: x[1], reverse=True)
    return scores[:5]


def save_high_score(name: str, score: int) -> None:
    """Persist a new score and keep only the top five."""
    scores = load_high_scores()
    scores.append((name, int(score)))
    scores.sort(key=lambda x: x[1], reverse=True)
    with open(HS_FILE, "w") as handle:
        for entry in scores[:5]:
            handle.write(f"{entry[0]},{entry[1]}\n")


def _prompt_for_name(display, screen) -> str:
    """Ask the player to enter their name using a simple text box."""
    font = pygame.font.SysFont("monospace", 24)
    clock = pygame.time.Clock()
    name = ""
    while True:
        display.fill((0, 0, 0))
        prompt = font.render("Enter Name: " + name, True, (255, 255, 255))
        display.blit(
            prompt,
            (
                screen.width // 2 - prompt.get_width() // 2,
                screen.height // 2 - prompt.get_height() // 2,
            ),
        )
        pygame.display.update()
        clock.tick(30)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    return name or "Anonymous"
                if event.key == pygame.K_BACKSPACE:
                    name = name[:-1]
                else:
                    if len(name) < 10 and event.unicode.isprintable():
                        name += event.unicode


def maybe_record_high_score(display, screen, score: int) -> None:
    """Record the score and ask for a name if it is a high score."""
    scores = load_high_scores()
    if len(scores) < 5 or score > scores[-1][1]:
        name = _prompt_for_name(display, screen)
    else:
        name = "Anonymous"
    save_high_score(name, score)
