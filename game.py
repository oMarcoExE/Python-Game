import pygame
from sys import exit
from random import randint

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
    cor_vermelha = (255, 0, 0)
    cor_preta = (0, 0, 0)
    if vida > 0:
        pygame.draw.rect(tela, cor_vermelha, (350, 100, largura_barra * (vida / 100), altura_barra))
        pygame.draw.rect(tela, cor_preta, (350, 100, largura_barra, altura_barra), 2)

def vida_knight(vida_knight):
 
    largura_barra = 200
    altura_barra = 20
    cor_verde = (0, 200, 0)
    cor_vermelha = (255, 0, 0) 
    if vida_knight > 0:
        pygame.draw.rect(tela, cor_verde, (45, 19, largura_barra * (vida_knight / 150), altura_barra))
    pygame.draw.rect(tela, cor_vermelha, (45, 19, largura_barra, altura_barra), 2)
    tela.blit(vidapixel, (0, 3))

def animacao_enemies():
    global spider_index

    spider_index += 0.11
    if spider_index > len(spider_superfice) -1:
        spider_index = 0

    tela.blit(spider_superfice[int(spider_index)], (400, 180, 10, 10))

def spider_ataque():
    global vidaKnight
    global ataque_projetil
    global rect
    global ataque_spider

    ataque_spider = (randint(0, 5000))
    rect = projSpider.get_rect(center=spider_rect.center)

    if ataque_spider >=0 and vida_inimigo == 0:
        ataque_spider = 1000
        

    if ataque_spider >= 0 and ataque_spider < 50:

        # Ataque de projetil
        ataque_projetil.append({
            'velocidade': projSpider_velocidade,
            'rect': rect,
            'destino': jogador_rect.center,
            'criacao': pygame.time.get_ticks()
        })

def animar_projeteis():
    global vidaKnight

    clock_projetil = pygame.time.Clock()
    clock_projetil.tick(120)

    for projetil in ataque_projetil:
        dest_x, dest_y = projetil['destino']
        vel = projetil['velocidade']
        proj = projetil['rect']

        if proj.x < dest_x: proj.x += vel 
        if proj.y < dest_y: proj.y += vel

        if proj.x > dest_x: proj.x -= vel
        if proj.y > dest_y: proj.y -= vel
     
        if jogador_rect.colliderect(rect) and ataque_spider < 50 :
            vidaKnight -= dano_spider
            ataque_projetil.remove(projetil)

        if vida_inimigo == 0:
            ataque_projetil.remove(projetil)
            
        tela.blit(projSpider, proj)


   # nasc = projetil['criacao']

   # tempo_projetil = clock_projetil - nasc

    #if tempo_projetil > 120:
     #   ataque_projetil.remove(projetil)
    


def ataque_2_spider():
    tela.blit(atk2Spider, spider_rect)


def animacao_perso():
    global player_index
    jogador = None

    #Delimitador de cenário
    if jogador_rect.bottom >= 460:
        jogador_rect.bottom = 460
    elif jogador_rect.bottom <= 200:
        jogador_rect.bottom = 200

    if jogador_rect.right >= 960:
        jogador_rect.right = 960
    elif jogador_rect.left <= 0:
        jogador_rect.left = 0


    if atacar_anim:
        global atacar_index
        atacar_index += 0.09
        if atacar_index > len(atacar_superfice) - 1:
            atacar_index = 0
        jogador = atacar_superfice[int(atacar_index)]
    else:
        global player_index
        if movimento_personagem == 0:  # Jogador está parado
            knight_superfice = knight_idle_superfice
        else:  # Jogador está se movimentando
            knight_superfice = knight_andando_superfice

        player_index += 0.07
        if player_index > len(knight_superfice) - 1:
            player_index = 0

        if direcao_personagem == 1:
            jogador = knight_idle_superfice[int(player_index)]
        else:
            jogador = pygame.transform.flip(knight_superfice[int(player_index)], True, False)

    tela.blit(jogador, jogador_rect)

def atacar(atacar_anim):
    global atacar_index

    if atacar_anim:
        tela.blit(atacar_superfice[int(atacar_index)], jogador_rect)
        atacar_index += 0.05
        if atacar_index > len(atacar_superfice) - 1:
            atacar_index = 0

        # Se a animação de ataque terminar, desative o ataque
        if atacar_index == 0:
            atacar_anim = False
    else:
        animacao_perso()


##
##Importa imagens
##

#Outros
vidapixel = pygame.image.load('assets\icons\coracao\Heart1.png').convert_alpha()
projSpider = pygame.image.load('assets\enemies\Items and effects\Arrows\Spider_left.png').convert_alpha()
atk2Spider = pygame.image.load('assets\enemies\Items and effects\Arrows\Sheep_horizontal.png').convert_alpha()

##Pesonagem
knight_idle = pygame.image.load("assets/knight/1 IDLE_000.png").convert_alpha()

##Background
Background1 = pygame.image.load('assets/background/1/bamboo bridge.png').convert()
Background2 = pygame.image.load('assets/background/2/forest bridge.png').convert()


##
## Transforma imagem
##
Background1 = pygame.transform.scale(Background1, tamanho)
Background2 = pygame.transform.scale(Background2, tamanho)

knight_idle = pygame.transform.scale(knight_idle, tamanho)
vidapixel = pygame.transform.scale(vidapixel, (50, 50))
projSpider = pygame.transform.scale(projSpider, (110, 110))
atk2Spider = pygame.transform.scale(atk2Spider, (110, 150))


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
    img = pygame.image.load(f'assets/knight/5 ATTACK_00{imagem}.png').convert_alpha()
    img = pygame.transform.scale(img, (180, 180))
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


projSpider_velocidade = 2.4287
movimento_personagem = 0
direcao_personagem = 0
vidaKnight = 150
dano_spider = 20
dano_jogador = 10
vida_inimigo = 100
atacar_anim = False
ataque_projetil = []

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
                atacar_anim = True
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

            if evento.key == pygame.K_SPACE:
                atacar_anim = False



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
    spider_ataque()
    animar_projeteis()
    atacar(atacar_anim)
    vida_knight(vidaKnight)


    pygame.display.update()

    relogio.tick(60)