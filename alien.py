import pygame
from pygame.sprite import Sprite


class Alien(Sprite):
    """A class to represent a single alien in a fleet"""

    def __init__(self, ai_game):
        """initialize the alien and set it's starting position"""
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings

        # Load the alien image and set it's rect attribute
        self.image = pygame.image.load('images/alien.bmp')
        self.rect = self.image.get_rect()

        # Start each new alien near the top left screen
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # Store the alien exact horizontal's position
        self.x = float(self.rect.x)

    def check_edges(self):
        """Return True if alien is at edge of the screen"""
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right or screen_rect.left <= 0:
            return True

    def update(self):
        """Move alien to the right"""
        self.x += (self.settings.alien_speed*self.settings.fleet_direction)
        self.rect.x = self.x
