import time
from typing import MappingView

class Game:

    def __init__(self):
        self.initialize_game()
    
    def initialize_game(self):
        self.current_state = [['.','.','.'],
                             ['.','.','.'],
                             ['.','.','.']]

        #El jugar X siempre comenzará primero
        self.playe_turn ='X'

    def draw_board(self):
        for i in range (o,3):
            for j in range(0,3):
                print('{}|'.format(self.current_state[i][j]), end=" ")
            print()
        print()

    #Verificar si se hace un movimiento ilegal

    def is_valid(self,px,py):
        if px < 0 or px > 2 or py < 0 or py >2:
            return False
        elif self.current_state[px][py] !='.':
            return False
        else:
            return True
        
    def is_end(self):
        #Victoria Vertical
        for i in range(0, 3):
            if (self.current_state[0][i] != '.' and
                self.current_state[0][i] == self.current_state[1][i] and
                self.current_state[1][i] == self.current_state[2][i]):
                return self.current_state[0][i]

        #Victoria Horizontal
        for i in range(0, 3):
            if (self.current_state[i] == ['X', 'X', 'X']):
                return 'X'
            elif (self.current_state[i] == ['O', 'O', 'O']):
                return 'O'

        #Victoria Diagonal 1
        if (self.current_state[0][0] != '.' and
            self.current_state[0][0] == self.current_state[1][1] and
            self.current_state[0][0] == self.current_state[2][2]):
            return self.current_state[0][0]

        #Victoria Diagonal 2
        if (self.current_state[0][2] != '.' and
            self.current_state[0][2] == self.current_state[1][1] and
            self.current_state[0][2] == self.current_state[2][0]):
            return self.current_state[0][2]

        #Tablero Lleno
        for i in range(0, 3):
            for j in range(0, 3):
                #Sie existe un campo vacio se continua el juego
                if (self.current_state[i][j] == '.'):
                    return None
        return '.'

    #Jugardor 0 is el Max, correspondiente a la AI

    def max(self):

        #Posbiles Valores de Max
        # -1 - Loss (negras)
        # 0 - Lazo
        # 1 - Victoria

        #Se configura un 2 como el peor caso
        maxv = -2

        px = None
        py = None

        result =self.is_end()

        #Si el juego llega a su fin, la función necesitará retornar
        #La evaluación de la función del final puede ser:

        # -1 Pierde
        # 0  Lazo
        # 1 Gana

        if result == 'X':
            return(-1,0,0)
        elif result == '0':
            return (1,0,0)
        elif result == '.':
            return(0,0,0)

        for i in range (0,3):
            for j in range (0,3):
                if self.current_state[i][j] == '.':
                    #En el campo vacio del jugador '0' hace una jugada llamada Min
                    #Esta es una rama del arbol del juego.
                    self.current_state[i][j] = '0'
                    (m, min_i, min_j) = self.min()
                    #Se arregla el valor maxv si se necesita

                    if m > maxv:

                        maxv=m
                        px = i
                        py = j
                    #Se asigna tras el campo vacio
                    self.current_state[i][j] ='.'
        return (maxv,px,py)


    def min(self):

        #Posibles valores del minv son:
        # -1 Gana
        # 0 Un Lazo
        # 1 Pierde

        minv = 2

        qx = None
        qv = None
        
        result = self.is_end()

        if result =='X':
            return (-1, 0, 0)
        elif result == '0':
            return (1, 0, 0)
        elif result == '.':
            return (0, 0, 0)

        for i in range(0, 3):
            for j in range(0, 3):
                if self.current_state[i][j] == '.':
                    self.current_state[i][j] = 'X'
                    (m, max_i, max_j) = self.max()
                    if m < minv:
                        minv = m
                        qx = i
                        qy = j
                    self.current_state[i][j] = '.'

        return (minv, qx, qy)



