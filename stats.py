"""
Class that records the current stats of the game (level, and everything connected
to game difficulty within each level).
"""
class GameStats():
    """Same as above."""
    def __init__(self, settings):
        """Initializes the initial game stats."""
        self.lives_left = settings.max_player_lives
        self.score = 0

        # Highscore should never be reset
        self.high_score = 0

        self.game_active = False

        self.curr_level = 1

    def reset_stats(self, settings):
        """Resets the stats if the player has no lives left."""
        self.lives_left = settings.max_player_lives
        self.score = 0
