import pygame
import collections
import sys

BLACK = (0,0,0)
BACKGROUND = (25, 210, 150)
size = (559,630)
screen = pygame.display.set_mode(size)
title = "REVERSI"
pygame.display.set_caption(title)

#DIMENSIONES DEL TABLERO 70X70 POR CASILLA, POR LO QUE LA RESOLUCION DE LA PANTALLA DEBE SER MULTIPLO DE ESTE VALOR.


pygame.init()
clock = pygame.time.Clock()

#FUENTE
LETRA20 = pygame.font.SysFont("Arial", 40)


MARGEN = 5
#FICHAS
recursos = {}
recursos['negras'] = pygame.image.load(r'D:\Universidad\Programacion\Sistemas_Inteligentes\Tareas\01\SI_Tarea1_ICF222\src\img\ficha_negra.png')
recursos['blancas'] = pygame.image.load(r'D:\Universidad\Programacion\Sistemas_Inteligentes\Tareas\01\SI_Tarea1_ICF222\src\img\ficha_blanca.png')

#SONIDO
gameOverSound = pygame.mixer.music.load(r'D:\Universidad\Programacion\Sistemas_Inteligentes\Tareas\01\SI_Tarea1_ICF222\src\sound\animefuckyou.mp3')

#INTERFAZ DIVIDIDA
img_grid = pygame.image.load(r'D:\Universidad\Programacion\Sistemas_Inteligentes\Tareas\01\SI_Tarea1_ICF222\src\img\Grid.png')
image_grid = pygame.transform.scale(img_grid, [420,420])
img_puntaje = pygame.image.load(r'D:\Universidad\Programacion\Sistemas_Inteligentes\Tareas\01\SI_Tarea1_ICF222\src\img\Puntaje.png')
img_titulo = pygame.image.load(r'D:\Universidad\Programacion\Sistemas_Inteligentes\Tareas\01\SI_Tarea1_ICF222\src\img\REVERSI.png')
#INTERFAZ UNICA
interfaz = pygame.image.load(r'D:\Universidad\Programacion\Sistemas_Inteligentes\Tareas\01\SI_Tarea1_ICF222\src\img\Interfaz01.png').convert()

#INTERFAZ 8X9 (9LINEAS X 8 COLUMNAS)
#TABLERO 6X6
tablero_interfaz = [[0 for x in range(8)] for x in range(9)]
for x in range(8):
    for y in range(9):
        if(2<=x<=7 and 1<=y<=6):
            tablero_interfaz[x][y]=2
print(tablero_interfaz)


valor_negra = 0
valor_blanca = 0

coord_list = []
jugador = 1

def marca(pos):
    pass


def movimiento(jugador,pos):
    global tablero_interfaz
    x,y = (pos[0]//70) , (pos[1]//70)
    x2,y2 = x,y
    print(pos)
    #print(tablero_interfaz)
    if jugador==1:
        if(tablero_interfaz[y][x]!=0):
            tablero_interfaz[y][x]=1
            if(x==0):
                x2=x+70
            if(y==0):
                y2=y+70
            
            x2=x2*70
            y2=y2*70

            x2 = x2 + MARGEN
            y2 = y2 + MARGEN
            
            screen.blit(recursos['blancas'],[x2,y2])
            return jugador
        else:
            print('Jugada incorrecta')
    elif jugador==2:
        if(tablero_interfaz[y][x]!=0):
            tablero_interfaz[y][x]=-1
            if(x==0):
                x2=x2+70
            if(y==0):
                y2=y2+70
            
            x2=x2*70
            y2=y2*70

            x2 = x2 + MARGEN
            y2 = y2 + MARGEN

            screen.blit(recursos['negras'],[x2,y2])
            return jugador
        else:
            print('Jugada incorrecta')
    




def tablero():
    screen.fill(BACKGROUND)
    screen.blit(interfaz,[0,0])
    #screen.blit(image_grid, [70,160])
    #screen.blit(img_puntaje, [70,90])
    #screen.blit(img_titulo, [190,10])


def actualizar_tablero():
    global valor_negra
    global valor_blanca
    valor_blanca = 0
    valor_negra = 0
    for fila in tablero_interfaz:

        contador = {x:fila.count(x) for x in fila}
        #print(contador)
        if(contador.get(-1)):
            #print(f'Negras: {contador.get(-1)}')
            valor_negra+=contador.get(-1)
        
        if(contador.get(1)):
            #print(f'Blancas: {contador.get(1)}')
            valor_blanca+=contador.get(1)
        
        
    #print(f'B: {valor_blanca} - N: {valor_negra}')
    
    #actualizar_puntaje(valor_blanca,valor_negra)

def actualizar_puntaje(blanca,negra):
    # 2,1 Negra - 5,1 Blanca
    texto_blanca = f'{blanca}  '
    imagen_blanca = LETRA20.render(texto_blanca,True,BLACK,(99,246,255))
    screen.blit(imagen_blanca,[410,75])

    texto_negra = f'{negra}  '
    imagen_negra = LETRA20.render(texto_negra,True,BLACK,(99,246,255))
    screen.blit(imagen_negra,[140,75])

    pass


def main():
    tablero()
    jugador = 1
    estado = True
    while True:
    
        for event in pygame.event.get():
            #print(event)
            if event.type == pygame.QUIT:
                sys.exit()
            
            elif event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                #print(pos)
                select_x = (pos[0] // 70)
                select_y = (pos[1] // 70)
                print(f' {select_x} , {select_y} ')
                coord_list.append([select_x,select_y])
                if(jugador==1):
                    movimiento(jugador,pos)
                    jugador=2

                elif(jugador==2): #[select_x,select_y]
                    movimiento(jugador,pos)
                    jugador=1

        actualizar_tablero()
        actualizar_puntaje(valor_blanca,valor_negra)
        pygame.display.flip()
        clock.tick(40)


if __name__ == "__main__":
    main()