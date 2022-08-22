class GameStats:
    """Tracking the game progress."""

    def __init__(self, ai_game):
        """Initialize the stats"""
        self.settings = self.ai_game.settings
        self.reset_stats()
