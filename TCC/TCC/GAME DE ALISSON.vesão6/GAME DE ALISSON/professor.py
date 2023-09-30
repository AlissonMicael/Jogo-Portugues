import pygame, os


class Prof(pygame.sprite.Sprite):
    def __init__(self, *group):
        super().__init__(*group)
        self.diretorio = os.listdir('personagemProf/')
        self.aparecer = [
            pygame.image.load('personagemProf/' + imagem).convert_alpha()
            for imagem in self.diretorio[0:]
        ]
        self.atual = 0
        self.image = self.aparecer[self.atual]
        self.image = pygame.transform.scale(self.image, (130, 130))
        self.rect = self.image.get_rect()
        self.rect.center = (450, 50)

    def update(self):
        self.atual += 0.05
        if self.atual >= 2:
            self.atual = 0
        self.image = self.aparecer[int(self.atual)]
        self.image = pygame.transform.scale(self.image, (130, 130))

