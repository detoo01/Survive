# ------------------------------------------------------------------------
# Author: Jesse Hancock
# Date Created: 8/4/2024
# Last Updated: 8/4/2024
# Description: Manages bullets in Survive game
# -----------------------------------------------------------------------
from random import random, randint
import time

import pygame
from pygame.sprite import Sprite


class Bullet:
    """A class to manage bullets in bullet.py"""

    def __init__(self, ai_game):
        #self.main = main.Survive()
        """Sets up bullets"""
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.color = ai_game.settings.bullet_color
        self.rect_x = 1000
        self.rect_y = 255

        # Create a bullet rect at (255,255) for testing
        self.rect = pygame.Rect(self.rect_x, self.rect_y, self.settings.bullet_width, self.settings.bullet_height)

    def blitme(self):
        """Draw the bullet to the screen"""
        self.rect = pygame.Rect(self.rect_x, self.rect_y, self.settings.bullet_width, self.settings.bullet_height)
        pygame.draw.rect(self.screen, self.color, self.rect)

    def update_position(self, x, y):
        """Updates bullet position"""
        self.rect_x = x
        self.rect.y = y

    def start_obstacle_one(self):
        """Returns random number from 1 to 1366"""
        return randint(1, 1366)
