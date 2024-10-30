import pygame, os


class Player(pygame.sprite.Sprite):
    def __init__(self, *group):
        super().__init__(*group)
        self.diretorio = os.listdir('personagem/')
        self.aparecer = [
            pygame.image.load('personagem/' + imagem).convert_alpha()
            for imagem in self.diretorio[0:]
        ]
        self.image = self.aparecer[0]
        self.rect = self.image.get_rect()
        self.rect.center = (450, 450)

    def movimentar_player(self):
        teclas = pygame.key.get_pressed()

        # Tecla A
        if teclas[pygame.K_a]:
            self.image = self.aparecer[1]
            if self.rect.left <= -20:
                self.rect.x += 10
            self.rect.x -= 10

        # Tecla D
        if teclas[pygame.K_d]:
            self.image = self.aparecer[0]
            if self.rect.right >= 910:
                self.rect.x -= 10
            self.rect.x += 10

        # Tecla W
        if teclas[pygame.K_w]:
            self.image = self.aparecer[3]
            if self.rect.top <= 260:
                self.rect.y += 10
            self.rect.y -= 10

        # Tecla S
        if teclas[pygame.K_s]:
            self.image = self.aparecer[2]
            if self.rect.bottom >= 605:
                self.rect.y -= 10
            self.rect.y += 10
