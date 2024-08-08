# ------------------------------------------------------------------------------------------
# Author: Jesse Hancock
# Title of game: Survive!
# Description: main file of the game, the goal is to dodge all the obstacles
# Date Created: 8/4/2024
# Last Updated: 8/4/2024
# -----------------------------------------------------------------------------------------
#            self.player.set_position(50,50) (for later)
# This is the package that will run the game
import pygame

# This helps run the player
from player import Player

# This is the package that will use tools to exit the game when the player quits
import sys

# This is the package that manages game settings
from settings import Settings

import bullet
from bullet import Bullet

# Allows random numbers from the random class
import random


class Survive:
    """Overall class to manage game assets and behavior"""

    def __init__(self):

        self.settings = Settings()

        """Initialize the game and create game resources."""
        pygame.init()

        # This controls the game frame rate
        self.clock = pygame.time.Clock()

        # Sets the title in the top left corner of the screen
        pygame.display.set_caption("Survive")

        # Sets the screen height and width from the settings class
        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))

        # Sets the background color to black
        self.bg_color = (0, 0, 0)

        # Fills the screen with background color
        self.screen.fill(self.bg_color)

        # Creates instance of player class
        self.player = Player(self)

        # Helps with bullet class
        self.Bullet = Bullet(self)
        self.bullets = pygame.sprite.Group()

        # Values for player position
        self.player_x = 0
        self.player_y = 0

        self.moving_right = False

        self.obstacle_one = False

        self.bullet_x = 0
        self.bullet_y = 0

        # Sets the time between obstacles to time variable in the settings class
        self.time_between_obstacles = self.settings.time

        self.bullet = Bullet(self)

    def _check_events(self):
        """Respond to key presses and mouse events."""

        # Watch for keyboard and mouse events.
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._key_down_events(event)
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_RIGHT:
                    self.player.moving_right = False
                if event.key == pygame.K_UP:
                    self.player.moving_up = False
                if event.key == pygame.K_LEFT:
                    self.player.moving_left = False
                if event.key == pygame.K_DOWN:
                    self.player.moving_down = False

    def _key_down_events(self, event):
        if event.key == pygame.K_LEFT:
            self.player.moving_left = True
        if event.key == pygame.K_RIGHT:
            self.player.moving_right = True
        if event.key == pygame.K_DOWN:
            self.player.moving_down = True
        if event.key == pygame.K_UP:
            self.player.moving_up = True

    def run_game(self):
        """Runs the game"""
        while True:
            pygame.display.update()
            # Checks keyboard interactions
            self._check_events()
            # Updates screen
            self.update_screen()

            self.new_obstacle()

    def update_screen(self):
        """Updates images on the screen, and flip to the new screen."""
        # Redraw the screen during each pass through the loop.
        self.screen.fill(self.bg_color)

        self.player.update()

        # starts the blitme function in bullet.py
        self.Bullet.blitme()

        # starts the blitme function in player.py
        self.player.blitme()

        # Gets position for the player
        self.player_x = self.player.get_position_x()
        self.player_y = self.player.get_position_y()

    def new_obstacle(self):
        """Starts a random obstacle"""
        obstacle = random.randint(1, 1)
        if obstacle == 1:
            self.obstacle_one = True
            self.start_obstacle_onee()

    def start_obstacle_onee(self):
        """Starts obstacle number 1"""
        self.bullet_x = self.bullet.start_obstacle_one()
        print(self.bullet_x)
        self.bullet_y = 300
        self.bullet.update_position(self.bullet_x, self.bullet_y)


def main():
    # Make a game instance,and run the game
    ai = Survive()
    ai.run_game()

if __name__ == '__main__':
    main()
