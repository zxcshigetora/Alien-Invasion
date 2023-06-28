class GameStats:
    def __init__(self, stats):
        self.high_score = 0
        self.settings = stats.settings
        self.reset_stats()
        self.game_active = False

    def reset_stats(self):
        self.ship_left = self.settings.ship_limit
        self.score = 0
        self.level = 1
