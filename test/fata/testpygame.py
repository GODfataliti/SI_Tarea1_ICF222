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
RED = (255,0,0)
BLUE = (0,0,255)
BACKGROUND = (25, 26, 25)



pygame.init()
        #Ancho,Alto
ancho = 600
alto = 600
size = (ancho,alto)
# 440 hacia la derecha(Columnas) 500 hacia abajo(Filas)

nxC, nyC = 6, 6

#Dimenciones de las celdas
dimCW = int(ancho/nxC)
dimCH = int(alto/nyC)


#Crear ventana
screen = pygame.display.set_mode(size)
title = "REVERSI"
pygame.display.set_caption(title)
# CONTROLAR LOS FPS
clock = pygame.time.Clock()


# while True:
#     for event in pygame.event.get():
#         print(event)
#         if event.type == pygame.QUIT:
#             sys.exit()
    
#     screen.fill(WHITE)
#     # Zona de dibujo
#     #pygame.draw.line(screen, GREEN, [0,100],[100,100], 5)

#     x = 5
#     y = 0
#     z = (x+y)/2
#     while x<430:
#         pygame.draw.line(screen,GREEN,[y,x],[x,x+y])
#         pygame.draw.line(screen, GREEN, [430-y,x], [430-x,x+y], width=1)
#         pygame.draw.circle(screen, BLACK, [z,200+z], 5, width=1)

#         x+=5
#         y+=5
#         z = (x+y)/2

#     # Fin de la zona de dibujo
#     #Actualizar pantalla
#     pygame.display.flip()

# FIGURAS CON FOOR LOOPS
# while True:
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             sys.exit()
    
#     screen.fill(WHITE)
#     # -- ZONA DE DIBUJO --
#     for x in range(100,500,50): #Inicio, termino, salto
#         pygame.draw.circle(screen,GREEN,(x, 150),20,width=1)
#         pygame.draw.circle(screen,GREEN,(150,x),20, width=1)
    
#     # -- ZONA DE DIBJO --
#     pygame.display.flip()



#COORDENADAS X e Y
coor_x = dimCH/2
coor_y = dimCH/2
coor_z = int(((dimCW/2)+(dimCH/2))/2)

print(f'{dimCH} - {dimCW}')


figura_circle = pygame.image.load(r'C:\Users\FATALITI\Desktop\Files\Codigos\SI_Tarea1_ICF222\src\img\hao.png')
image = pygame.transform.scale(figura_circle, [int(dimCW*0.75),int(dimCH*0.75)])

#VELOCIDAD DE MOVIMIENTO
speed_x = 6
speed_y = 4
margen = (dimCW/2)-(dimCW/2)*0.15

linebg = (40,250,40)

select_x = None
select_y = None

while True:
   num_linea = [0,1,2,3,4,5,6]
   screen.fill(BACKGROUND)
   for event in pygame.event.get():
      #print(event)
      if event.type == pygame.QUIT:
         sys.exit()
      
      elif event.type == pygame.MOUSEBUTTONDOWN:
         pos = pygame.mouse.get_pos()
         select_x = pos[0] // 100
         select_y = pos[1] // 100
         print(f'{select_x} , {select_y}')
         pygame.draw.circle(screen, BLACK, ((coor_z+dimCW*num_linea.index(select_x)),(coor_z+dimCW*num_linea.index(select_y))), (margen),width=0)

   
   for y in range(0,nxC):
        for x in range(0,nyC):
            poly = [((x)    * dimCW,    y       *dimCH),
                    ((x+1)  * dimCW,    y       * dimCH),
                    ((x+1)  * dimCW,    (y+1)   * dimCH),
                    ((x)    * dimCW,    (y+1)   * dimCH)]
            pygame.draw.polygon(screen, linebg, poly, width=1)
   
   if(coor_x>(ancho-margen) or coor_x<0):
      speed_x *=-1
   
   if(coor_y>(alto-margen) or coor_y<0):
      speed_y *=-1

   screen.blit(image, [coor_x,coor_y])

   #AGREGAR FUNCION QUE RETORNE LAS COORDENADAS DEL TABLERO (FILA,COLUMNA)
   pygame.draw.circle(screen, WHITE, ((coor_z+dimCW*num_linea[2]),(coor_z+dimCW*num_linea[3])), (margen),width=0)
   pygame.draw.circle(screen, WHITE, ((coor_z+dimCW*num_linea[3]),(coor_z+dimCW*num_linea[2])), (margen),width=0)
   
   pygame.draw.circle(screen, BLACK, ((coor_z+dimCW*num_linea[2]),(coor_z+dimCW*num_linea[2])), (margen),width=0)
   pygame.draw.circle(screen, BLACK, ((coor_z+dimCW*num_linea[3]),(coor_z+dimCW*num_linea[3])), (margen),width=0)

   #pygame.draw.circle(screen, BLACK, ((coor_z+dimCW*num_linea.index(select_x)),(coor_z+dimCW*num_linea.index(select_y))), (margen),width=0)



   coor_x += speed_x
   coor_y += speed_y

   #pygame.draw.circle(screen,GREEN,(coor_x, coor_y),15,width=2)

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

# DIBUJO DE LLUVIA RELLENANDOSE SOLA --------
# altura_max = 800
# coor_list = []
# for i in range(150):
#       x = random.randint(0,altura_max)
#       y = random.randint(0,altura_max)
#       coor_list.append([x,y])



# while True:
#    for event in pygame.event.get():
#       if event.type == pygame.QUIT:
#          sys.exit()
   
#    screen.fill(BACKGROUND)
#    pygame.display.flip()

#    for coord in coor_list:
#       pygame.draw.circle(screen, WHITE, coord, 2)
#       coord[1]+=3
#       coord[0]+=1
#       if (coord[1]>altura_max):
#          coord[1]=0
      
#       if(coord[0]>altura_max):
#          coord[0]=0
   
#    pygame.display.flip()
#    clock.tick(80)