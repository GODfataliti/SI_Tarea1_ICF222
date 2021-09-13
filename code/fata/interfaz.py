import pygame
import sys
import random
import numpy as np
import os
from dotenv import load_dotenv
from pygame.constants import KEYDOWN

load_dotenv()


BACKGROUND = (25, 210, 150)
SIZE = [560,630]
CLOCK = pygame.time.Clock()

DIMENSION_GRID = [70,160]
DIFERENCIA_GRID = [SIZE[0] - DIMENSION_GRID[0],SIZE[1] - DIMENSION_GRID[1]]
TITLE = "REVERSI"



#Dar a elegir el color al jugador
def elegir_color():
    pass

class Interfaz:
    def __init__(self):
        self.fichas = {}
        self.keydown = {}
        self.grid_game = [[0 for x in range(6)] for x in range(6)]
        self.grid_game[3][3] = 1
        self.grid_game[3][4] = -1
        self.grid_game[4][3] = -1
        self.grid_game[4][4] = 1

        self.cambios = True
        

        self.grid = 0

    def startup(self):
        pygame.init()
        self.clock = pygame.time.Clock()
        self.surface = pygame.display.set_mode(SIZE)
        pygame.display.set_caption(TITLE)

        self.fichas['negras'] = pygame.image.load(r'D:\Universidad\Programacion\Sistemas_Inteligentes\Tareas\01\SI_Tarea1_ICF222\src\img\ficha_negra.png')
        self.fichas['blancas'] = pygame.image.load(r'D:\Universidad\Programacion\Sistemas_Inteligentes\Tareas\01\SI_Tarea1_ICF222\src\img\ficha_blanca.png')

        self.grid = pygame.image.load(r'D:\Universidad\Programacion\Sistemas_Inteligentes\Tareas\01\SI_Tarea1_ICF222\src\img\Grid.png')
        self.grid_scale = pygame.transform.scale(self.grid, [420,420])

        self.draw_interfaz()
    
    def draw_interfaz(self):

        self.surface.fill(BACKGROUND)
        #grid = pygame.Rect(0,0,DIMENSION_GRID[0],DIMENSION_GRID[1])
        self.surface.blit(self.grid_scale,[70,160])

        for x in range(0,6):
            for y in range(0,6):
                jugador = self.grid_game[x][y]
                pos = pygame.mouse.get_pos()
                if jugador==1:
                    self.surface.blit(self.fichas['blancas'],pos)
                elif jugador==-1:
                    self.surface.blit(self.fichas['negras'],pos)

    


    def new_game(self):
        self.__init__()
    
    def start(self):
        self.startup()
        self.new_game()

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    pos = pygame.mouse.get_pos()
                    #self.mov_mouse(event)
                
                else:
                    pass

            
            if self.cambios:
                self.draw_interfaz()
                self.cambios = False
            

            self.clock.tick(40)
                    
        



if __name__ == "__main__":
    gr = Interfaz()
    gr.start()
