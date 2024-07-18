# ____ bibliotecas ____ #
import pygame, time, random
# ____ classes ____ #
import player, papel, professor
import papel_bom, cronometro

pygame.init()


# _____ Todas as funções do jogo _____ #


def escrevendo_texto(text: str, tamanho: int, posicao: tuple, cor=(0, 0, 0)):
    fonte = pygame.font.SysFont('arial black', tamanho)
    tx = fonte.render(text, True, cor)
    posi_do_txt = tx.get_rect()
    posi_do_txt.center = posicao
    return tx, posi_do_txt

# ----------------------------------- #


def escrevendo_texto2(text: str, tamanho: int, cor=(0, 0, 0)):
    fonte = pygame.font.SysFont('arial black', tamanho)
    x = fonte.render(text, True, cor)
    return x


# ----------------------------------- #
# _____ Carregamento do jogo _____ #
janela_start = True
janela_aberta = False

# Time do jogo
tempo = pygame.time.Clock()
crono = cronometro.Cronometro()
delay_para_criar_papel = 8

# Musica de fundo
pygame.mixer.music.set_volume(0.4)
pygame.mixer.music.load('musica_fundo.mp3')
pygame.mixer.music.play(-1)

# musica resposta
musica_crt = pygame.mixer.Sound('smw_1-up (1).wav')
musica_erd = pygame.mixer.Sound('smw_lost_a_life.wav')
musica_go = pygame.mixer.Sound('msc-go.wav')
musica_go.set_volume(0.3)
fds = 0

# fundo
fundo_go = pygame.image.load('fundo_go.png')
fundo = pygame.image.load('fundo.png')
fundo_start = pygame.image.load('fundo_start.png')
fundo_startc = pygame.transform.scale(fundo_start, (900, 600))
colidiu = False
colidiu2 = False

janela = pygame.display.set_mode((900, 600))
pygame.display.set_caption("Portugame")

# Grupo do Player
grupo_player = pygame.sprite.GroupSingle()
player = player.Player(grupo_player)

# Grupo Professor
grupo_professor = pygame.sprite.GroupSingle()
professor = professor.Prof(grupo_professor)

# Grupos dos papeis
grupo_papel = pygame.sprite.Group()

# Fontes
font = pygame.font.SysFont('arial black', 30)
segunda_font = pygame.font.SysFont('arial black', 20)
terceira_font = pygame.font.SysFont('arial black', 15)
quarta_font = pygame.font.SysFont('arial black', 13)
font_pq = pygame.font.SysFont('arial black', 10)

# Sorteando a pergunta
num_sorteado_pergunta = random.randint(0, 9)
print(num_sorteado_pergunta)

temp = ""
pontos = 0
esrtaPresionado = False
esrtaPresionadon = False
texto_s = False
texto_n = False
respondido = False
pontos_acerta_papel = 0

# __ Tela de start __ #
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

crono.iniciar()
grupo_papel_bom = pygame.sprite.Group()
dalay_para_criar_papel2 = 100

# _____ Jogo _____ #
while janela_aberta:

    # FPS do jogo
    tempo.tick(30)

    # eventos do jogo
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            janela_aberta = False
        keys = pygame.key.get_pressed()
        if colidiu2 and not respondido:
            if keys[pygame.K_s]:
                esrtaPresionado = True
                if num_sorteado_pergunta < 5:
                    texto_s = True
                    musica_crt.play()
                else:
                    texto_n = True
                    musica_erd.play()
                respondido = True
            if keys[pygame.K_n]:
                esrtaPresionadon = True
                if num_sorteado_pergunta > 5:
                    texto_s = True
                    musica_crt.play()
                else:
                    texto_n = True
                    musica_erd.play()
                respondido = True

    tempo_mostrado = crono.tempo_decorrido()
    # Mostrar tempo de jogo
    texto = font.render(
        'Tempo: ' + str(int(tempo_mostrado)), True, (255, 255, 255), (0, 0, 0)
    )
    pos_tex = texto.get_rect()
    pos_tex.topleft = (5, 5)

    # Permitir movimentação do Player
    player.movimentar_player()

    # Colisões
    colisao = pygame.sprite.spritecollide(
        player, grupo_papel, False, pygame.sprite.collide_mask
    )
    colisao2 = pygame.sprite.spritecollide(
        player, grupo_papel_bom, False, pygame.sprite.collide_mask
    )

    # Criar e organizar papeis
    if not colidiu and not colidiu2:
        delay_para_criar_papel = papel.Papel.organizar_papeis(grupo_papel, delay_para_criar_papel)
        dalay_para_criar_papel2 = papel_bom.Papel_bom.criar_papeis(grupo_papel_bom, dalay_para_criar_papel2)

    if tempo_mostrado > 150:
        delay_para_criar_papel = 5

    # Desenhar objetos na tela
    janela.blit(fundo, (0, 0))
    janela.blit(texto, pos_tex)
    grupo_player.draw(janela)
    if not colisao or colisao2:
        grupo_papel.draw(janela)
        grupo_papel_bom.draw(janela)
        grupo_papel_bom.update()
    grupo_professor.draw(janela)
    grupo_professor.update()

    # colisao e tela de colisao
    if colisao:
        colidiu = True
    if colidiu or texto_n:
        janela.blit(fundo_go, (0, 0))
        if not temp:
            temp = tempo_mostrado
        if pontos_acerta_papel > 0:
            pontos = pontos_acerta_papel*temp
        else:
            pontos = temp

        t = escrevendo_texto(f"Você fez {int(pontos)} pontos", 40, (450, 540), (255, 255, 255))
        janela.blit(t[0], t[1])
        t2 = escrevendo_texto("Segure 'r' para reiniciar", 35, (450, 570), (255, 255, 255))
        janela.blit(t2[0], t2[1])
        pygame.mixer.music.pause()
        print(temp)
        if fds < 1:
            musica_go.play()
            fds += 1
            if texto_n:
                pontos_acerta_papel -= 2
        if keys[pygame.K_r]:
            fundo = pygame.image.load('fundo.png')
            texto_s = False; colidiu = False
            esrtaPresionado = False; esrtaPresionadon = False
            colidiu2 = False; respondido = False
            crono.iniciar(); pygame.mixer.music.unpause()
            texto_n = False; pontos_acerta_papel = 0
            temp = ""

    if colisao2:
        colidiu2 = True
    if colidiu2:
        crono.pausar()
        fundo = pygame.image.load('tela.colisao.png')
        janela.blit(fundo, (0, 0))
        pygame.mixer.music.pause()

        # perguntas
        list_perguntas = [
            'Precisa-se de voluntários para o projeto de limpeza. Essa frase possui sujeito indeterminado?',
            'A frase "O menino estava com fome. Ele comeu um sanduíche." possui coesão?',
            'A conjunção "além de" é um termo que estabelece uma ideia de adição?',
            'É necessário o uso da vírgula na frase? Já compramos ovos_ leite e chocolate.',
            'É necessário o uso da vírgula na frase ? Estamos esperando_ pessoal.',
            'A frase abaixo requer o uso de ponto de interrogação? Você já terminou o seu trabalho_',
            'É necessário o uso da vírgula na frase ? Ele foi_ comigo.',
            'Era uma vez um reino distante e encantado. Há sujeito composto nessa frase?',
            'Choveu bastante na semana passada. Essa frase possui sujeito indeterminado?',
            'É necessário a utilização do ponto final na frase? O que você vai fazer agora_'
        ]
        list_PorQue = [
            'Sim, há sujeito indeterminado, pois não se especifica quem precisa de voluntários para o projeto de limpeza.',
            'Sim, pois o pronome “ele” conecta as duas frases, mostrando que a ação de comer o sanduíche foi realizada pelo menino'
            'Sim, a conjunção "além de" é um termo aditivo, pois indica soma, acréscimo ou adição de ideias.',
            'Sim, vírgula obrigatória para separar termos numa enumeração',
            'Sim, vírgula obrigatória para separar vocativo.',
            'Sim, a frase "Você já terminou o seu trabalho," requer o uso de ponto de interrogação e isso ocorre porque a frase é uma pergunta direta.',
            'Não, vírgula não necessária, pois não há vocativo.',
            'Não, não há sujeito composto. A frase apresenta apenas um sujeito simples, "um reino distante e encantado", que se refere a um único conceito',
            'Não, há uma oração sem sujeito, pois a frase não especifica quem realizou a ação de chover, apenas menciona a ocorrência do evento.',
            'Não, o ponto final não é necessário, pois a frase é uma pergunta.'


        ]
        # Mostrandp pergunta, resposta e o porque.
        # texto = segunda_font.render(
        #     'Acerte se tem ou não virgula:', True, (0, 0, 0), (189, 141, 75)
        # )
        # pos_dois_tex = texto.get_rect()
        # pos_dois_tex.center = (490, 230)
        # janela.blit(texto, pos_dois_tex)

        texto = terceira_font.render(
            list_perguntas[num_sorteado_pergunta], True, (0, 0, 0), (189, 141, 75)
        )
        pos_dois_tex = texto.get_rect()
        pos_dois_tex.center = (490, 270)
        janela.blit(texto, pos_dois_tex)

        texto = quarta_font.render(
            "Digite (S) 'Sim, Tem' ou (N) 'Não tem':", True, (0, 0, 0), (189, 141, 75)
        )
        pos_dois_tex = texto.get_rect()
        pos_dois_tex.center = (490, 300)
        janela.blit(texto, pos_dois_tex)

        # Mostrando se acertou ou nao e o porque
        if esrtaPresionado:
            if texto_s:
                texto1 = escrevendo_texto2("Parabens, voce acertou.", 13)
                janela.blit(texto1, (330, 330))

                texto2 = escrevendo_texto(list_PorQue[num_sorteado_pergunta], 10, (490, 360))
                janela.blit(texto2[0], texto2[1])

            if texto_n:
                texto1 = escrevendo_texto("sinto muito, mas voce errou.", 13, (490, 340))
                janela.blit(texto1[0], texto1[1])

                texto2 = escrevendo_texto("Vamos treinar mais um pouco", 13, (490, 360))
                janela.blit(texto2[0], texto2[1])

                texto3 = escrevendo_texto(list_PorQue[num_sorteado_pergunta], 10, (490, 380))
                janela.blit(texto3[0], texto3[1])

        if esrtaPresionadon:
            if texto_s:
                texto1 = escrevendo_texto("Parabens, voce acertou", 13, (490, 340))
                janela.blit(texto1[0], texto1[1])

                texto2 = escrevendo_texto(list_PorQue[num_sorteado_pergunta], 10, (490, 360))
                janela.blit(texto2[0], texto2[1])

            if texto_n:
                texto1 = escrevendo_texto("sinto muito, mas voce errou.", 13, (490, 340))
                janela.blit(texto1[0], texto1[1])

                texto2 = escrevendo_texto("Vamos treinar mais um pouco", 13, (490, 360))
                janela.blit(texto2[0], texto2[1])

                texto3 = escrevendo_texto(list_PorQue[num_sorteado_pergunta], 10, (490, 380))
                janela.blit(texto3[0], texto3[1])
        
        if respondido:
            textProseguir = escrevendo_texto("Aperte a tecla 'p' para proseguir", 13, (500, 450))
            janela.blit(textProseguir[0], textProseguir[1])
            if keys[pygame.K_p]:
                fundo = pygame.image.load('fundo.png')
                texto_s = False; pontos_acerta_papel += 1
                esrtaPresionado = False; esrtaPresionadon = False
                colidiu2 = False; respondido = False
                crono.retomar(); pygame.mixer.music.unpause()

    pygame.display.update()
