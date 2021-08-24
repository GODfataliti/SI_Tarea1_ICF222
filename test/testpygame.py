import pygame
import sys
import os
import dotenv

# Definir colores RGB(,,,)
        #RED GREEN BLUE
BLACK = (0,0,0)
WHITE = (255,255,255)
GREEN = (0,255,0)
RED = (255,0,0)
BLUE = (0,0,255)



pygame.init()
        #Ancho,Alto
size = (440,500)

#Crear ventana
screen = pygame.display.set_mode(size)

while True:
    for event in pygame.event.get():
        #print(event)
        if event.type == pygame.QUIT:
            sys.exit()
    
    screen.fill(WHITE)
    # Zona de dibujo
    #pygame.draw.line(screen, GREEN, [0,100],[100,100], 5)

    x = 5
    y = 0
    z = (x+y)/2
    while x<430:
        pygame.draw.line(screen,GREEN,[y,x],[x,x+y])
        pygame.draw.line(screen, GREEN, [430-y,x], [430-x,x+y], width=1)
        pygame.draw.circle(screen, BLACK, [z,200+z], 5, width=1)

        x+=5
        y+=5
        z = (x+y)/2

    # Fin de la zona de dibujo
    #Actualizar pantalla
    pygame.display.flip()
    


