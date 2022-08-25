class Settings:
    """A class to store all the settings for the Alien Invasion Game"""

    def __init__(self):
        """Initialize the game's static settings"""
        # Screen Settings
        self.screen_width = 1080
        self.screen_height = 2000
        self.bg_color = (118, 118, 118)
        # ship setting
        self.ship_speed = 1.5
        self.ship_limit = 2
        # Bullet setings
        self.bullet_speed = 1.0
        self.bullet_width = 10
        self.bullet_height = 30
        self.bullet_color = (60, 60, 60)
        self.bullets_allowed = 5
        # Alien Settings
        self.alien_speed = 1.0
        # this fleet_drop_speed should be 1 as the fleet should come down after reaching edge
        # but some problem causes the fleet to come down at once
        self.fleet_drop_speed = 0.1

        # fleet_direction of 1 represents right and -1 represents left
        self.fleet_direction = 1

        # How quickly the game speeds up
        self.speedup_scale = 1.5

        # How quickly the alient point value increases
        self.score_scale = 1.5

        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        """Initializing the settings that change throughout the game"""
        self.ship_speed = 1.5
        self.bullet_speed = 1.0
        self.alien_speed = 1.0

        # Scoring
        self.alien_point = 10

        # fleet direction of 1 represents right and -1 represents left
        self.fleet_direction = 1

    def increase_speed(self):
        """Increase speed settings and alien points values"""
        self.bullet_speed *= self.speedup_scale
        self.alien_speed *= self.speedup_scale
        self.ship_speed *= self.speedup_scale

        self.alien_points = int(self.alien_point * self.score_scale)
