# ------------------------------------------------------------------------
# Author: Jesse Hancock
# Date Created: 8/4/2024
# Last Updated: 8/4/2024
# Description: Manages bullets in Survive game
# -----------------------------------------------------------------------

import pygame
from pygame.sprite import Sprite

class Bullet:
    """A class to manage bullets in bullet.py"""

    def __init__(self, ai_game):
        """Sets up bullets"""
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.color = self.settings.bullet_color

        # Create a bullet rect at (0,0) for testing
        self.rect = pygame.rect(0,0, self.settings.bullet_width, self.settings.bullet_height)
