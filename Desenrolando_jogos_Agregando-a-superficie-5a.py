import pygame
blanco = (255, 255, 255)
negro = (0, 0, 0)
rojo = (255, 0, 0)

pygame.init()
superficie = pygame.display.set_mode((800,600))
pygame.display.set_caption('deslizante')


gameExit = False
while not gameExit:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameExit = True
    superficie.fill(blanco)
    pygame.draw.rect(superficie, negro, [400, 300, 10,100])
    superficie.fill(rojo, rect=[200, 200,10, 10])
    pygame.display.update()

    
pygame.quit()
quit()
