import pygame
import sys
import random
import numpy as np
import os
import dotenv

load_dotenv()

BLACK = os.getenv('BLACK')
WHITE = os.getenv('WHITE')
BACKGROUND = os.getenv('BACKGROUND')
GREEN = os.getenv('GREEN')
LINEABG = os.getenv('LINEABG')
DIMENSION_VOL = int(os.getenv('DIMENSION_VOL'))

#Dar a elegir el color al jugador
def elegir_color():
    pass


#Clase para dibujar el tablero
class gridReversi:

    def __init__(self):
        self.griid = []
        self.jugador = None
        self.adversario = None
    
    def generar_grid(self):
        pass
    
    def rellener_grid(self):
        pass

    def contar_color(self):
        pass

    def movimiento(self):
        pass

#Clase que ejecuta la aplicacion GUI
class Interfaz:

    def __init__(self):
        pygame.init()






#Main
def main():
    Interfaz()

if __name__ == '__main__':
    main()