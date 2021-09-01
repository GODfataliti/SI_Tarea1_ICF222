import pygame
import numpy as np
import sys
import time


pygame.init()

#Ancho, Alto
width,height = 600,600
screen = pygame.display.set_mode((height,width))

bg = 25, 26, 25
screen.fill(bg)

BLACK = (0,      0,       0)
WHITE = (255,   255,    255)


linebg = (40,250,40)

#Cantidad de celdas en el eje X - eje Y
nxC, nyC = 8, 8

#Dimenciones de las celdas
dimCW = width/nxC
dimCH = height/nyC

celdai = [36,36]

#Estado de las celdas. Alfa = 1; Beta = 0
gameState = np.zeros((nxC,nyC))

circleW = (screen, WHITE, [150, 50, 400, 400], 1)
circleB = (screen, BLACK, [150, 50, 400, 400], 1)


while True:

    for event in pygame.event.get():
        #print(event)
        if event.type == pygame.QUIT:
            sys.exit()
    


    pygame.draw.circle(screen, WHITE,celdai ,33, 0)
    #pygame.draw.circle(Surface, color, pos, radius, width=0)

    
    #Dibujar la cuadricula
    for y in range(0,nxC):
        for x in range(0,nyC):
            poly = [((x)    * dimCW,    y       *dimCH),
                    ((x+1)  * dimCW,    y       * dimCH),
                    ((x+1)  * dimCW,    (y+1)   * dimCH),
                    ((x)    * dimCW,    (y+1)   * dimCH)]
            pygame.draw.polygon(screen, linebg, poly, width=1)
    




    #Actualizar pantalla
    pygame.display.flip()