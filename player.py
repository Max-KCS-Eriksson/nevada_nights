from pathlib import Path

import pygame

from base_classes import AbstractBaseGameElement


ASSETS_PATH = Path(__file__).parent.resolve() / "assets"


class Player(AbstractBaseGameElement):
    """
    Hanterar spelaren och dess resurser.

    Ärver metoder och attribut från abcs.AbstractBaseGameElement och utökar dess
    funktionalitet.
    """

    def __init__(self, game):
        """Instansiera spelaren och dennes förutsättningar."""

        # Ladda spelarens bilder.
        self._image_idle = pygame.image.load(ASSETS_PATH / "adventurer_idle.png")
        self._image_jumping = pygame.image.load(ASSETS_PATH / "adventurer_jump.png")
        self._image_running1 = pygame.image.load(ASSETS_PATH / "adventurer_action1.png")
        self._image_running2 = pygame.image.load(ASSETS_PATH / "adventurer_action2.png")
        self._image_crouching = pygame.image.load(ASSETS_PATH / "adventurer_duck.png")

        self.image = self._image_idle

        # Ärv egenskaper.
        super().__init__(game)

        # Ladda spelarens inställningar.
        self.gravity = self.settings.player_gravity
        self.speed = self.settings.player_speed
        self.jump_height = self.settings.player_jump_height

        # Flaggvariabel för spelarens rörelser.
        self.is_jumping = False
        self.is_crouching = False

        self._step = 0  # Används för att alternera _image_running1 och _image_running2.

        self._spawn()

    def update(self):
        """Uppdaterar sin position och animation."""
        if self._step == 80:
            # Låt inte överstiga 79.
            self._step = 0
        else:
            # Inkrementera om under 80.
            self._step += 1

        # Spelaren går.
        if not self.is_jumping:
            # Byt bild var 40e steg.
            if self._step < 40:
                self.image = self._image_running1
            else:
                self.image = self._image_running2
        # Spelaren hoppar.
        else:
            self.image = self._image_jumping

            # Öka fallets hastighet tills att marken är nådd.
            self.rect.y += self.speed
            self.speed += self.gravity
            if self.rect.bottom >= self.screen_rect.bottom:
                self.speed = 0
                self.is_jumping = False
                # Se till att spelaren inte hamnar under marken.
                self._spawn()

        # Förläng med förälderns metod.
        super().update()

        # Spelaren kryper.
        # Måste vara efter super().update() för att ändra positionering av 'hitbox'.
        if self.is_crouching:
            self.image = self._image_crouching

            # Sänk spelaren 'hitbox' för att ta sig under hinder.
            # Hur högt över marken som toppen av spelarens hitbox är utan att ducka.
            player_hitbox_top = 82
            self.hitbox.top = self.rect.bottom - player_hitbox_top * 0.6

    def jump(self):
        """Spelaren inleder ett hopp."""
        self.speed = self.jump_height
        self.is_jumping = True

    def crouch(self):
        """Spelaren hukar sig."""
        self.is_crouching = True

    def _spawn(self):
        """
        Placera ut spelaren på spelskärmen.

        Spelarens nedre vänsterkant placeras i spelskärmens nedre vänsterkant, med liten
        marginal till vänster.
        """
        x = self.screen_rect.left + 100
        y = self.screen_rect.bottom
        self.rect.bottomleft = (x, y)
