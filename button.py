import pygame
import pygame.font


class Button:
    def __init__(self, game, text):
        """Instansiera knappens attribut."""
        self.screen = game.screen
        self.screen_rect = self.screen.get_rect()

        # Knappens dimensioner och egenskaper.
        self.width, self.height = 400, 100
        self.button_color = (0, 125, 255)
        self.text_color = (255, 255, 255)
        self.font = pygame.font.SysFont(None, 72)

        # Bygg knappens rectobjeckt och centrera den.
        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect.center = self.screen_rect.center

        self._prep_text(text)

    def _prep_text(self, text):
        """Rendera en centrerad bild av text given som argument för textparametern."""
        self.text_image = self.font.render(
            text, True, self.text_color, self.button_color
        )
        self.text_image_rect = self.text_image.get_rect()
        self.text_image_rect.center = self.rect.center

    def draw_button(self):
        """Rita upp knappen."""
        # Rita en tom knapp först, och sedan texten ovanpå.
        self.screen.fill(self.button_color, self.rect)
        self.screen.blit(self.text_image, self.text_image_rect)
