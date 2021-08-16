import pygame


class State(object):
    def __init__(self):
        self.previous = None
        self.current = 'running'
        self.paused = False

    def is_paused(self):
        print(f"Checked. Status: {self.paused}")
        return self.paused

    def pause(self):
        """

        Pause the game state.

        Returns:
            None

        """
        print("PAUSED")
        if not self.is_paused():
            self.previous = self.current
            self.current = 'paused'
            self.paused = True

    def unpause(self):
        """

        Unpause the game-state.

        Returns:
            None

        """
        print("UNPAUSED")
        if self.is_paused():
            self.previous = self.current
            self.current = 'running'
            self.paused = False
