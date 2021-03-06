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
lead_x_cambio = 0
lead_y_cambio = 0
reloj = pygame.time.Clock()

while not gameExit:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameExit = True
    if event.type == pygame.KEYDOWN:
         if event.key == pygame.K_LEFT:
             lead_x_cambio = -10
             lead_y_cambio = 0
         elif event.key == pygame.K_RIGHT:
             lead_x_cambio = +10
             lead_y_cambio = 0
         elif event.key == pygame.K_UP:
             lead_y_cambio = -10
             lead_x_cambio = 0
         elif event.key == pygame.K_DOWN:
             lead_y_cambio = +10
             lead_x_cambio = 0


    if lead_x >= 800 or lead_x < 0 or lead_y >= 600 or lead_y < 0:
        gameExit = True
        
              
    lead_x += lead_x_cambio
    lead_y += lead_y_cambio
    superficie.fill(blanco)
    pygame.draw.rect(superficie, negro, [lead_x, lead_y, 10,10])
    
    pygame.display.update()
    reloj.tick(15)
    
pygame.quit()
quit()
