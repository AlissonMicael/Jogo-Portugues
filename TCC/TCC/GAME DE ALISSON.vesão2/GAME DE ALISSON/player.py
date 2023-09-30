import pygame


class Player(pygame.sprite.Sprite):
    def __init__(self, *group):
        super().__init__(*group)
        self.image = pygame.image.load('pixil-frame-0.png').convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.center = (450, 450)

    def movimentar_player(self):
        teclas = pygame.key.get_pressed()

        # Tecla A
        if teclas[pygame.K_a]:
            self.image = pygame.image.load('sprite_1.png').convert_alpha()
            if self.rect.left <= -20:
                self.rect.x += 10
            self.rect.x -= 10

        # Tecla D
        if teclas[pygame.K_d]:
            self.image = pygame.image.load('sprite_0.png').convert_alpha()
            if self.rect.right >= 910:
                self.rect.x -= 10
            self.rect.x += 10

        # Tecla W
        if teclas[pygame.K_w]:
            self.image = pygame.image.load('sprite_3.png').convert_alpha()
            if self.rect.top <= 260:
                self.rect.y += 10
            self.rect.y -= 10

        # Tecla S
        if teclas[pygame.K_s]:
            self.image = pygame.image.load('sprite_2.png').convert_alpha()
            if self.rect.bottom >= 605:
                self.rect.y -= 10
            self.rect.y += 10
