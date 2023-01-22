import pygame

from settings import Settings


class Player:
    def __init__(self, game) -> None:
        self.settings = Settings()
        self.gravity = self.settings.player_gravity
        self.speed = self.settings.player_gravity
        self.jump_height = self.settings.player_jump_height
        self.is_jumping = False

        self.screen = game.screen
        self.screen_rect = game.screen.get_rect()

        self.image_idle = pygame.image.load("images/adventurer_idle.png")
        self.image_jumping = pygame.image.load("images/adventurer_jump.png")

        self.image = self.image_idle
        self.rect = self.image.get_rect()

        # Placera spelarens nedre vänsterkant diktan med spelskärmens nedre vänsterkant.
        self.rect.bottomleft = self.screen_rect.bottomleft

    def blitme(self):
        self.screen.blit(self.image, self.rect)

    def update(self):
        if self.is_jumping:
            self.image = self.image_jumping
            # Öka fallets hastighet tills att marken är nådd.
            self.rect.y += self.speed
            self.speed += self.gravity
            if self.rect.bottom >= self.screen_rect.bottom:
                self.speed = 0
                self.is_jumping = False
                self.image = self.image_idle

    def jump(self):
        self.speed = self.jump_height
        self.is_jumping = True
