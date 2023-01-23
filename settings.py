import pygame


class Settings:
    def __init__(self):
        """Instansiera inställningar för spelaren, hindren, och skärmen."""
        # Spelskärmens inställningar.
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (60, 0, 80)

        # Spelarens inställningar.
        self.player_gravity = 0.075
        self.player_speed = 0
        self.player_jump_height = -7.75

        # Hindrets inställningar.
        self.obstacle_speed = 1.5  # Måste vara över 1 annars kan inte x bli lägre än 0.
        self.obstacle_respawn_rate = 5  # Avstånd utanför högerkant nytt hinder skapas.

        self._create_screen()

    def _create_screen(self):
        """Skapa bildskärmen efter angivna inställningar."""
        self.screen = pygame.display.set_mode((self.screen_width, self.screen_height))
        self.screen_rect = self.screen.get_rect()
