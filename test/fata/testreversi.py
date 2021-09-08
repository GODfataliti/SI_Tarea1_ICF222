import pygame
import sys
import random
import numpy as np
import os
import dotenv

# Definir colores RGB(,,,)
        #RED GREEN BLUE
BLACK = (0,0,0)
WHITE = (255,255,255)
GREEN = (0,255,0)
BACKGROUND = (25, 26, 25)

linebg = (40,250,40)


ancho, alto = 800, 800
size = (ancho,alto)
# 440 hacia la derecha(Columnas) 500 hacia abajo(Filas)

pygame.init()

#FICHAS
#BLACK = -1
#WHITE = 1
#NULL/CLEAR = 0


num_casillas_x, num_casillas_y = 6, 6

grid = []
for row in range(num_casillas_x):
    grid.append([])
    for column in range(num_casillas_y):
        grid[row].append(0)

print(grid)


#Dimenciones de las celdas
dim_CW = int(ancho/num_casillas_x)
dim_CH = int(alto/num_casillas_y)


#Crear ventana
screen = pygame.display.set_mode(size)
title = "REVERSI"
pygame.display.set_caption(title)
# CONTROLAR LOS FPS
clock = pygame.time.Clock()


#COORDENADAS X e Y
coor_x = dim_CW/2
coor_y = dim_CH/2
coor_z = int(((dim_CW/2)+(dim_CH/2))/2)
#MARGEN
margen = (dim_CH/2)-(dim_CW/2)*0.15


#HAO ASAKURA IMG
# figura_circle = pygame.image.load(r'C:\Users\FATALITI\Desktop\Files\Codigos\SI_Tarea1_ICF222\src\img\hao.png')
# image = pygame.transform.scale(figura_circle, [int(dim_CW*0.75),int(dim_CH*0.75)])

#VELOCIDAD DE MOVIMIENTO
# speed_x = 5
# speed_y = 5

while True:
    
    for event in pygame.event.get():
        print(event)
        if event.type == pygame.QUIT:
            sys.exit()
        
        elif event.type == pygame.MOUSEBUTTONDOWN:

            pos = pygame.mouse.get_pos()
            column = (pos[0] // (ancho+margen))
            row = (pos[1] // (alto+margen))

            grid[row][column] = 1
            print(f'Click {pos} Coordenada: {row}, {column} ')
    
    screen.fill(BACKGROUND)
#coor_x = dim_CW/2
#coor_y = dim_CH/2
#coor_z = int(((dim_CW/2)+(dim_CH/2))/2)

    #DIBUJO CUADRICULA
    for y in range(0,num_casillas_x):
        for x in range(0,num_casillas_y):
            poly = [((x)    * dim_CW,    y       *dim_CH),
                    ((x+1)  * dim_CW,    y       * dim_CH),
                    ((x+1)  * dim_CW,    (y+1)   * dim_CH),
                    ((x)    * dim_CW,    (y+1)   * dim_CH)]
            pygame.draw.polygon(screen, linebg, poly, width=1)
    
    #DIBUJO DE LA CASILLA MARCADA
    for row in range(num_casillas_x):
        for column in range(num_casillas_y):
            color = GREEN
            if grid[row][column]==1:
                color = WHITE
            pygame.draw.circle(screen,color,(((margen+alto)*row),((margen+alto)*column)),margen,width=0)
    
    
    

    clock.tick(40)
    pygame.display.flip()



