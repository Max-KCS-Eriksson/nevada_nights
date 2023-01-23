import pygame

from settings import Settings


class Obstacle:
    def __init__(self, game) -> None:
        self.settings = Settings()
        self.speed = self.settings.obstacle_speed

        self.screen = game.screen
        self.screen_rect = game.screen.get_rect()

        self.image = pygame.image.load("images/cactus.png")
        self.rect = self.image.get_rect()

        # Placera hindret i nedre högra hörnet.
        self.rect.bottomright = self.screen_rect.bottomright

    def blitme(self):
        self.screen.blit(self.image, self.rect)

    def update(self):
        pass
