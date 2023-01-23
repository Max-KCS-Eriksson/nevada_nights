class GameStats:
    """Håller räkningen på spelets statistik."""

    def __init__(self, game):
        """
        Instansiera spelets statistik med statiska attribut.

        Tar en instans av spelet som argument för parametern "game".
        """
        self.settings = game.settings
        self.reset_stats()

    def reset_stats(self):
        """Nollställ dynamiska attribut."""
        self.player_lives_left = self.settings.player_lives_max
        self.score = 0
