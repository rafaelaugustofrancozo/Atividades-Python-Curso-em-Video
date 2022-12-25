import pygame
pygame.init()
for c in range(10,0,-1):
    print('{}...'.format(c))
    pygame.event.wait(1000)
print('FELIZ ANO NOVO!')

from time import sleep
for c in range(10,0,-1):
    print('{}...'.format(c))
    sleep(0.5)
print('FELIZ ANO NOVO!')