"""En modul för abstrakta classer."""

from pygame.sprite import Sprite

from settings import Settings


class AbstractBaseGameElement:
    """
    En abstract basklass som enkapsulerar vanligt förekommande attribut och metoder.

    Används för att reducera kodduplicering genom att låta andra klasser för spelelement
    ärva från denna klass.
    """

    def __init__(self, game):
        """
        Initierar attribut vanliga för spelelement i PyGame.

        Användning:
            Initiera efter att ett "image" attribut har deklarerats med
            "pygame.image.load()" som värde. Detta då attributet "rect" får sitt värde
            från "image" attributets ".get_rect()" metod.
            Deklarera specifika inställnings attribut efter super().__init__().
        """
        # Ladda spelets inställningar.
        self.settings = game.settings

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


class BaseObstacle(AbstractBaseGameElement, Sprite):
    """
    Hanterar ett generiskt hinder, dess resurser, och dess generella beteende.

    Ärver metoder och attribut från abcs.AbstractBaseGameElement och utökar dess
    funktionalitet.
    """

    def __init__(self, game):
        """
        Instansiera hindret och dennes förutsättningar.

        De ärvda metoderna möjliggör att instanser av klassen kan hanteras i "sprit.Group",
        som är ett listliknande objekt med metoder för att hantera flera tillgångar
        samtidigt, samt använda metoder från AbstractBaseGameElement.

        Åkallar båda föräldrarnas __init__() metoder.

        Användning:
            Initiera efter att ett "image" attribut har deklarerats med
            "pygame.image.load()" som värde. Detta då attributet "rect" får sitt värde
            från "image" attributets ".get_rect()" metod.
            Ett "speed" attribut med ett numeriskt värde >= 1 måste deklareras då detta
            attribut används i .update() metoden.
        """
        # Kalla på båda förälderklassers __init__() metod.
        # Viktigt få om "super().__init__()" används så åkallas endast den förstnämnde
        # förälderns metod om båda klasser har metoder med samma namn.
        # Detta pga MRO (Method Resolution Order) i Python.
        AbstractBaseGameElement.__init__(self, game)
        Sprite.__init__(self)

    def update(self):
        """
        Förflyttar sig i vänster riktning med en hastighet av "speed" attributets värde.
        """
        # Förflytta i vänster riktning.
        self.rect.x -= self.speed

        # Förläng med förälderns metod.
        super().update()
