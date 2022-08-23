class GameStats:
    """Tracking the game progress."""

    def __init__(self, ai_game):
        """Initialize the stats"""
        self.settings = ai_game.settings
        self.reset_stats()

        # Setting a game active flag
        self.game_active = False

    def reset_stats(self):
        """Initialize statsics that can change during the game"""
        self.ships_left = self.settings.ship_limit
