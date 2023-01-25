from pathlib import Path
import random

import pygame

from base_classes import BaseObstacle


ASSETS_PATH = Path(__file__).parent.resolve() / "assets"


class GroundObstacle(BaseObstacle):
    """Ett hinder på marken som ärver metoder från abcs.BaseObstacle och Sprite-klassen."""

    def __init__(self, game):
        """
        Instansiera hindret med ärvda metoder från förälderklassen, samt hindrets
        förutsättningar.
        """
        # Ladda hindrets bild.
        self.image = pygame.image.load(ASSETS_PATH / "cactus.png")

        # Ärv attribut och metoder.
        super().__init__(game)

        # Ladda inställningar.
        self.speed = self.settings.obstacle_speed
        self.spawn_distance = self.settings.obstacle_spawn_distance

        self._spawn()

    def _spawn(self):
        """
        Placera hindret utanför nedre högra hörnet av spelskärmen.

        Avståndet utanför hörnet bestämms av attributet spawn_distance.
        """
        # Packa upp det oföränderliga tuple-värdet och addera värdet av spawn_distance.
        screen_right, screen_bottom = self.screen_rect.bottomright
        self.rect.bottomleft = (screen_right + self.spawn_distance, screen_bottom)


class AirObstacle(BaseObstacle):
    """Ett hinder i luften som ärver metoder från abcs.BaseObstacle och Sprite-klassen."""

    def __init__(self, game):
        """
        Instansiera hindret med ärvda metoder från förälderklassen, samt hindrets
        förutsättningar.
        """
        # Ladda hindrets bild.
        self._image_alien_beige = pygame.image.load(ASSETS_PATH / "alien_beige.png")
        self._image_alien_blue = pygame.image.load(ASSETS_PATH / "alien_blue.png")
        self._image_alien_green = pygame.image.load(ASSETS_PATH / "alien_green.png")
        self._image_alien_pink = pygame.image.load(ASSETS_PATH / "alien_pink.png")
        self._image_alien_yellow = pygame.image.load(ASSETS_PATH / "alien_yellow.png")

        # Tilldela en slumpmässig bild.
        self.image = random.choice(
            [
                self._image_alien_beige,
                self._image_alien_blue,
                self._image_alien_green,
                self._image_alien_pink,
                self._image_alien_yellow,
            ]
        )

        # Ärv attribut och metoder.
        super().__init__(game)

        # Ladda inställningar.
        self.speed = self.settings.obstacle_speed
        self.spawn_distance = self.settings.obstacle_spawn_distance

        self._spawn()

    def _spawn(self):
        """
        Placera hindret i luften.

        Avståndet utanför hörnet bestämms av attributet spawn_distance.
        """
        # Packa upp det oföränderliga tuple-värdet och addera värdet av spawn_distance.
        screen_right, screen_bottom = self.screen_rect.bottomright

        # Hur högt över marken som toppen av spelarens hitbox är utan att ducka.
        player_hitbox_top = 82

        self.rect.bottomleft = (
            screen_right + self.spawn_distance,
            # Flyg på en höjd av 95% av player_hitbox_top för att krocka med spelare.
            screen_bottom - player_hitbox_top * 0.95,
        )

    def update(self):
        """
        Skriv över ärvt beteende att centrera 'hitbox' i sin rect.

        Nedre kanten av 'hitbox' sätt mot nedre kanten av rect, vilket skapar en lägre
        kollisionsyta passande för ett hinder som spelaren ska ducka under.
        """
        # Åkalla förälderns metod.
        super().update()

        # Skriv över positioneringen av 'hitbox'.
        self.hitbox.bottom = self.rect.bottom
