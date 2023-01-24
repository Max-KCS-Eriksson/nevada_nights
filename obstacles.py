import pygame
from pygame.sprite import Sprite

from abcs import BaseObstacle


class GroundObstacle(BaseObstacle, Sprite):
    """Ett hinder på marken som ärver metoder från abcs.BaseObstacle och Sprite-klassen."""

    def __init__(self):
        """
        Instansiera hindret med ärvda metoder från förälderklassen, samt hindrets
        förutsättningar.

        De ärvda metoderna möjliggör att instanser av klassen kan hanteras i "sprit.Group",
        som är ett listliknande objekt med metoder för att hantera flera tillgångar
        samtidigt.

        Åkallar båda föräldrarnas __init__() metoder.
        """
        # Ladda hindrets bild.
        self.image = pygame.image.load("assets/cactus.png")

        # Kalla på båda förälderklassers __init__() metod.
        # Viktigt få om "super().__init__()" används så åkallas endast den förstnämnde
        # förälderns metod om båda klasser har metoder med samma namn.
        # Detta pga MRO (Method Resolution Order) i Python.
        BaseObstacle.__init__(self)
        Sprite.__init__(self)

        # Ladda inställningar.
        self.speed = self.settings.obstacle_speed
        self.respawn_rate = self.settings.obstacle_respawn_rate

        self._spawn()

    def _spawn(self):
        """
        Placera hindret utanför nedre högra hörnet av spelskärmen.

        Avståndet utanför hörnet bestämms av attributet respawn_rate.
        """
        # Packa upp det oföränderliga tuple-värdet och addera värdet av respawn_rate.
        screen_right, screen_bottom = self.screen_rect.bottomright
        self.rect.bottomleft = (screen_right + self.respawn_rate, screen_bottom)


class AirObstacle(BaseObstacle, Sprite):
    """Ett hinder i luften som ärver metoder från abcs.BaseObstacle och Sprite-klassen."""

    def __init__(self):
        """
        Instansiera hindret med ärvda metoder från förälderklassen, samt hindrets
        förutsättningar.

        De ärvda metoderna möjliggör att instanser av klassen kan hanteras i "sprit.Group",
        som är ett listliknande objekt med metoder för att hantera flera tillgångar
        samtidigt.

        Åkallar båda föräldrarnas __init__() metoder.
        """
        # Ladda hindrets bild.
        self.image = pygame.image.load("assets/alien.png")

        # Kalla på båda förälderklassers __init__() metod.
        # Viktigt få om "super().__init__()" används så åkallas endast den förstnämnde
        # förälderns metod om båda klasser har metoder med samma namn.
        # Detta pga MRO (Method Resolution Order) i Python.
        BaseObstacle.__init__(self)
        Sprite.__init__(self)

        # Ladda inställningar.
        self.speed = self.settings.obstacle_speed
        self.respawn_rate = self.settings.obstacle_respawn_rate

        self._spawn()

    def _spawn(self):
        """
        Placera hindret i luften.

        Avståndet utanför hörnet bestämms av attributet respawn_rate.
        """
        # Packa upp det oföränderliga tuple-värdet och addera värdet av respawn_rate.
        screen_right, screen_top = self.screen_rect.topright
        self.rect.topleft = (screen_right + self.respawn_rate, screen_top)
