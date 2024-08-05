# ------------------------------------------------------------------------
# Author: Jesse Hancock
# Title: player.py
# Description: Created for survive game
# Date Created: 8/4/2024
# Last Updated: 8/4/2024
# ------------------------------------------------------------------------

import pygame

from settings import Settings


class Player:
    """A class to manage the player"""

    def __init__(self, ai_game):
        """Sets the image for the player"""

        # Assigns the screen to an attribute of player
        self.screen = ai_game.screen
        self.settings = ai_game.settings

        # Gets the rect, helps place ship in right place
        self.screen_rect = ai_game.screen.get_rect()

        # Loads the square image for the player and gets its rect
        self.image = pygame.image.load('images/square.png')
        self.rect = self.image.get_rect()

        # Sets rect to center, places player in the center
        self.rect.center = self.screen_rect.center

        # Stores floats for the ships exact position
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

        self.square = pygame.transform.scale(self.image, (35, 35))
        self.rect = self.image.get_rect()

        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False

    def blitme(self):
        """Draw the player at the screen on its current location."""
        self.screen.blit(self.square, self.rect)

    def update(self):
        """Updates x and y coordinates if moving."""
        if self.moving_right:
            self.x += 1
        if self.moving_left:
            self.x -= 1
        if self.moving_up:
            self.y -= 1
        if self.moving_down:
            self.y += 1
        self.rect.x = self.x
        self.rect.y = self.y