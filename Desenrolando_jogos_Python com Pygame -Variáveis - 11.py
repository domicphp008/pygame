import pygame
blanco = (255, 255, 255)
negro = (0, 0, 0)
rojo = (255, 0, 0)

pygame.init()
superficie = pygame.display.set_mode((800,600))
pygame.display.set_caption('deslizante')


gameExit = False
display_ancho = 800
display_altura = 600
lead_x = display_ancho/2
lead_y = display_altura/2
lead_x_cambio = 0
lead_y_cambio = 0
reloj = pygame.time.Clock()
bloque_tamano = 10
CPS = 15
while not gameExit:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameExit = True
    if event.type == pygame.KEYDOWN:
         if event.key == pygame.K_LEFT:
             lead_x_cambio = -bloque_tamano
             lead_y_cambio = 0
         elif event.key == pygame.K_RIGHT:
             lead_x_cambio = bloque_tamano
             lead_y_cambio = 0
         elif event.key == pygame.K_UP:
             lead_y_cambio = -bloque_tamano
             lead_x_cambio = 0
         elif event.key == pygame.K_DOWN:
             lead_y_cambio = bloque_tamano
             lead_x_cambio = 0


    if lead_x >= display_ancho or lead_x < 0 or lead_y >= display_altura or lead_y < 0:
        gameExit = True
        
              
    lead_x += lead_x_cambio
    lead_y += lead_y_cambio
    superficie.fill(blanco)
    pygame.draw.rect(superficie, negro, [lead_x, lead_y, bloque_tamano,bloque_tamano])
    
    pygame.display.update()
    reloj.tick(CPS)
    
pygame.quit()
quit()
