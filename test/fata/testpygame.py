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
BACKGROUND = (25, 26, 25)



pygame.init()
        #Ancho,Alto
ancho = 500
alto = 500
size = (ancho,alto)
# 440 hacia la derecha(Columnas) 500 hacia abajo(Filas)

nxC, nyC = 8, 8

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
coor_x = 100
coor_y = 100

figura_circle = pygame.image.load(r'C:\Users\FATALITI\Desktop\Files\Codigos\SI_Tarea1_ICF222\src\img\hao.png')
image = pygame.transform.scale(figura_circle, [(dimCW-4),(dimCH-4)])

#VELOCIDAD DE MOVIMIENTO
speed_x = 6
speed_y = 4

linebg = (40,250,40)

while True:
   screen.fill(BACKGROUND)
   for event in pygame.event.get():
      if event.type == pygame.QUIT:
         sys.exit()
   
   for y in range(0,nxC):
        for x in range(0,nyC):
            poly = [((x)    * dimCW,    y       *dimCH),
                    ((x+1)  * dimCW,    y       * dimCH),
                    ((x+1)  * dimCW,    (y+1)   * dimCH),
                    ((x)    * dimCW,    (y+1)   * dimCH)]
            pygame.draw.polygon(screen, linebg, poly, width=1)
   
   if(coor_x>(ancho-80) or coor_x<0):
      speed_x *=-1
   
   if(coor_y>(alto-80) or coor_y<0):
      speed_y *=-1
   

   screen.blit(image, [coor_x,coor_y])

   coor_x += speed_x
   coor_y += speed_y

    #pygame.draw.circle(screen,GREEN,(coor_x, coor_y),15,width=2)

   pygame.display.flip()
   clock.tick(35)