
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
    contador_blanca = 0
    contador_negra = 0
    for fila in tablero_interfaz:

        contador = {x:fila.count(x) for x in fila}
        #print(contador)
        if(contador.get(-1)):
            print(f'Negras: {contador.get(-1)}')
            valor_negra+=contador.get(-1)
        
        if(contador.get(1)):
            print(f'Blancas: {contador.get(1)}')
            valor_blanca+=contador.get(1)
        
        
    print(f'B: {valor_blanca} - N: {valor_negra}')


actualizar_tablero()