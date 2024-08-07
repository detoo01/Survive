# ------------------------------------------------------------------------
# Author: Jesse Hancock
# Date Created: 8/4/2024
# Last Updated: 8/4/2024
# Description: Manages bullets in Survive game
# -----------------------------------------------------------------------
from random import random, randint

import pygame
from pygame.sprite import Sprite


class Bullet:
    """A class to manage bullets in bullet.py"""

    def __init__(self, ai_game):
        """Sets up bullets"""
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.color = ai_game.settings.bullet_color

        # Create a bullet rect at (255,255) for testing
        self.rect = pygame.Rect(1000, 255, self.settings.bullet_width, self.settings.bullet_height)


    def blitme(self):
        pygame.draw.rect(self.screen, self.color, self.rect)

    def start_obstacle(self):
        position = randint(1, 1366)
