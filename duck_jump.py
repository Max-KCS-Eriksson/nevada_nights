import sys
from time import sleep

import pygame

from settings import Settings
from gamestats import GameStats
from scoreboard import Scoreboard
from button import Button
from player import Player
from obstacle import GroundObstacle


class DuckAndJump:
    def __init__(self):
        """
        Instansiera spelet med inställningar, skärm, spelaren, och hinder attribut.
        """
        # Starta pygame.
        pygame.init()

        # Spelets inställningar och skärm.
        self.settings = Settings()
        self.screen = self.settings.screen
        self.screen_rect = self.settings.screen_rect
        pygame.display.set_caption("Duck and Jump")  # Titel på spelets fönster.

        # Instansiera spelets statistik.
        self.stats = GameStats(self)
        self.scoreboard = Scoreboard(self)

        self.scoreboard.prep_score()

        # Instansiera spelets spelare.
        self.player = Player()

        # Skapa grupp med instanser av spelets hinder.
        self.obstacles = pygame.sprite.Group()  # Hantera en mängd hinder samtidigt.
        self._create_obstacles()

        # Instansiera knapp för att starta spelet.
        self.play_button = Button(self, "PLAY")

    def run_game(self):
        """Spelets körning."""
        while True:
            # Kolla efter input från användaren.
            self._check_events()

            # Kolla om spelet är aktivt.
            if self.stats.game_active:
                # Uppdatera spelaren och hindren.
                self.player.update()
                self._update_obstacles()

            # Uppdatera skärmen.
            self._update_screen()

    def _start_game(self):
        """Startar ett ny spelomgång."""
        self.stats.game_active = True

        # Nollställ spelets statistik.
        self.stats.reset_stats()
        self.scoreboard.prep_score()

        # Ta bort alla hinder.
        self.obstacles.empty()

        # Göm muspekaren.
        pygame.mouse.set_visible(False)

    def _update_screen(self):
        """Updaterar skärmen of 'flippar' till en ny bild."""
        # Rita spelets bakgrund och element.
        self.screen.fill(self.settings.bg_color)
        self.player.blitme()
        self.obstacles.draw(self.screen)  # Rita hela gruppen hinder.

        # Rita poänginformation.
        self.scoreboard.show_score()

        # Rita 'PLAY' knappen om spelet är inaktivt..
        if not self.stats.game_active:
            self.play_button.draw_button()

        # 'Flippa' till en ny bild.
        pygame.display.flip()

    def _create_obstacles(self):
        """Skapa och lägg till hinder i list attributet self.obstacles."""
        obstacle = GroundObstacle()
        self.obstacles.add(obstacle)

    def _update_obstacles(self):
        """Uppdatera hinder."""
        self.obstacles.update()
        self._check_obstacle_off_screen()
        self._check_obstacles_collisions()

        # Skapa fler hinder om det inte finns några.
        if not self.obstacles:
            self._create_obstacles()

    def _check_obstacle_off_screen(self):
        """Kolla efter hinder som har passerat ut ur spelskärmen."""
        for obstacle in self.obstacles.copy():
            if obstacle.rect.right <= self.screen_rect.left:
                # Ta bort hinderinstansen från gruppen av hinder.
                self.obstacles.remove(obstacle)
                # Inkrementera poängstatistiken.
                self.stats.score += self.settings.obstacle_points

        # Uppdatera poängen på 'score board'.
        self.scoreboard.prep_score()
        self.scoreboard.check_high_score()

    def _check_obstacles_collisions(self):
        """Kolla efter kollisioner mellan spelare och hinder."""
        # Skapa en lista som fylls med kolliderade objekt.
        collisions = pygame.sprite.spritecollide(
            self.player, self.obstacles, dokill=True, collided=self._has_collided
        )

        # Agera på kollision om listan inte är tom.
        if collisions:
            # Spelaren har liv kvar.
            if self.stats.player_lives_left > 0:
                # Subtrahera ett liv från spelaren.
                self.stats.player_lives_left -= 1
                # Fördröj start av nästa runda.
                sleep(0.5)
            # Spelaren har inte liv kvar.
            else:
                # Deaktivera spelet och återställ muspekaren.
                self.stats.game_active = False
                pygame.mouse.set_visible(True)

                # Kolla om spelaren slagit tidigare 'high score'.
                self.scoreboard.check_high_score()

    def _has_collided(self, player, obstacle):
        """
        Metod för att avgöra kollision mellan 'hitbox'.

        Returnerar booleskt värde.
        """
        return obstacle.hitbox.colliderect(player.hitbox)

    def _check_events(self):
        """Kolla efter tangentbords- och mushändelser."""
        for event in pygame.event.get():
            # Klickar kryssrutan eller använder genväg för att stänga fönster.
            if event.type == pygame.QUIT:
                sys.exit()
            # Inledande vänsterklick.
            elif event.type == pygame.MOUSEBUTTONDOWN:
                # Avgör vart muspekaren var när vänsterklick inleddes.
                mouse_pos = pygame.mouse.get_pos()
                self._check_play_button(mouse_pos)

            # Nedtryckning av tangentbordsknappar.
            elif event.type == pygame.KEYDOWN:
                # Styrning av spelaren.
                if event.key == pygame.K_UP:
                    self.player.jump()

    def _check_play_button(self, mouse_pos):
        """Startar ett nytt spel när 'PLAY' knappen klickas med musen."""
        button_clicked = self.play_button.rect.collidepoint(mouse_pos)
        # Kontrollera att spelet inte redan är aktivt.
        if button_clicked and not self.stats.game_active:
            self._start_game()


if __name__ == "__main__":
    # Instansiera spelet och kalla på dess metod för att starta spelets loop.
    game = DuckAndJump()
    game.run_game()
