import sys
# the tools in sys module can be used to quit the game when the player wants

import pygame


class AlienInvasion:
    """Overall class to manage game assests and behaviours."""

    def __init__(self):
        """Initialize the game and create resources."""
        pygame.init()

        # game window which will be 1200 pixel wide and 800 pixel height
        self.screen = pygame.display.set_mode((1200, 800))
        pygame.display.set_caption("Alien Invasion By @Sushovit204")

    def run_game(self):
        """Start the main loop for the game."""
        while True:
            # Watch for keyboard and mouse events.
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

            # Make the most recently drawn screen visible.
            pygame.display.flip()


if __name__ == '__main__':
    # Make a game instance and run the game.
    ai = AlienInvasion()
    ai.run_game()
