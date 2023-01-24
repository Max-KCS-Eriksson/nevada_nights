import pygame.font


class Scoreboard:
    """En klass för rapportering av poäng och spelstatistik."""

    def __init__(self, game):
        """Instansiera attribut för poängräkning."""
        self.screen = game.screen
        self.screen_rect = self.screen.get_rect()
        self.settings = game.settings
        self.stats = game.stats

        # Typsnittsinställningar för poäng info.
        self.text_color = (255, 255, 255)
        self.font = pygame.font.SysFont(None, 48)

        # Förbered den initiala poängtavlan.
        self.prep_score()
        self.prep_high_score()

    def prep_score(self):
        """Formatera poängen och rendera det som en bild."""
        # Formatera poäng med kommateckensavskiljare för tusental.
        score_str = "{:,}".format(self.stats.score)

        # Rendera stängvärde som bild.
        self.score_image = self.font.render(
            score_str, True, self.text_color, self.settings.bg_color
        )

        # Visa poäng högst upp i vänster hörn.
        self.score_rect = self.score_image.get_rect()
        self.score_rect.right = self.screen_rect.right - 20
        self.score_rect.top = 20

    def prep_high_score(self):
        """Formatera 'high score' och rendera det som en bild."""
        # Formatera poäng med kommateckensavskiljare för tusental.
        high_score = round(self.stats.high_score, -1)
        high_score_str = "{:,}".format(high_score)

        # Rendera stängvärde som bild.
        self.high_score_image = self.font.render(
            high_score_str, True, self.text_color, self.settings.bg_color
        )

        # Centrera 'high score' högst upp i bild.
        self.high_score_rect = self.high_score_image.get_rect()
        self.high_score_rect.centerx = self.screen_rect.centerx
        # Matcha den övre marginalen med poängräkningens.
        self.high_score_rect.top = self.score_rect.top

    def check_high_score(self):
        """Kontrollera om ett nytt 'high score' har satts."""
        if self.stats.score > self.stats.high_score:
            self.stats.high_score = self.stats.score
            self.prep_high_score()

    def show_score(self):
        """Visa nuvarande poäng och 'high score'."""
        self.screen.blit(self.score_image, self.score_rect)
        self.screen.blit(self.high_score_image, self.high_score_rect)
