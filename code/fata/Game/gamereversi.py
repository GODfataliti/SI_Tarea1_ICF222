
def cargar_tablero():
    board = [[0 for x in range(8)] for x in range(9)]
    for x in range(8):
        for y in range(9):
            if(2<=x<=7 and 1<=y<=6):
                board[x][y]=2
    
    return board

class Reversi:

    def __init__(self):
        self.tablero = cargar_tablero()
        self.valor_blanca = 0
        self.valor_negra = 0
        self.player = 1

        self.tablero[4][3] = 1
        self.tablero[4][4] = -1
        self.tablero[5][3] = -1
        self.tablero[5][4] = 1
    
    def start(self,dificultad):
        self.__init__()
    
    #Agregar funciones del juego!
    def take_token(self,):
        #Recorrer la matriz
        pass
    