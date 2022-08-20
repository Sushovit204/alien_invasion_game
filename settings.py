class Settings:
    """A class to store all the settings for the Alien Invasion Game"""

    def __init__(self):
        """Initialize the game's settings"""
        # Screen Settings
        self.screen_width = 2000
        self.screen_height = 800
        self.bg_color = (118, 118, 118)
        # ship setting
        self.ship_speed = 1.5
        # Bullet setings
        self.bullet_speed = 1.0
        self.bullet_width = 8
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)
        self.bullets_allowed = 5
        # Alien Settings
        self.alien_speed = 1.0
        self.fleet_drop_speed = 0
        # fleet_direction of 1 represents right and -1 represents left
        self.fleet_direction = 1
