import sys

import pygame

from settings import Settings
from player import Player
from obstacle import GroundObstacle


class DuckAndJump:
    def __init__(self):
        """
        Instansiera spelet med inställningar, skärm, spelaren, och hinder attribut.
        """
        # Starta pygame.
        pygame.init()

        # Spelets inställningar och skärm.
        self.settings = Settings()
        self.screen = self.settings.screen
        pygame.display.set_caption("Duck and Jump")  # Titel på spelets fönster.

        # Spelets spelare och hinder.
        self.player = Player()
        self.ground_obstacle = GroundObstacle()

    def run_game(self):
        """Spelets körning."""
        while True:
            # Kolla efter input från användaren.
            self._check_events()

            # Uppdatera spelaren och hindren.
            self.player.update()
            self.ground_obstacle.update()

            # Uppdatera skärmen.
            self._update_screen()

    def _update_screen(self):
        """Updaterar skärmen of 'flippar' till en ny bild."""
        # Rita spelets bakgrund och element.
        self.screen.fill(self.settings.bg_color)
        self.player.blitme()
        self.ground_obstacle.blitme()

        # 'Flippa' till en ny bild.
        pygame.display.flip()

    def _check_events(self):
        """Kolla efter tangentbords- och mushändelser."""
        for event in pygame.event.get():
            # Klickar kryssrutan eller anvönder genväg för att stänga fönster.
            if event.type == pygame.QUIT:
                sys.exit()

            # Nedtryckning av tangentbordsknappar.
            elif event.type == pygame.KEYDOWN:
                # Styrning av spelaren.
                if event.key == pygame.K_UP:
                    self.player.jump()


if __name__ == "__main__":
    # Instansiera spelet och kalla på dess metod för att starta spelets loop.
    game = DuckAndJump()
    game.run_game()
