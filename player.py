#------------------------------------------------------------------------
# Author: Jesse Hancock
# Title: player.py
# Description: Created for survive game
# Date Created: 8/4/2024
# Last Updated: 8/4/2024
#------------------------------------------------------------------------

import pygame


class Player:
    """A class to manage the player"""

    def __init__(self, ai_game):
        """Sets the image for the player"""

        self.image = pygame.image.load('images/square.png')
        self.square = pygame.transform.scale(self.image, (50,50) )
        self.rect = self.image.get_rect()
        self.screen = ai_game.screen



    def blitme(self):
        """Draw the player at the screen"""
        self.screen.blit(self.square, self.rect)