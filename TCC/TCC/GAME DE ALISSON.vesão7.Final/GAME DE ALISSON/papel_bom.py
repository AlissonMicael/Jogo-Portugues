import pygame, random


class Papel_bom(pygame.sprite.Sprite):
    def __init__(self, *group):
        super().__init__(*group)
        self.image = pygame.image.load('Prova_.png').convert_alpha()
        self.rect = self.image.get_rect()
        self.mask = pygame.mask.from_surface(self.image)

    def update(self):
        self.rect.y += 10

    @staticmethod
    def criar_papeis(grupo_papeis_bom, dalay_para_criar_papel2):
        if not dalay_para_criar_papel2:
            if len(grupo_papeis_bom) == 0:
                # Gerar papel
                posicao_do_papel = random.randint(10, 850)
                papel_aser_criado = Papel_bom(grupo_papeis_bom)
                papel_aser_criado.rect.center = (posicao_do_papel, random.randint(10, 300))
                dalay_para_criar_papel2 = 10
        else:
            dalay_para_criar_papel2 -= 1
        # Atualizar papeis dentro do grupo
        for papel in grupo_papeis_bom:
            if papel.rect.top >= 610:
                grupo_papeis_bom.remove(papel)

        return dalay_para_criar_papel2
