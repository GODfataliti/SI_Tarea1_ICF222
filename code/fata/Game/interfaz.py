from gamereversi import Reversi
import pygame
import collections
import sys

#VARIABLES GLOBALES
BLACK = (0,0,0)
BACKGROUND = (25, 210, 150)
SIZE = (559,630)
TITLE = "REVERSI"
MARGEN = 5


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
    
    def dificult_selection(self):
        opc = None
        #COORD: FACIL ( 2,8 -> 3,8 )
        #COORD: DIFICIL ( 4,8 -> 5,8 ) 
        self.start_board()
        return opc

    def update_board(self):
        self.reversi.valor_blanca = 0
        self.reversi.valor_negra = 0

        pos_x = 0
        pos_y = 0

        for fila in self.reversi.tablero:
            pos_y = 0
            contador = {x:fila.count(x) for x in fila}
            #print(contador)
            if(contador.get(-1)):
                self.reversi.valor_negra+=contador.get(-1)
            
            if(contador.get(1)):
                self.reversi.valor_blanca+=contador.get(1)

            #Actualizar casillas
            for value in fila:
                new_y = 0
                #OBTENER POSICION COORDENADA
                new_x = (pos_x * 70) + MARGEN
                new_y = (pos_y * 70) + MARGEN
                if value == 1:
                    self.screen.blit(self.recursos['blancas'],[new_y,new_x])

                if value == -1:
                    self.screen.blit(self.recursos['negras'],[new_y,new_x])
                
                pos_y+=1
            pos_x+=1

    def move(self,player,pos):
        #Verificar si el movimiento es valido.
        x,y = (pos[0]//70) , (pos[1]//70)
        x2,y2 = x,y
        if player==1:
            if(self.reversi.tablero[y][x]!=0):
                self.reversi.tablero[y][x]=1
                if(x==0):
                    x2=x+70
                if(y==0):
                    y2=y+70
                
                x2=x2*70 + MARGEN
                y2=y2*70 + MARGEN

                self.screen.blit(self.recursos['blancas'],[x2,y2])
                return player
            else:
                print(f'Jugada Incorrecta.')
        
        elif player==2:
            if(self.reversi.tablero[y][x]!=0):
                self.reversi.tablero[y][x]=-1
                if(x==0):
                    x2=x+70
                if(y==0):
                    y2=y+70
                
                x2=x2*70 + MARGEN
                y2=y2*70 + MARGEN

                self.screen.blit(self.recursos['negras'],[x2,y2])
                return player
            else:
                print(f'Jugada Incorrecta.')

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
        new = self.dificult_selection()
        self.reversi.start(new)

    def start_game(self):
        self.new_game()

        while True:

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    pos = pygame.mouse.get_pos()
                    #print(pos)
                    select_x = (pos[0] // 70)
                    select_y = (pos[1] // 70)
                    print(f' {select_x} , {select_y} ')
                    if(self.reversi.player == 1):
                        self.move(self.reversi.player,pos)
                        print(f'Blanca: {self.reversi.player}')
                        self.reversi.player = 2
                    
                    elif(self.reversi.player==2):
                        self.move(self.reversi.player,pos)
                        print(f'Negra: {self.reversi.player}')
                        self.reversi.player = 1
            
            self.update_board()
            self.update_points(self.reversi.valor_blanca,self.reversi.valor_negra)
            pygame.display.flip()
            self.clock.tick(120)



if __name__ == "__main__":
    gm = Interfaz()
    gm.start_game()