import pygame
import numpy as np
import sys


pygame.init()

#Ancho, Alto
width,height = 600,600
screen = pygame.display.set_mode((height,width))

bg = 25, 26, 25
screen.fill(bg)


linebg = (40,250,40)

#Cantidad de celdas en el eje X - eje Y
nxC, nyC = 8, 8

#Dimenciones de las celdas
dimCW = width/nxC
dimCH = height/nyC

#Estado de las celdas. Vivas = 1; Muertas = 0
gameState = np.zeros((nxC,nyC))

while True:

    for event in pygame.event.get():
        #print(event)
        if event.type == pygame.QUIT:
            sys.exit()
    
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