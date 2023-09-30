import pygame, random


class Papel(pygame.sprite.Sprite):
    def __init__(self, *group):
        super().__init__(*group)
        self.image = pygame.image.load('Prova.png').convert_alpha()
        self.rect = self.image.get_rect()
        self.mask = pygame.mask.from_surface(self.image)

    def update(self):
        self.rect.y += 10

    @staticmethod
    def organizar_papeis(grupo_papeis, dalay_para_criar_papel):
        if not dalay_para_criar_papel:
            if not len(grupo_papeis) == 3:
                posicao_do_papelnovo = random.randint(10, 850)

                # while de verificação para ter certeza que um papel não vai sair em cima do outro
                posi_verificacao = 0
                while posi_verificacao != len(grupo_papeis):
                    if len(grupo_papeis):
                        papel_ja_criado = grupo_papeis.sprites()[posi_verificacao].rect.x

                        if (papel_ja_criado - 100) <= posicao_do_papelnovo <= (papel_ja_criado + 100):
                            posicao_do_papelnovo = random.randint(10, 850)
                            posi_verificacao = 0
                        else:
                            posi_verificacao += 1

                # Gerar novo papel
                papel_aser_criado = Papel(grupo_papeis)
                papel_aser_criado.rect.center = (posicao_do_papelnovo, random.randint(10, 300))
                dalay_para_criar_papel = 10
        else:
            dalay_para_criar_papel -= 0.5

        # Atualizar papeis dentro do grupo
        for papel in grupo_papeis:
            if papel.rect.top >= 610:
                grupo_papeis.remove(papel)
            else:
                papel.update()

        return dalay_para_criar_papel
