import pygame


class Ship:
    """A class to manage the ship"""

    def __init__(self, ai_game):
        """Initialzie the  ship and  set its starting position."""
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()

        # Load the ship image and get the rect
        self.image = pygame.image.load('images/spaceship.bmp')
        self.rect = self.image.get_rect()

        # start each new ship at the bottom of the map
        self.rect.midbottom = self.screen_rect.midbottom

        # Movement Flag
        self.moving_right = False
        self.moving_left = False

    def update(self):
        """Update the ship's position based on the movement flag"""
        if self.moving_right:
            self.rect.x += 1
        if self.moving_left:
            self.rect.x -= 1

    def blitme(self):
        """Draw the ship at its current location"""
        self.screen.blit(self.image, self.rect)
