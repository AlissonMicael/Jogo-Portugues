import pygame, time, random
import player, papel

pygame.init()

# _____ Carregamento do jogo _____ #
janela_aberta = True

# Time do jogo
tempo = pygame.time.Clock()
tempo_inicial = time.time()
delay_para_criar_papel = 10

fundo = pygame.image.load('fundo.png')
colidiu = False

janela = pygame.display.set_mode((900, 600))
pygame.display.set_caption("Quem disse que eu não sei Português?")

# Grupo do Player
grupo_player = pygame.sprite.GroupSingle()
player = player.Player(grupo_player)

# Grupo dos papeis
grupo_papel = pygame.sprite.Group()

# Fontes
font = pygame.font.SysFont('arial black', 30)
segunda_font = pygame.font.SysFont('arial black', 20)
terceira_font = pygame.font.SysFont('arial black', 15)
quarta_font = pygame.font.SysFont('arial black', 13)

#sorteando a pergunta
num_sorteado_pergunta = random.randint(0, 2)

# _____ Jogo _____ #
while janela_aberta:

    # FPS do jogo
    tempo.tick(60)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            janela_aberta = False
        keys = pygame.key.get_pressed()
        if colidiu:
            if keys[pygame.K_s]:
                print('digitou (S)')
            if keys[pygame.K_n]:
                print('dogitou (n)')

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

    # Criar e organizar papeis
    delay_para_criar_papel = papel.Papel.organizar_papeis(grupo_papel, delay_para_criar_papel)

    # Desenhar objetos na tela
    janela.blit(fundo, (0, 0))
    janela.blit(texto, pos_tex)
    grupo_player.draw(janela)
    grupo_papel.draw(janela)

    # colisao e tela de colisao
    if colisao:
        colidiu = True
        print('colidiu')
    if colidiu:
        fundo = pygame.image.load('tela.colisao.png')
        janela.blit(fundo, (0, 0))
        list_perguntas = [
            'Já compramos_ ovos leite e chocolate.',
            'Vamos comer_ gente?',
            'Brasília_ 10 de fevereiro de 1999'
        ]
        list_resposta = [
            'N',
            'S',
            'S'
        ]
        list_PorQue = [
            'Virgula obrigatoria para separar termos numa enumeração',
            'Virgula obrigatoria para separar vocativo',
            'Virgula obrigatoria entre nomes de lugares e datas ou endereços'
        ]

        # Mostrandp pergunta, resposta e o porque.
        texto = segunda_font.render(
            'Acerte se tem ou não virgula:', True, (0, 0, 0), (189, 141, 75)
        )
        pos_dois_tex = texto.get_rect()
        pos_dois_tex.center = (490, 230)
        janela.blit(texto, pos_dois_tex)

        texto = terceira_font.render(
            list_perguntas[num_sorteado_pergunta], True, (0, 0, 0), (189, 141, 75)
        )
        pos_dois_tex = texto.get_rect()
        pos_dois_tex.center = (490, 270)
        janela.blit(texto, pos_dois_tex)

        texto = quarta_font.render(
            "Digite (S) 'Sim, Tem' ou (N) 'Não tem' virgula:", True, (0, 0, 0), (189, 141, 75)
        )
        pos_dois_tex = texto.get_rect()
        pos_dois_tex.center = (490, 300)
        janela.blit(texto, pos_dois_tex)

    pygame.display.update()


