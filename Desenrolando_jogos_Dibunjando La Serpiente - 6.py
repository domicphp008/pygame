import pygame
blanco = (255, 255, 255)
negro = (0, 0, 0)
rojo = (255, 0, 0)

pygame.init()
superficie = pygame.display.set_mode((800,600))
pygame.display.set_caption('deslizante')


gameExit = False

lead_x = 300
lead_y = 300

while not gameExit:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameExit = True
    if event.type == pygame.KEYDOWN:
         if event.key == pygame.K_LEFT:
             lead_x -= 10
         if event.key == pygame.K_RIGHT:
              lead_x += 10
            
    superficie.fill(blanco)
    pygame.draw.rect(superficie, negro, [lead_x, lead_y, 10,10])
    
    pygame.display.update()

    
pygame.quit()
quit()
