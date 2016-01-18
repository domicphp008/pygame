import pygame
import time
blanco = (255, 255, 255)
negro = (0, 0, 0)
rojo = (255, 0, 0)
display_ancho = 800
display_altura = 600
pygame.init()
superficie = pygame.display.set_mode((800,600))
pygame.display.set_caption('deslizante')


gameExit = False

lead_x = display_ancho/2
lead_y = display_altura/2
lead_x_cambio = 0
lead_y_cambio = 0
reloj = pygame.time.Clock()
bloque_tamano = 10
CPS = 15
font = pygame.font.SysFont(None, 25)
def message_to_screen(msg, color):
     screen_text = font.render(msg, True, color)
     superficie.blit(screen_text, [display_ancho/2, display_altura/2])
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
message_to_screen(" Você perdeu meu Plaboy ", rojo)
pygame.display.update()
time.sleep(3)
    
pygame.quit()
quit()
