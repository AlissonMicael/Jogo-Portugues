# ____ bibliotecas ____ #
import pygame, time, random
# ____ classes ____ #
import player, papel, professor
import papel_bom

pygame.init()
# _____ Todas as funções do jogo _____ #


def escrevendo_texto(text: str, tamanho: int, posiçao: tuple, cor=(0, 0, 0)):
    fonte = pygame.font.SysFont('arial black', tamanho)
    txt = fonte.render(text, True, cor)
    posi_do_txt = txt.get_rect()
    posi_do_txt.center = posiçao
    return txt, posi_do_txt

# ----------------------------------- #


def escrevendo_texto2(text: str, tamanho: int, cor=(0, 0, 0)):
    fonte = pygame.font.SysFont('arial black', tamanho)
    txt = fonte.render(text, True, cor)
    return txt


# _____ Carregamento do jogo _____ #
janela_start = True
janela_aberta = False

# Time do jogo
tempo = pygame.time.Clock()
tempo_inicial = time.time()
delay_para_criar_papel = 10
delay_para_criar_papel_2 = 1000

# Musica de fundo
pygame.mixer.music.set_volume(0.4)
pygame.mixer.music.load('musica_fundo.mp3')
pygame.mixer.music.play(-1)

# musica resposta
musica_crt = pygame.mixer.Sound('smw_1-up (1).wav')
musica_erd = pygame.mixer.Sound('smw_lost_a_life.wav')

# fundo
fundo = pygame.image.load('fundo.png')
fundo_start = pygame.image.load('fundo_start.png')
fundo_startc = pygame.transform.scale(fundo_start, (900, 600))
colidiu = False

janela = pygame.display.set_mode((900, 600))
pygame.display.set_caption("Quem disse que eu não sei Português?")

# Grupo do Player
grupo_player = pygame.sprite.GroupSingle()
player = player.Player(grupo_player)

# Grupo Professor
grupo_professor = pygame.sprite.GroupSingle()
professor = professor.Prof(grupo_professor)

# Grupos dos papeis
grupo_papel = pygame.sprite.Group()
grupo_papel_bom = pygame.sprite.Group()

# Fontes
font = pygame.font.SysFont('arial black', 30)
segunda_font = pygame.font.SysFont('arial black', 20)
terceira_font = pygame.font.SysFont('arial black', 15)
quarta_font = pygame.font.SysFont('arial black', 13)
font_pq = pygame.font.SysFont('arial black', 10)

# Sorteando a pergunta
num_sorteado_pergunta = random.randint(0, 2)

esrtaPresionado = False
esrtaPresionadon = False
texto_s = False
texto_n = False

while janela_start:
    # eventos da tela start
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            janela_start = False
        keys = pygame.key.get_pressed()
        if keys[pygame.K_p]:
            janela_start = False
            janela_aberta = True

    texto = escrevendo_texto("Presione 'p' para jogar", 25, (450, 290))

    texto1 = escrevendo_texto("Quem disse que eu não sei Português?", 30, (450, 200))

    color = (255, 255, 255)
    janela.fill(color)
    janela.blit(fundo_startc, (0, 0))
    janela.blit(texto[0], texto[1])
    janela.blit(texto1[0], texto1[1])

    pygame.display.update()

# _____ Jogo _____ #
while janela_aberta:

    # FPS do jogo
    tempo.tick(60)

    #eventos do jogo
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            janela_aberta = False
        keys = pygame.key.get_pressed()
        if colidiu:
            if keys[pygame.K_s]:
                esrtaPresionado = True
                if num_sorteado_pergunta != 0:
                    texto_s = True
                    musica_crt.play()
                else:
                    texto_n = True
                    musica_erd.play()
            if keys[pygame.K_n]:
                esrtaPresionadon = True
                if num_sorteado_pergunta == 0:
                    texto_s = True
                    musica_crt.play()
                else:
                    texto_n = True
                    musica_erd.play()

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
    delay_para_criar_papel_2 = papel_bom.Papel_bom.criar_papeis(grupo_papel, delay_para_criar_papel)

    # Desenhar objetos na tela
    janela.blit(fundo, (0, 0))
    janela.blit(texto, pos_tex)
    grupo_player.draw(janela)
    grupo_papel.draw(janela)
    grupo_papel_bom.draw(janela)
    grupo_professor.draw(janela)
    grupo_professor.update()

    # colisao e tela de colisao
    if colisao:
        colidiu = True
    if colidiu:
        fundo = pygame.image.load('tela.colisao.png')
        janela.blit(fundo, (0, 0))
        pygame.mixer.music.stop()

    # perguntas
        list_perguntas = [
            'Já compramos_ ovos leite e chocolate.',
            'Vamos comer_ gente?',
            'Brasília_ 10 de fevereiro de 1999'
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

        # Mostrando se acertou ou nao e o porque
        if esrtaPresionado:
            if texto_s:
                texto1 = escrevendo_texto2("Parabens, voce acertou se usa virgula aqui.", 13)
                janela.blit(texto1, (330, 330))

                texto2 = escrevendo_texto(list_PorQue[num_sorteado_pergunta], 10, (490, 360))
                janela.blit(texto2[0], texto2[1])

            if texto_n:
                texto1 = escrevendo_texto("sinto muito, mas voce errou.", 13, (490, 340))
                janela.blit(texto1[0], texto1[1])

                texto2 = escrevendo_texto("Pois nao era nessesario o uso da virgula.", 13, (490, 360))
                janela.blit(texto2[0], texto2[1])

                texto3 = escrevendo_texto(list_PorQue[num_sorteado_pergunta], 10, (490, 380))
                janela.blit(texto3[0], texto3[1])

        if esrtaPresionadon:
            if texto_s:
                texto1 = escrevendo_texto("Parabens, voce acertou nao se usa virgula aqui.", 13, (490, 340))
                janela.blit(texto1[0], texto1[1])

                texto2 = escrevendo_texto(list_PorQue[num_sorteado_pergunta], 10, (490, 360))
                janela.blit(texto2[0], texto2[1])

            if texto_n:
                texto1 = escrevendo_texto("sinto muito, mas voce errou.", 13, (490, 340))
                janela.blit(texto1[0], texto1[1])

                texto2 = escrevendo_texto("Pois nao era nessesario o uso da virgula.", 13, (490, 360))
                janela.blit(texto2[0], texto2[1])

                texto3 = escrevendo_texto(list_PorQue[num_sorteado_pergunta], 10, (490, 380))
                janela.blit(texto3[0], texto3[1])

    pygame.display.update()