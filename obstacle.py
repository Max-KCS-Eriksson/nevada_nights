import pygame

from settings import Settings


class GroundObstacle(pygame.sprite.Sprite):
    """Ett hinder som ärver metoder från Sprite-klassen."""

    def __init__(self):
        """
        Instansiera hindret med ärvda metoder från förälderklassen, samt hindrets
        förutsättningar.

        De ärvda metoderna möjliggör att instanser av klassen kan hanteras i "sprit.Group",
        som är ett listliknande objekt med metoder för att hantera flera tillgångar
        samtidigt.
        """
        # Ärv egenskaper.
        super().__init__()

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

    def _spawn(self):
        """
        Placera hindret utanför nedre högra hörnet av spelskärmen.

        Avståndet utanför hörnet bestämms av det privata attributet _respawn_rate.
        """
        # Packa upp det oföränderliga tuple-värdet och addera värdet av _respawn_rate.
        screen_right, screen_bottom = self.screen_rect.bottomright
        self.rect.bottomleft = (screen_right + self._respawn_rate, screen_bottom)
