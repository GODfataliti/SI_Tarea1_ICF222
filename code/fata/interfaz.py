import pygame
import sys
import random
import numpy as np
import os
from dotenv import load_dotenv

load_dotenv()

BLACK = os.getenv('BLACK')
WHITE = os.getenv('WHITE')
#BACKGROUND = (os.getenv('BACKGROUND'))
BACKGROUND = (25, 26, 25)
GREEN = os.getenv('GREEN')
#LINEABG = os.getenv('LINEABG')
LINEABG = (40,250,40)
DIMENSION_VOL = int(os.getenv('DIMENSION_VOL')) * 100
DIMENSION_GRID = int(os.getenv('DIMENSION_GRID')) * 100
CLOCK = pygame.time.Clock()

DIFERENCIA_GRID = DIMENSION_VOL - DIMENSION_GRID

print(f'{BACKGROUND}')
#Dar a elegir el color al jugador
def elegir_color():
    pass


#Clase para dibujar el tablero
class gameReversi:

    def __init__(self,dimWH=DIMENSION_GRID):
        self.grid = []
        self.tam = dimWH*100
        self.jugador = None
        self.adversario = None
    
    def generar_grid(self,screen,dim=DIMENSION_GRID):
        
        casillas_x: int = 6
        casillas_y: int = 6
        for value_row in range(casillas_x):
            for value_column in range(casillas_y):
                self.grid.append(0)
        
        dim_casilla_x: int = (dim//casillas_x)
        dim_casilla_y: int = (dim//casillas_y)

        for x in range(0,dim_casilla_x):
            for y in range(0,dim_casilla_y):
                new_poly = []
                poly = [[(x)*dim_casilla_x, (y)*dim_casilla_y],
                            [(x+1)*dim_casilla_x, (y)*dim_casilla_y],
                            [(x+1)*dim_casilla_x, (y+1)*dim_casilla_y],
                            [(x)*dim_casilla_x, (y+1)*dim_casilla_y],
                            ]
                for value in poly:
                    valor_x:int = value[0] + (dim_casilla_x/2) * DIFERENCIA_GRID
                    valor_y:int = value[1] + (dim_casilla_y/2) * DIFERENCIA_GRID
                    new_poly.append([valor_x,valor_y])
                
                pygame.draw.polygon(screen, LINEABG, new_poly, width=1)
                
        





        pass
    
    def rellener_grid(self):
        pass

    def contar_color(self):
        pass

    def movimiento(self):
        pass

#Clase que ejecuta la aplicacion GUI
class Interfaz:

    def __init__(self,dim,name):
        self.size = (dim,dim)
        self.screen = pygame.display.set_mode(self.size)
        self.tick = CLOCK.tick(40)
        self.grid = gameReversi(DIMENSION_GRID)
        pygame.display.set_caption(f'{name}')
        pygame.init()
    
    def run(self):
        while True:
            self.screen.fill(BACKGROUND)
            self.grid.generar_grid(self.screen,DIMENSION_GRID)

            #TO DO: NO DETECTA SALIR DEL PROGRAMA.
            for event in pygame.event.get():
                if event == pygame.QUIT:
                    sys.exit()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    pos = pygame.mouse.get_pos()
                    pos_x: int = (pos[0] // 100)
                    pos_y: int = (pos[1] // 100)
                    print(f'{pos_x}, {pos_y}')
            
            pygame.display.flip()
            self.tick



# #IR LEYENDO LA MATRIZ Y VERIFICAR SI TIENE -1, 0, 1 Y CAMBIANDO 
# matriz = [[0,0,0,0,0,0,0,0],
#          [0,0,0,0,0,0,0,0],
#          [0,0,0,0,0,0,0,0],
#          [0,0,0,0,0,0,0,0],
#          [0,0,0,0,0,0,0,0],
#          [0,0,0,0,0,0,0,0],
#          [0,0,0,0,0,0,0,0],
#          [0,0,0,0,0,0,0,0]]




#Main
def main():

    interfaz = Interfaz(DIMENSION_VOL,"REVERSI")
    interfaz.run()

if __name__ == '__main__':
    main()