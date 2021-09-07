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

linebg = (40,250,40)

#Cantidad de celdas en el eje X - eje Y
nxC, nyC = 25, 25

#Dimenciones de las celdas
dimCW = width/nxC
dimCH = height/nyC

#Estado de las celdas. Vivas = 1; Muertas = 0
gameState = np.zeros((nxC,nyC))

#Crear Automata 
#      ( Fila, Columna)
gameState[12, 12] = 1
gameState[13, 13] = 1
gameState[14, 14] = 1
gameState[12, 13] = 1
gameState[12, 14] = 1
gameState[13, 12] = 1

while True:

    newGameState = np.copy(gameState)

    screen.fill(bg)
    time.sleep(0.1)

    for event in pygame.event.get():
        #print(event)
        if event.type == pygame.QUIT:
            sys.exit()
    
    #Dibujar la cuadricula
    for y in range(0,nxC):
        for x in range(0,nyC):


            #Calculamos el numero de vecinos cercanos.
            n_neigh= gameState[(x-1) % nxC,   (y-1) % nyC] + \
                     gameState[(x) % nxC,     (y-1) % nyC] + \
                     gameState[(x+1) % nxC,   (y-1) % nyC] + \
                     gameState[(x-1) % nxC,   (y) % nyC] + \
                     gameState[(x+1) % nxC,   (y) % nyC] + \
                     gameState[(x-1) % nxC,   (y+1) % nyC] + \
                     gameState[(x) % nxC,     (y+1) % nyC] + \
                     gameState[(x+1) % nxC,   (y+1) % nyC]

            #Rule #1: Una celula muerta con exactamente 3 vecinas vivas, "revive".
            if(gameState[x,y] == 0 and n_neigh == 3):
                newGameState[x,y] = 1
            
            #Rule #2: Una celula viva con menos de 2 o mas 3 vecinas vivas, "muere".
            elif(gameState[x,y] == 1 and (n_neigh < 2 or n_neigh > 3)):
                newGameState[x,y] = 0

            poly = [((x)    * dimCW,    y       *dimCH),
                    ((x+1)  * dimCW,    y       * dimCH),
                    ((x+1)  * dimCW,    (y+1)   * dimCH),
                    ((x)    * dimCW,    (y+1)   * dimCH)]
            pygame.draw.polygon(screen, linebg, poly, width=1)

            #Dibujamos la celda para cada par de x e y.
            if(newGameState[x,y] == 0):
                pygame.draw.polygon(screen, (128,128,128), poly, 1)
            else:
                pygame.draw.polygon(screen, (255,255,255), poly, 0)
            
        
    #Actualizamos el estado del juego
    gameState = np.copy(newGameState)
    #Actualizar pantalla
    pygame.display.flip()