import os

HS_FILE = os.path.join(os.path.dirname(__file__), 'high_scores.txt')


def load_high_scores():
    """Return a list of saved high scores sorted descending."""
    if not os.path.exists(HS_FILE):
        return []
    scores = []
    with open(HS_FILE, 'r') as handle:
        for line in handle:
            line = line.strip()
            if line.isdigit():
                scores.append(int(line))
    return sorted(scores, reverse=True)[:5]


def save_high_score(score: int) -> None:
    """Persist a new score if it is among the top scores."""
    scores = load_high_scores()
    scores.append(int(score))
    scores.sort(reverse=True)
    with open(HS_FILE, 'w') as handle:
        for entry in scores[:5]:
            handle.write(f"{entry}\n")
