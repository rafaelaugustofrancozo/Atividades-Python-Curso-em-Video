import pygame
pygame.mixer.init()
pygame.init()
pygame.mixer.music.load('hide.mp3') #A musica tem q ser colada dentro do projeto
pygame.mixer.music.play()
#pygame.event.wait() #Serve para o python só encerrar a execução depois q música acabar

