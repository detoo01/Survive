#------------------------------------------------------------------------------------------
# Author: Jesse Hancock
# Title of game: Survive!
# Description: main file of the game, the goal is to dodge all the obstacles
# Date Created: 8/4/2024
# Last Updated: 8/4/2024
#-----------------------------------------------------------------------------------------

# This is the package that will run the game
import pygame

# This is the package that will use tools to exit the game when the player quits
import sys

class Survive:
    """Overall class to manage game assets and behavior"""

    def __init__(self):
        """Initialize the game and create game resources."""
        pygame.init()


