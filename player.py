import pygame

from settings import Settings


class Player:
    def __init__(self):
        """Instansiera spelaren och dennes förutsättningar."""
        self.settings = Settings()
        self.gravity = self.settings.player_gravity
        self.speed = self.settings.player_speed
        self.jump_height = self.settings.player_jump_height
        self.is_jumping = False  # Flaggvariabel för att påbörja ett hopp.
        self.step = 0  # Används för att alternera image_running1 och image_running2.

        # Spelplanens gränser.
        self.screen = self.settings.screen
        self.screen_rect = self.settings.screen_rect

        # Ladda spelarens bilder.
        self.image_idle = pygame.image.load("images/adventurer_idle.png")
        self.image_jumping = pygame.image.load("images/adventurer_jump.png")
        self.image_running1 = pygame.image.load("images/adventurer_action1.png")
        self.image_running2 = pygame.image.load("images/adventurer_action2.png")

        self.image = self.image_idle
        self.rect = self.image.get_rect()  # Mät spelarens gränser.

        self._spawn()

    def blitme(self):
        """Ritar sig på skärmen."""
        self.screen.blit(self.image, self.rect)

    def update(self):
        """Updaterar sin position."""
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
        else:
            if self.step % 2 == 0:
                self.image = self.image_running1
            else:
                self.image = self.image_running2

        # Uppdatera spelarens gränser, i det fall att spelaren hoppar eller duckar.
        self.rect = self.image.get_rect()

    def jump(self):
        """Spelaren innleder ett hopp."""
        self.speed = self.jump_height
        self.is_jumping = True

    def _spawn(self):
        """
        Placera ut spelaren på spelskärmen.

        Spelarens nedre vänsterkant placeras diktan med spelskärmens nedre vänsterkant.
        """
        self.rect.bottomleft = self.screen_rect.bottomleft
