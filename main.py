# ------------------------------------------------------------------------------------------
# Author: Jesse Hancock
# Title of game: Survive!
# Description: main file of the game, the goal is to dodge all the obstacles
# Date Created: 8/4/2024
# Last Updated: 8/4/2024
# -----------------------------------------------------------------------------------------

# This is the package that will run the game
import pygame

# This helps run the player
from player import Player

# This is the package that will use tools to exit the game when the player quits
import sys

# This is the package that manages game settings
from settings import Settings


class Survive:
    """Overall class to manage game assets and behavior"""

    def __init__(self):
        self.settings = Settings()

        """Initialize the game and create game resources."""
        pygame.init()

        # This controls the game frame rate
        self.clock = pygame.time.Clock()

        pygame.display.set_caption("Survive")

        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))

        self.bg_color = (0, 0, 0)

        self.screen.fill(self.bg_color)

        self.player = Player(self)

    def _check_events(self):
        """Respond to keypresses and mouse events."""

        # Watch for keyboard and mouse events.
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

    def run_game(self):
        """Runs the game"""
        while True:
            pygame.display.update()
            self._check_events()
            self.player.blitme()


def main():
    # Make a game instance,and run the game
    ai = Survive()
    ai.run_game()


if __name__ == '__main__':
    main()
