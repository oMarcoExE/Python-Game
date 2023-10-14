import pygame
from sys import exit

pygame.init()

##
##  Tela
##
tamanho = (960, 540)
tela = pygame.display.set_mode(tamanho)
pygame.display.set_caption("Luta na ponte")

def desenhar_barra_vida(vida):
    largura_barra = 200
    altura_barra = 20
    cor_verde = (0, 255, 0)  # Cor verde
    cor_vermelha = (255, 0, 0)  # Cor vermelha
    if vida > 0:
        pygame.draw.rect(tela, cor_verde, (400, 50, largura_barra * (vida / 100), altura_barra))
    pygame.draw.rect(tela, cor_vermelha, (400, 50, largura_barra, altura_barra), 2)

def animacao_enemies():
    global spider_index

    spider_index += 0.11
    if spider_index > len(spider_superfice) -1:
        spider_index = 0

    tela.blit(spider_superfice[int(spider_index)], (400, 180, 10, 10))

def animacao_perso():
    global player_index
    # Calcula o movimento do personagem

    if movimento_personagem == 0: # Jogador está parado
        knight_superfice = knight_idle_superfice
    else: # Jogador está se movimentando
        knight_superfice = knight_andando_superfice

    # Avança para o proximo frame
    player_index += 0.07
    if player_index > len(knight_superfice) - 1:
        player_index = 0


    if direcao_personagem == 1:
        jogador = knight_idle_superfice[int(player_index)]        
    else:
        jogador = pygame.transform.flip(knight_superfice[int(player_index)], True, False)

    # Desenha o jogador na tela
    tela.blit(jogador, jogador_rect)

def atacar():
    
    global atacar_index

    atacar_index += 0.09
    if atacar_index > len(atacar_superfice) -1:
        atacar_index = 0

    tela.blit(spider_superfice[int(spider_index)], knight_idle_superfice)


##
##Importa imagens
##

##Pesonagem
knight_idle = pygame.image.load("assets/knight/1 IDLE_000.png").convert_alpha()

##Background
Background1 = pygame.image.load('assets/background/1/bamboo bridge.png').convert()


##
## Transforma imagem
##
Background1 = pygame.transform.scale(Background1, tamanho)

knight_idle = pygame.transform.scale(knight_idle, tamanho)

relogio = pygame.time.Clock()


##personagem principal
player_index = 0
knight_idle_superfice = []
knight_andando_superfice = []

for imagem in range(1, 5):
    img = pygame.image.load(f'assets/knight/1 IDLE_00{imagem}.png').convert_alpha()
    img = pygame.transform.scale(img, (150, 150))
    knight_idle_superfice.append(img)

for imagem in range(1, 5):
    img = pygame.image.load(f'assets/knight/2 WALK_00{imagem}.png').convert_alpha()
    img = pygame.transform.scale(img, (150, 150))
    knight_andando_superfice.append(img)

jogador_rect = knight_idle_superfice[player_index].get_rect( center = (100, 430))    

##Animacao atacar
atacar_index = 0
atacar_superfice = []

for imagem in range(1, 5):
    img = pygame.image.load(f'assets/knight/5 ATTACK_000.png').convert_alpha()
    img = pygame.transform.scale(img, (150, 150))
    atacar_superfice.append(img)   

    atacar_rect = atacar_superfice[atacar_index].get_rect(center = (100, 430))

##Inimigo 1 cenario 1
spider_index = 0
spider_superfice = []

for imagem in range(1, 13):
    img = pygame.image.load(f'assets/enemies/Spider/Spider_{imagem}.png').convert_alpha()
    img = pygame.transform.scale(img, (90, 90))
    spider_superfice.append(img)
spider_rect = spider_superfice[int(spider_index)].get_rect(topleft=(400, 180))

movimento_personagem = 0
direcao_personagem = 0
dano_jogador = 10
vida_inimigo = 100

status = True
## Loop principal
while True:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            pygame.quit()
            exit()

        if evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_RIGHT:
                movimento_personagem = 1
                direcao_personagem = 1

            if evento.key == pygame.K_LEFT:
                movimento_personagem = 2
                direcao_personagem = 0

            if evento.key == pygame.K_UP:
                movimento_personagem = 3
                direcao_personagem = 1

            if evento.key == pygame.K_DOWN:
                movimento_personagem = 4
                direcao_personagem = 0

            if evento.key == pygame.K_SPACE:
                if evento.key == pygame.K_SPACE:
                    if jogador_rect.colliderect(spider_rect):
                        vida_inimigo -= dano_jogador
                        if vida_inimigo <= 0:
                            vida_inimigo = 0

        if evento.type == pygame.KEYUP:
            if evento.key == pygame.K_RIGHT:
                movimento_personagem = 0

            if evento.key == pygame.K_LEFT:
                movimento_personagem = 0

            if evento.key == pygame.K_UP:
                movimento_personagem = 0

            if evento.key == pygame.K_DOWN:
                movimento_personagem = 0


    if movimento_personagem == 1:
        jogador_rect.x += 7
    elif movimento_personagem == 2:
        jogador_rect.x -= 7
    elif movimento_personagem == 3:
        jogador_rect.y -= 7
    elif movimento_personagem == 4:
        jogador_rect.y += 7
  

    tela.blit(Background1, (0, 0))

    animacao_perso()
    animacao_enemies()
    desenhar_barra_vida(vida_inimigo)

    pygame.display.update()

    relogio.tick(60)
