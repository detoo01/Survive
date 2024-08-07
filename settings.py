# --------------------------------------------------------------------
# Author: Jesse Hancock
# Description: manages game settings
# Date Created: 8/4/2024
# Last Updated: 8/4/2024
# --------------------------------------------------------------------

class Settings:
    """A class to store all settings for survive"""

    def __init__(self):
        self.screen_width = 1366
        self.screen_height = 700
        self.bg_color = (255, 255, 255)

        # Bullet settings:
        self.bullet_width = 10.0
        self.bullet_height = 25.0
        self.bullet_color = (255, 0, 0)


        # DEFAULT SETTINGS
        #        self.bullet_width = 10.0
        #self.bullet_height = 25.0
        # DEFAULT SETTINGS ^^^^^