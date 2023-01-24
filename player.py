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

        # Mät spelarens utkant, och skapa en 'hitbox' som är mindre än utkanten.
        self.rect = self.image.get_rect()
        hitbox_width = self.rect.width / 2
        hitbox_height = self.rect.height / 2
        self.hitbox = self.rect.inflate(-hitbox_width, -hitbox_height)

        self._spawn()

    def blitme(self):
        """Ritar sig på skärmen."""
        self.screen.blit(self.image, self.rect)
        # self.screen.fill((0, 125, 255), self.hitbox)  # NOTE Used for DEBUG only.

    def update(self):
        """Updaterar sin position."""
        self.step += 1  # TODO Find better solution.

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

        # Centrera 'hitbox'.
        self.hitbox.center = self.rect.center

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
