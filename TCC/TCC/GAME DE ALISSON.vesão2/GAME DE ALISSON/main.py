import pygame, time
import player, papel

pygame.init()

# _____ Carregamento do jogo _____ #
janela_aberta = True

# Time do jogo
tempo = pygame.time.Clock()
tempo_inicial = time.time()
delay_para_criar_papel = 10

fundo = pygame.image.load('New Piskel.png')
janela = pygame.display.set_mode((900, 600))
pygame.display.set_caption("Quem disse que eu não sei Português?")

# Grupo do Player
grupo_player = pygame.sprite.GroupSingle()
player = player.Player(grupo_player)

# Grupo dos papeis
grupo_papel = pygame.sprite.Group()

# Fontes
font = pygame.font.SysFont('arial black', 30)

# _____ Jogo _____ #
while janela_aberta:

    # FPS do jogo
    tempo.tick(60)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            janela_aberta = False

    # Mostrar tempo de jogo
    texto = font.render(
        'Tempo: ' + str(int(time.time() - tempo_inicial)), True, (255, 255, 255), (0, 0, 0)
    )
    pos_tex = texto.get_rect()
    pos_tex.topleft = (5, 5)

    # Permitir movimentação do Player
    player.movimentar_player()

    # Colisões
    colisao = pygame.sprite.spritecollide(
        player, grupo_papel, False, pygame.sprite.collide_mask
    )

    if colisao:
        print('colidiu')

    # Criar e organizar papeis
    delay_para_criar_papel = papel.Papel.organizar_papeis(grupo_papel, delay_para_criar_papel)

    # Desenhar objetos na tela
    janela.blit(fundo, (0, 0))
    janela.blit(texto, pos_tex)
    grupo_player.draw(janela)
    grupo_papel.draw(janela)
    pygame.display.update()
