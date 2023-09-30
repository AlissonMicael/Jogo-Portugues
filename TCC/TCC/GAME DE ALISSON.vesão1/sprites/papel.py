import pygame


class Papel(pygame.sprite.Sprite):
    def __init__(self, *group):
        super().__init__(*group)
        self.image = pygame.image.load('../Prova.png')
        self.mask = pygame.mask.from_surface(self.image)

    def update(self):
        self.rect.y += 10
