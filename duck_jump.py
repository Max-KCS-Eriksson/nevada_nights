import sys

import pygame

from settings import Settings
from player import Player
from obstacle import Obstacle


class DuckAndJump:
    def __init__(self) -> None:
        pygame.init()

        self.settings = Settings()
        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height)
        )

        pygame.display.set_caption("Duck and Jump")

        self.player = Player(self)
        self.obstacle = Obstacle(self)

    def run_game(self):
        while True:
            self._check_events()
            self.obstacle.update()
            self.player.update()
            self._update_screen()

    def _update_screen(self):
        """Updaterar skärmen of 'flippar' till en ny skärm."""
        self.screen.fill(self.settings.bg_color)
        self.obstacle.blitme()
        self.player.blitme()

        pygame.display.flip()

    def _check_events(self):
        """Kolla efter tangentbords- och mushändelser."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

            # Styrning av spelaren.
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    self.player.jump()


if __name__ == "__main__":
    game = DuckAndJump()
    game.run_game()
