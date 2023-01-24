"""En modul för abstrakta classer."""


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
        """
        # Spelplanens gränser.
        self.screen = self.settings.screen
        self.screen_rect = self.settings.screen_rect

        # Mät spelarens utkant, och skapa en 'hitbox' som är mindre än utkanten.
        self.rect = self.image.get_rect()
        hitbox_width = self.rect.width / 2
        hitbox_height = self.rect.height / 2
        self.hitbox = self.rect.inflate(-hitbox_width, -hitbox_height)

    def blitme(self):
        """Ritar sig på skärmen."""
        self.screen.blit(self.image, self.rect)

    def update(self):
        """
        Centrera 'hitbox'.

        Användning:
            Används som förlängning av kod specifik för den ärvande klassen.
        """
        self.hitbox.center = self.rect.center
