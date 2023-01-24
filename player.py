import pygame

from abcs import AbstractBaseGameElement
from settings import Settings


class Player(AbstractBaseGameElement):
    """
    Hanterar spelaren och dess resurser.

    Ärver metoder och attribut från abcs.AbstractBaseGameElement och utökar dess
    funktionalitet.
    """

    def __init__(self):
        """Instansiera spelaren och dennes förutsättningar."""
        # Ladda spelarens inställningar
        self.settings = Settings()
        self.gravity = self.settings.player_gravity
        self.speed = self.settings.player_speed
        self.jump_height = self.settings.player_jump_height
        self.is_jumping = False  # Flaggvariabel för att påbörja ett hopp.
        self.step = 0  # Används för att alternera image_running1 och image_running2.

        # Ladda spelarens bilder.
        self.image_idle = pygame.image.load("images/adventurer_idle.png")
        self.image_jumping = pygame.image.load("images/adventurer_jump.png")
        self.image_running1 = pygame.image.load("images/adventurer_action1.png")
        self.image_running2 = pygame.image.load("images/adventurer_action2.png")

        self.image = self.image_idle

        # Ärv egenskaper.
        super().__init__()

        self._spawn()

    def update(self):
        """Uppdaterar sin position."""
        self.step += 1

        if self.is_jumping:
            self.image = self.image_jumping

            # Öka fallets hastighet tills att marken är nådd.
            self.rect.y += self.speed
            self.speed += self.gravity
            if self.rect.bottom >= self.screen_rect.bottom:
                self.speed = 0
                self.is_jumping = False
                self.image = self.image_running1
                # Se till att spelaren inte hamnar under marken..s
                self._spawn()
        else:
            if self.step % 2 == 0:
                self.image = self.image_running1
            else:
                self.image = self.image_running2

        # Förläng med förälderns metod.
        super().update()

    def jump(self):
        """Spelaren inleder ett hopp."""
        self.speed = self.jump_height
        self.is_jumping = True

    def _spawn(self):
        """
        Placera ut spelaren på spelskärmen.

        Spelarens nedre vänsterkant placeras i spelskärmens nedre vänsterkant, med liten
        marginal till vänster.
        """
        x = self.screen_rect.left + 100
        y = self.screen_rect.bottom
        self.rect.bottomleft = (x, y)
