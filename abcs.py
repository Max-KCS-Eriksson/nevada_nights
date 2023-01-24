"""En modul för abstrakta classer."""

from settings import Settings


class AbstractBaseGameElement:
    """
    En abstract basklass som enkapsulerar vanligt förekommande attribut och metoder.

    Används för att reducera kodduplicering genom att låta andra klasser för spelelement
    ärva från denna klass.
    """

    def __init__(self):
        """
        Initierar attribut vanliga för spelelement i PyGame.

        Användning:
            Initiera efter att ett "image" attribut har deklarerats med
            "pygame.image.load()" som värde. Detta då attributet "rect" får sitt värde
            från "image" attributets ".get_rect()" metod.
            Deklarera specifika inställnings attribut efter super().__init__().
        """
        # Ladda inställningar.
        self.settings = Settings()

        # Spelplanens gränser.
        self.screen = self.settings.screen
        self.screen_rect = self.settings.screen_rect

        # Mät spelelementets utkant, och skapa en 'hitbox' som är mindre än utkanten.
        self.rect = self.image.get_rect()
        hitbox_width = self.rect.width / 2
        hitbox_height = self.rect.height / 2
        self.hitbox = self.rect.inflate(-hitbox_width, -hitbox_height)

    def blitme(self):
        """Ritar sig på skärmen."""
        self.screen.blit(self.image, self.rect)
        # self.screen.fill((0, 125, 255), self.hitbox)  # NOTE Used for DEBUG only.

    def update(self):
        """
        Centrera 'hitbox'.

        Användning:
            Används som förlängning av kod specifik för den ärvande klassen.
        """
        self.hitbox.center = self.rect.center


class BaseObstacle(AbstractBaseGameElement):
    """
    Hanterar ett generiskt hinder och dess resurser.

    Ärver metoder och attribut från abcs.AbstractBaseGameElement och utökar dess
    funktionalitet.
    """

    def __init__(self):
        """
        Instansiera hindret och dennes förutsättningar.

        Användning:
            Initiera efter att ett "image" attribut har deklarerats med
            "pygame.image.load()" som värde. Detta då attributet "rect" får sitt värde
            från "image" attributets ".get_rect()" metod.
            Ett "speed" attribut med ett numeriskt värde >= 1 måste deklareras då detta
            attribut används i .update() metoden.
        """
        # Ärv egenskaper.
        super().__init__()

        self._spawn()

    def update(self):
        """
        Förflyttar sig i vänster riktning med en hastighet av "speed" attributets värde.
        """
        # Förflytta i vänster riktning.
        self.rect.x -= self.speed

        # Förläng med förälderns metod.
        super().update()

    def _spawn(self):
        """
        Placera hindret utanför nedre högra hörnet av spelskärmen.

        Avståndet utanför hörnet bestämms av det privata attributet _respawn_rate.
        """
        # Packa upp det oföränderliga tuple-värdet och addera värdet av _respawn_rate.
        screen_right, screen_bottom = self.screen_rect.bottomright
        self.rect.bottomleft = (screen_right + self._respawn_rate, screen_bottom)
