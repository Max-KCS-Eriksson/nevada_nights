import pygame

from settings import Settings


class Obstacle:
    def __init__(self) -> None:
        self.settings = Settings()
        self.speed = self.settings.obstacle_speed

        self.screen = self.settings.screen
        self.screen_rect = self.settings.screen_rect

        self.image = pygame.image.load("images/cactus.png")
        self.rect = self.image.get_rect()

        # Placera hindret i utanför nedre högra hörnet av spelskärmen.
        self.rect.bottomleft = self.screen_rect.bottomright

    def blitme(self):
        self.screen.blit(self.image, self.rect)

    def update(self):
        self.rect.x -= self.speed

        if self.rect.x <= self.settings.obstacle_respawn_rate:
            self.rect.bottomleft = self.screen_rect.bottomright
