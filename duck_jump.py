import sys

import pygame

from settings import Settings
from gamestats import GameStats
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
        self.screen_rect = self.settings.screen_rect
        pygame.display.set_caption("Duck and Jump")  # Titel på spelets fönster.

        # Instansiera spelets statistik.
        self.stats = GameStats(self)

        # Instansiera spelets spelare.
        self.player = Player()

        # Skapa grupp med instanser av spelets hinder.
        self.obstacles = pygame.sprite.Group()  # Hantera en mängd hinder samtidigt.
        self._create_obstacles()

    def run_game(self):
        """Spelets körning."""
        while True:
            # Kolla efter input från användaren.
            self._check_events()

            # Uppdatera spelaren och hindren.
            self.player.update()
            self._update_obstacles()

            # Uppdatera skärmen.
            self._update_screen()

    def _update_screen(self):
        """Updaterar skärmen of 'flippar' till en ny bild."""
        # Rita spelets bakgrund och element.
        self.screen.fill(self.settings.bg_color)
        self.player.blitme()
        self.obstacles.draw(self.screen)  # Rita hela gruppen hinder.

        # 'Flippa' till en ny bild.
        pygame.display.flip()

    def _create_obstacles(self):
        obstacle = GroundObstacle()
        self.obstacles.add(obstacle)

    def _update_obstacles(self):
        self.obstacles.update()

        # Ta bort hinder som har passerat ut från spelskärmen.
        for obstacle in self.obstacles.copy():
            if obstacle.rect.right <= self.screen_rect.left:
                self.obstacles.remove(obstacle)

        self._check_obstacles()

    def _check_obstacles(self):
        # Skapa fler hinder om det inte finns några.
        if not self.obstacles:
            self._create_obstacles()

        # Kolla efter kollision med spelaren.
        if pygame.sprite.spritecollideany(self.player, self.obstacles):
            # Agera på kollision.
            self.stats.reset_stats()

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
