from reversi import Reversi
import pygame
import collections
import sys

#VARIABLES GLOBALES
BLACK = (0,0,0)
BACKGROUND = (25, 210, 150)
SIZE = (559,630)
TITLE = "REVERSI"
MARGEN = 5

def determinar_coord(pos):
    # (70,140) == [0,0]
    # (490,560) == [5,5]

    coord = pos
    x_coord = (coord[0] // 70) - 1
    y_coord = (coord[1] // 70) - 2

    print(f'{x_coord}, {y_coord}')


    new_coord = [x_coord,y_coord]

    return new_coord


def imprimeTablero(tablero):
    
    for fila in tablero:
        print(f'{fila}', end="\n")

class Interfaz:

    def __init__(self):
        self.interfaz = None
        self.screen = None
        self.recursos = {}
        self.clock = pygame.time.Clock()
        self.reversi = Reversi()
        pass


    def start_board(self):
        self.screen = pygame.display.set_mode(SIZE)
        pygame.init()
        self.interfaz = pygame.image.load(r'D:\Universidad\Programacion\Sistemas_Inteligentes\Tareas\01\SI_Tarea1_ICF222\src\img\Interfaz01.png').convert()
        self.screen.fill(BACKGROUND)
        self.screen.blit(self.interfaz,[0,0])
        pygame.display.set_caption(TITLE)
        self.recursos['negras'] = pygame.image.load(r'D:\Universidad\Programacion\Sistemas_Inteligentes\Tareas\01\SI_Tarea1_ICF222\src\img\ficha_negra.png')
        self.recursos['blancas'] = pygame.image.load(r'D:\Universidad\Programacion\Sistemas_Inteligentes\Tareas\01\SI_Tarea1_ICF222\src\img\ficha_blanca.png')

        return True
    
    def dificult_selection(self):
        self.start_board()
        opc = None
        pos_x = 0
        pos_y = 0
        print("TEST DIFICULTAD")
        pygame.init()
        for event in pygame.event.get():

            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                pos_x, pos_y = (pos[0]) , (pos[1])


                print(f'{pos_x}, {pos_y}')
                #COORD: FACIL ( 2,8 -> 3,8 )
                if(140<=pos_x<210 and 560<pos_y<560):
                    print("Facil")
                    return 1
                #COORD: DIFICIL ( 4,8 -> 5,8 ) 
                if(280<=pos_x<350 and 560<pos_y<560):
                    print("dificil")
                    return 3

        #self.start_board()
        return 0

    def update_board(self):
        self.reversi.valor_blanca = 0
        self.reversi.valor_negra = 0
        diferencia_x = 140
        diferencia_y = 70
        pos_x = 0
        pos_y = 0

        for fila in self.reversi.tablero:
            pos_y = 0
            contador = {x:fila.count(x) for x in fila}
            #print(contador)
            if(contador.get(2)):
                self.reversi.valor_blanca+=contador.get(2)
            
            if(contador.get(1)):
                self.reversi.valor_negra+=contador.get(1)

            #Actualizar casillas
            for value in fila:
                new_y = 0
                #OBTENER POSICION COORDENADA
                new_x = (pos_x * 70) + MARGEN + diferencia_x
                new_y = (pos_y * 70) + MARGEN + diferencia_y
                if value == 2:
                    self.screen.blit(self.recursos['blancas'],[new_y,new_x])

                if value == 1:
                    self.screen.blit(self.recursos['negras'],[new_y,new_x])
                
                pos_y+=1
            pos_x+=1

    def move(self,player,pos):
        #Verificar si el movimiento es valido.
        diferencia_x = 70
        diferencia_y = 140
        x,y = pos[0], pos[1]
        x2,y2 = x,y
        try:
            if player==1:
                if(x<0 or y<0):
                    print(f'Jugada Incorrecta.')
                    return False

                if(self.reversi.tablero[y][x]==0 or self.reversi.tablero[y][x]==2):
                    self.reversi.tablero[y][x]=1
                    
                    x2=x2*70 + MARGEN + diferencia_x
                    y2=y2*70 + MARGEN + diferencia_y
                    print(f'B: {x2}, {y2}')

                    self.screen.blit(self.recursos['negras'],[x2,y2])
                    self.reversi.fill_column(y,x)
                    imprimeTablero(self.reversi.tablero)
                    #self.reversi.place_piece(x,y)
                    return True
                else:
                    print(f'Jugada Incorrecta.')
                    return False
            
            elif player==2:
                if(x<0 or y<0):
                    print(f'Jugada Incorrecta.')
                    return False

                if(self.reversi.tablero[y][x]==0 or self.reversi.tablero[y][x]==1):
                    self.reversi.tablero[y][x]=2
                    # if(x==0):
                    #     x2=x+70
                    # if(y==0):
                    #     y2=y+70
                    
                    x2=x2*70 + MARGEN + diferencia_x
                    y2=y2*70 + MARGEN + diferencia_y

                    print(f'N: {x2}, {y2}')

                    self.screen.blit(self.recursos['blancas'],[x2,y2])
                    self.reversi.fill_column(y,x)
                    imprimeTablero(self.reversi.tablero)
                    #self.reversi.place_piece(x,y)
                    return True
                else:
                    print(f'Jugada Incorrecta.')
                    return False
            else:
                print("Ninguna opcion")
                return False
        except Exception as e:
            print(f'Error: {e}')

    def update_points(self,blanca,negra):
        pygame.font.init()
        LETRA20 = pygame.font.SysFont("Arial", 40)
        texto_blanca = f'{blanca}  '
        imagen_blanca = LETRA20.render(texto_blanca,True,BLACK,(99,246,255))
        self.screen.blit(imagen_blanca,[410,75])

        texto_negra = f'{negra}  '
        imagen_negra = LETRA20.render(texto_negra,True,BLACK,(99,246,255))
        self.screen.blit(imagen_negra,[140,75])

    def new_game(self):
        #new = self.dificult_selection()
        self.start_board()
        self.reversi.start(None)

    def start_game(self):
        self.new_game()

        while True:

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    pos = pygame.mouse.get_pos()

                    # 70,140 == [0,0]


                    #print(pos)
                    select_x = (pos[0] // 70) - 1
                    select_y = (pos[1] // 70) - 2
                    print(f' {select_x} , {select_y} ')
                    if(self.reversi.player == 1):
                        if(self.move(self.reversi.player,[select_x,select_y])):
                            print(f'Blanca: {self.reversi.player}')
                            self.reversi.player = 2
                    
                    elif(self.reversi.player==2):
                        if(self.move(self.reversi.player,[select_x,select_y])):
                            print(f'Negra: {self.reversi.player}')
                            self.reversi.player = 1
            
            self.update_board()
            self.update_points(self.reversi.valor_blanca,self.reversi.valor_negra)
            pygame.display.flip()
            self.clock.tick(120)



if __name__ == "__main__":
    gm = Interfaz()
    gm.start_game()