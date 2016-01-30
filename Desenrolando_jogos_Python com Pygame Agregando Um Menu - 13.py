import pygame
import time

pygame.init()

blanco = (255,255,255)
negro = (0,0,0)
rojo = (255, 0,0)

display_ancho = 800
display_altura = 600

superficie = pygame.display.set_mode((display_ancho,display_altura))
pygame.display.set_caption('Deslizante')



reloj = pygame.time.Clock()
bloque_tamano = 10
CPS = 15

font = pygame.font.SysFont(None, 25)

def message_to_screen(msg,color):
    pantalla_texto = font.render(msg, True, color)
    superficie.blit(pantalla_texto, [display_ancho/2, display_altura/2])
    
def gameLoop():
    gameExit = False
    gameOver = False
    lead_x = display_ancho/2
    lead_y = display_altura/2
    
    lead_x_cambio = 0
    lead_y_cambio = 0
    
    while not gameExit:
        
          while not gameOver == True
            superficie.fill(blanco)
            message_to_screen("presiona C para Continuar y Q para Terminar", rojo)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        gameExit = True
                        gameOver = False
                    if event.key == pygame.K_c:
                        gameLoop()    



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
                    gameOver = True
            
                  
                lead_x += lead_x_cambio
                lead_y += lead_y_cambio
                superficie.fill(blanco)
                pygame.draw.rect(superficie, negro, [lead_x, lead_y,bloque_tamano,bloque_tamano])
                pygame.display.update()
                
                reloj.tick(CPS)
        
    pygame.quit()
    quit()
    
gameLoop()    
