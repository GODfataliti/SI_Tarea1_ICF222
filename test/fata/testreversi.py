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

pygame.init()
        #Ancho,Alto
dim_vol = 7
ancho_v2,alto_v2 = ((dim_vol*100)+1), ((dim_vol*100)+1)
ancho,alto  = 600, 600

size = (ancho_v2,alto_v2)

nxC, nyC = 6, 6

#Dimenciones de las celdas
dimCW = int(ancho/nxC)
dimCH = int(alto/nyC)
margen = int((dimCW/2)-(dimCW/2)*0.15)

#Crear ventana
screen = pygame.display.set_mode(size)
title = "REVERSI"
pygame.display.set_caption(title)
# CONTROLAR LOS FPS
clock = pygame.time.Clock()

diferencia_grid = (ancho_v2 - ancho) // 100
#COORDENADAS X e Y
coor_x = dimCH/2 + ((dimCW/2) * diferencia_grid)
coor_y = dimCH/2 + ((dimCW/2) * diferencia_grid)
coor_z = int(((dimCW/2)+(dimCH/2))/2) + ((dimCW/2) * diferencia_grid)

print(f'{dimCH} - {dimCW}')
colors_list = [WHITE,BLACK]

figura_circle = pygame.image.load(r'D:\Universidad\Programacion\Sistemas_Inteligentes\Tareas\01\SI_Tarea1_ICF222\src\img\hao.png')
image = pygame.transform.scale(figura_circle, [int(dimCW*0.75+margen),int(dimCH*0.75+margen)])

#VELOCIDAD DE MOVIMIENTO
speed_x = 6
speed_y = 4


linebg = (40,250,40)

select_x = None
select_y = None

coord_list = []
contador_white = 0
contador_black = 0

grid = [x for x in range(0,ancho_v2,dimCW)]
print(grid)

diferencia_grid = (ancho_v2 - ancho) // 100
TITLE = "REVERSI"
pygame.display.set_caption(TITLE)

while True:
   num_linea = [0,1,2,3,4,5]
   screen.fill(BACKGROUND)
   screen.blit(image, [coor_x,coor_y])
   for event in pygame.event.get():
      #print(event)
      if event.type == pygame.QUIT:
         sys.exit()
      
      elif event.type == pygame.MOUSEBUTTONDOWN:
         pos = pygame.mouse.get_pos()
         #print(pos)
         select_x = (((pos[0]-(dimCW/2)*diferencia_grid)) // 100)
         select_y = (((pos[1]-(dimCW/2)*diferencia_grid)) // 100)
         coord_list.append([select_x,select_y])
         print(f' {select_x} , {select_y} ')
         contador_white+=1
         print(f'Total blancos: {contador_white}')
   
   for y in range(0,nxC):
        for x in range(0,nyC):
            new_poly = []
            poly = [[(x)    * dimCW,    y       *dimCH],
                    [(x+1)  * dimCW,    y       * dimCH],
                    [(x+1)  * dimCW,    (y+1)   * dimCH],
                    [(x)    * dimCW,    (y+1)   * dimCH]]
            for value in poly:
               valor_x = value[0] + ((dimCW/2) * diferencia_grid)
               valor_y = value[1] + ((dimCW/2) * diferencia_grid)
               new_poly.append([valor_x,valor_y])

            pygame.draw.polygon(screen, linebg, new_poly, width=1)
   
   
   if(coor_x>(ancho-margen) or coor_x<(0+(dimCH/2))):
      speed_x *=-1
   
   if(coor_y>(alto-margen) or coor_y<(0+(dimCW/4))):
      speed_y *=-1

   if(select_x!=None or select_y!=None):
      #color = random.choice(colors_list)
      for value in coord_list:
         pygame.draw.circle(screen, WHITE, (((coor_z+dimCW*num_linea.index(value[0]))),((coor_z+dimCW*num_linea.index(value[1])))), (margen),width=0)
         


   coor_x += speed_x
   coor_y += speed_y

   pygame.display.flip()
   clock.tick(40)


# #IR LEYENDO LA MATRIZ Y VERIFICAR SI TIENE -1, 0, 1 Y CAMBIANDO 
# matriz = [[0,0,0,0,0,0,0,0],
#          [0,0,0,0,0,0,0,0],
#          [0,0,0,0,0,0,0,0],
#          [0,0,0,0,0,0,0,0],
#          [0,0,0,0,0,0,0,0],
#          [0,0,0,0,0,0,0,0],
#          [0,0,0,0,0,0,0,0],
#          [0,0,0,0,0,0,0,0]]


