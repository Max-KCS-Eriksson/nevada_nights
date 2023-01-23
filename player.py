import pygame

from settings import Settings


class Player:
    def __init__(self, game) -> None:
        self.settings = Settings()
        self.gravity = self.settings.player_gravity
        self.speed = self.settings.player_speed
        self.jump_height = self.settings.player_jump_height
        self.is_jumping = False
        self.step = 0  # Används för att alternera image_running1 och image_running2.

        self.screen = game.screen
        self.screen_rect = game.screen.get_rect()

        self.image_idle = pygame.image.load("images/adventurer_idle.png")
        self.image_jumping = pygame.image.load("images/adventurer_jump.png")
        self.image_running1 = pygame.image.load("images/adventurer_action1.png")
        self.image_running2 = pygame.image.load("images/adventurer_action2.png")

        self.image = self.image_idle
        self.rect = self.image.get_rect()

        # Placera spelarens nedre vänsterkant diktan med spelskärmens nedre vänsterkant.
        self.rect.bottomleft = self.screen_rect.bottomleft

    def blitme(self):
        self.screen.blit(self.image, self.rect)

    def update(self):
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

    def jump(self):
        self.speed = self.jump_height
        self.is_jumping = True
