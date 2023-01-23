import pygame

from settings import Settings


class GroundObstacle:
    def __init__(self):
        """Instansiera hindret och dess förutsättningar."""
        self.settings = Settings()
        self.speed = self.settings.obstacle_speed
        self._respawn_rate = self.settings.obstacle_respawn_rate

        # Spelplanens gränser.
        self.screen = self.settings.screen
        self.screen_rect = self.settings.screen_rect

        # Ladda hindrets bilder.
        self.image = pygame.image.load("images/cactus.png")
        self.rect = self.image.get_rect()  # Mät hindrets gränser.

        self._spawn()

    def blitme(self):
        """Ritar sig på skärmen."""
        self.screen.blit(self.image, self.rect)

    def update(self):
        """Updaterar sin position."""
        # Förflytta i vänster riktning.
        self.rect.x -= self.speed

        # Kolla om hindret är utanför spelplanen.
        if self._is_out():
            self._spawn()

    def _spawn(self):
        """
        Placera hindret utanför nedre högra hörnet av spelskärmen.

        Avståndet utanför hörnet bestämms av det privata attributet ._respawn_rate.
        """
        self.rect.bottomleft = self.screen_rect.bottomright + self._respawn_rate

    def _is_out(self):
        """
        Kolla om hindret har passerat ut från spelskärmen.

        Returnerar booleskt värde.
        """
        if self.rect.right <= self.screen.left:
            return True

        return False
