import pygame
pygame.init()

superfice = pygame.display.set_mode((800,600))
pygame.display.set_caption('deslizante')

pygame.display.update()
gameExit = False
while not gameExit:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameExit = True
        

    
pygame.quit()
quit()
