#------------------------------------------------------------------------
# Author: Jesse Hancock
# Title: player.py
# Description: Created for survive game
# Date Created: 8/4/2024
# Last Updated: 8/4/2024
#------------------------------------------------------------------------

import pygame

class player:
    """A class to manage the player"""

    def __init__(self):
        """Sets the image for the player"""

        self.image = pygame.image.load('images/square.png')
        self.rect = self.image.get_rect()
