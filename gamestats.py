from pathlib import Path


class GameStats:
    """Håller räkningen på spelets statistik."""

    def __init__(self, game):
        """
        Instansiera spelets statistik med statiska attribut.

        Tar en instans av spelet som argument för parametern "game".
        """
        self.settings = game.settings
        self.reset_stats()

        self.high_score_path = Path(__file__).parent.resolve() / ".highscore.txt"
        print(self.high_score_path)
        self.high_score = self._read_high_score()

        # Start spelet med inaktivt status.
        self.game_active = False

    def reset_stats(self):
        """Nollställ dynamiska attribut."""
        self.player_lives_left = self.settings.player_lives_max - 1  # Off-by-one.
        self.score = 0

    def _read_high_score(self):
        try:
            with open(self.high_score_path, "r") as file_object:
                return int(file_object.read())
        except FileNotFoundError:
            return 0

    def write_high_score(self, high_score):
        with open(self.high_score_path, "w") as file_object:
            file_object.write(str(high_score))
