import pygame

pygame.init()

##
##  Tela
##
tamanho = (960, 540)
tela = pygame.display.set_mode(tamanho)
pygame.display.set_caption("Luta na ponte")

##
##Importa imagens
##

##Pesonagem
knight_idle = pygame.image.load("assets\knight\1 IDLE_000.png").convert_alpha

##Background
Background1 = pygame.image.load("assets\background\1\bamboo bridge.png").convert_alpha



status = True
## Loop principal
while True:
    pass
