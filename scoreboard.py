import pygame


class Scoreboard:
    """En klass för rapportering av poäng och spelstatistik."""

    def __init__(self, game):
        """Instansiera attribut för poängräkning."""
        self.game = game
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
        self.prep_player_lives()
        self.prep_level()

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
        high_score_str = "{:,}".format(self.stats.high_score)

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
            # Sätt nuvarande poäng som 'high score'.
            self.stats.high_score = self.stats.score
            self.prep_high_score()

            # Kalla på metod för att skriva 'high score' till fil.
            self.stats.write_high_score(self.stats.high_score)

    def prep_player_lives(self):
        """Visa hur många liv spelaren har kvar."""
        # Formatera sträng, och väg upp fär off-by-one.
        player_lives_left_str = "Lives: {}".format(self.stats.player_lives_left + 1)

        # Rendera stängvärde som bild.
        self.player_lives_left_image = self.font.render(
            player_lives_left_str, True, self.text_color, self.settings.bg_color
        )

        # Placera i vänstra hörnet.
        self.player_lives_left_rect = self.high_score_image.get_rect()
        self.player_lives_left_rect.left = self.screen_rect.left + 20
        # Matcha den övre marginalen med poängräkningens.
        self.player_lives_left_rect.top = self.score_rect.top

    def prep_level(self):
        """Formatera nivån och rendera det som en bild."""
        # Formatera sträng.
        level_str = "Level: {}".format(self.stats.level)

        # Rendera stängvärde som bild.
        self.level_image = self.font.render(
            level_str, True, self.text_color, self.settings.bg_color
        )

        # Positionera under spelarens liv.
        self.level_rect = self.level_image.get_rect()
        self.level_rect.left = self.player_lives_left_rect.left
        self.level_rect.top = self.player_lives_left_rect.bottom + 10

    def prep_all(self):
        """Formatera alla poäng och rendera det som en bild."""
        self.prep_score()
        self.prep_high_score()
        self.prep_player_lives()
        self.prep_level()

    def show_score(self):
        """Rita upp alla poängtavlor."""
        self.screen.blit(self.score_image, self.score_rect)
        self.screen.blit(self.high_score_image, self.high_score_rect)
        self.screen.blit(self.player_lives_left_image, self.player_lives_left_rect)
        self.screen.blit(self.level_image, self.level_rect)
