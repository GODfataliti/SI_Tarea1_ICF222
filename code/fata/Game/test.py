


tablero = [[0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0], [0, 1, 2, 3, 4, 5, 6, 0], [0, -1, -2, -3, -4, -5, -6, 0], [0, 1, 2, 3, 4, 5, 6, 0], [0, -1, -2, -3, -4, -5, 
-6, 0], [0, 1, 2, 3, 4,5, 6, 0], [0, -1, -2, -3, -4, -5, -6, 0], [0, 0, 0, 0, 0, 0, 0, 0]]

player = 2


# def place_token(columna_x,fila_y,estado=True):

#     # if estado:
#     #     tablero[columna_x][fila_y]= player

#     contador_cambios = 0
#     fila = [tablero[fila_y][i] for i in range(0,8)]
#     columna = [tablero[i][columna_x] for i in range(0,9)]
#     print(fila)
#     print(columna)



#     #Verificamos si podemos movernos hacia arriba
#     print(columna[:fila_y])
#     if player in columna[:fila_y]:
#         cambios = []
#         busqueda_completa = False

#         for i in range(fila_y-1,-1,-1):
#             print(f'i: {i}')
#             if busqueda_completa:
#                 continue

#             contador = columna[i]
#             print(f'Valor columna: {contador}')
#             if contador == 0:
#                 cambios = []
#             elif contador == player:
#                 busqueda_completa = True
#             else:
#                 cambios.append(i)
        
#         #Aplicar cambios
#         print(f'Cambios: {cambios}')
#         if busqueda_completa:
#             contador_cambios+=len(cambios)
#             if estado:
#                 for i in cambios:
#                     tablero[i][columna_x] = player
    
    #print(columna)

pos = (489,550)
coord = [5,5]
jugador=1
MARGEN = 5
diferencia_x = 140
diferencia_y = 210

def determinar_coord(pos):
    # (70,140) == [0,0]
    # (490,560) == [5,5]

    coord = pos
    x_coord = (coord[0] // 70) - 1
    y_coord = (coord[1] // 70) - 2

    print(f'{x_coord}, {y_coord}')


    

    new_coord = [x_coord,y_coord]

    return new_coord


def move(player,pos):
    #Verificar si el movimiento es valido.
    x,y = pos[0], pos[1]
    x2,y2 = x,y
    if player==1:
        if(x==0):
            x2=x+70
        if(y==0):
            y2=y+70
            
        x2=x2*70 + MARGEN + diferencia_x
        y2=y2*70 + MARGEN + diferencia_y
        print(f'Pos: {x2},{y2}')
    
    # elif player==2:
    # if(self.reversi.tablero[y][x]==0):
    #     self.reversi.tablero[y][x]=-1
    #     if(x==0):
    #         x2=x+70
    #     if(y==0):
    #         y2=y+70
        
    #     x2=x2*70 + MARGEN
    #     y2=y2*70 + MARGEN

    #     self.screen.blit(self.recursos['negras'],[x2,y2])
    #     #self.reversi.place_piece(x,y)
    #     return player
    # else:
    #     print(f'Jugada Incorrecta.')

print(determinar_coord(pos))
move(jugador,coord)


#(x,y) -> (Columna,Fila)

#place_token(2,5)



def update_board():
    valor_blanca = 0
    valor_negra = 0

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