import pygame
from random import randint
pygame.init()
x = 400
y = 490     #max 600  min 260     490
posproj_x = 420
posproj_y = -3000 #P1
prova2_y = -4000 #P2
prova3_y = -1000 #P3
velocidade = 40
velocidade_proje = 10
timer = 0
tempo_segundos = 0

fundo = pygame.image.load('New Piskel.png')
personagem = pygame.image.load('pixil-frame-0.png')
projeteis = pygame.image.load('Prova.png')

font = pygame.font.SysFont('arial black', 30)
texto = font.render("Tempo: ", True, (255, 255, 255), (0, 0, 0))
pos_tex = texto.get_rect()
pos_tex.center = (65, 30)

janela = pygame.display.set_mode((900, 600))
pygame.display.set_caption("Quem disse que eu nao sei Português?")


janela_aberta = True
while janela_aberta:
    pygame.time.delay(50)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            janela_aberta = False

    comandos = pygame.key.get_pressed()
    if comandos[pygame.K_w] and y >= 260:
        y -= velocidade
    if comandos[pygame.K_s] and y <= 500:
        y += velocidade
    if comandos[pygame.K_d] and x <= 800:
        x += velocidade
    if comandos[pygame.K_a] and x >= 0:
        x -= velocidade

    #colisoes
    # if 0 < posproj_y - y < 180:
    #     if x+10 < posproj_x and y + 80 < posproj_y:
    #         y = 1200
    #         print('erroo')
    #     if x-80 < posproj_x - 300 and y + 180 > posproj_y:
    #         y = 1200
    #     if (x+80 > posproj_x - 136 and y + 180 > prova3_y) and (x-80 < posproj_x - 136 and y + 180 > prova2_y):
    #         y = 1200

    if posproj_y >= 750:
        posproj_y = randint(-600, -300)
    if prova2_y >= 750:
        prova2_y = randint(1, 400) #movimentos das provas
    if prova3_y >= 750:
        prova3_y = randint(-300, 1) #quando enprementar os outros dois papeis trocar a ordem dos valores

    if timer < 20:
        timer += 1
    else:
        tempo_segundos += 1
        texto = font.render("Tempo: "+str(tempo_segundos), True, (255, 255, 255), (0, 0, 0))
        timer = 0

    posproj_y += velocidade_proje + 5
    prova2_y += velocidade_proje
    prova3_y += velocidade_proje + 20

    #deixa o fundo preto janela.fill((0, 0, 0))
    janela.blit(fundo, (0, 0))
    #isso faz o circulo pygame.draw.circle(janela, (255, 0, 0), (x, y), 40)
    janela.blit(personagem, (x, y))
    #relacionado ao if de cima
    posproj_y += velocidade_proje
    janela.blit(projeteis, (posproj_x, posproj_y))
    janela.blit(projeteis, (posproj_x + 160, prova2_y))
    janela.blit(projeteis, (posproj_x - 160, prova3_y))
    janela.blit(texto, pos_tex)
    pygame.display.update()

pygame.quit()