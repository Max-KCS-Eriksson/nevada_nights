import pygame


class Settings:
    def __init__(self):
        """Instansiera statiska inställningar för spelaren, hindren, och skärmen."""
        # Spelskärmens inställningar.
        self.screen_width = 1200
        self.screen_height = 800

        # Spelarens inställningar.
        self.player_lives_max = 3
        self.player_gravity = 0.075
        self.player_speed = 0
        self.player_jump_height = -8

        # Hindrens inställningar.
        self.obstacle_spawn_distance = 500

        # Ladda dynamiska inställningar.
        self.initialize_dynamic_settings()

        self._create_screen()

    def initialize_dynamic_settings(self):
        """Deklarera spelets dynamiska inställningar."""
        # Hindrens inställningar.
        self.obstacle_speed = 1.5  # Måste vara över 1 annars kan inte x bli lägre än 0.
        self.obstacle_points = 100
        self.obstacles_per_level = 3

        # Bakgrundsfärg.
        self.bg_color = (60, 0, 80)

    def increase_obstacles_per_level(self):
        """Ökar antalet hinder per nivå med 2."""
        self.obstacles_per_level += 2

    def increase_obstacle_difficulty(self):
        """
        Ökar hindrens hastighet, och poäng per hinder, samt gör bakgrunden mörkare.

        Ökar hindrens hastighet med 20%.
        Ökar poäng per hinder med 50%.
        Gör bakgrundsfärgen mörkare.
        """
        # Hindrens inställningar.
        self.obstacle_speed *= 1.2
        self.obstacle_points += int(self.obstacle_points / 2)

        # Bakgrundsfärg.
        r, g, b = self.bg_color  # Packa upp immutable tuple.
        # Försäkra valid rgb-färg.
        if r > 0:
            r -= 10
        if g > 0:
            g -= 10
        if b > 0:
            b -= 10
        self.bg_color = (r, g, b)

    def _create_screen(self):
        """Skapa bildskärmen efter angivna inställningar."""
        self.screen = pygame.display.set_mode((self.screen_width, self.screen_height))
        self.screen_rect = self.screen.get_rect()
