
import collections


# tablero_interfaz = [[0 for x in range(8)] for x in range(9)]
# for x in range(8):
#     for y in range(9):
#         if(2<=x<=7 and 1<=y<=6):
#             tablero_interfaz[x][y]=2
# #print(tablero_interfaz[x=Fila][y=Columna])
tablero_interfaz = [[0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0], [0, 1, 1, 1, 1, 1, 1, 0], [0, -1, 1, -1, 1, 1, -1, 0], [0, 1, -1, -1, 1, -1, -1, 0], [0, 1, 1, 1, 1, -1, 
-1, 0], [0, 1, 1, -1, 1, 1, -1, 0], [0, 1, 1, 1, 1, -1, 1, 0], [0, 0, 0, 0, 0, 0, 0, 0]]

tablero_interfaz[4][3] = 1
tablero_interfaz[4][4] = -1
tablero_interfaz[5][3] = -1
tablero_interfaz[5][4] = 1


valor_negra = 0
valor_blanca = 0

def actualizar_tablero():
    global valor_negra
    global valor_blanca

    for fila in tablero_interfaz:

        contador = {x:fila.count(x) for x in fila}
        #print(contador)
        if(contador.get(-1)):
            print(f'Negras: {contador.get(-1)}')
            valor_negra+=contador.get(-1)
        
        if(contador.get(1)):
            print(f'Blancas: {contador.get(1)}')
            valor_blanca+=contador.get(1)
        
        #print(fila)
        for value in fila:
            if value == 1:
                print("Actualizar Blanca")
            
            if value == -1:
                print("Actualizar Negra")
        
        
    print(f'B: {valor_blanca} - N: {valor_negra}')



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



movimiento(1,[4,4])
actualizar_tablero()