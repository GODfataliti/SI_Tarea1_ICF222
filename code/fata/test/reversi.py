
def cargar_tablero():
    board = [[0 for x in range(6)] for x in range(6)]
    # for fila in board:
    #     print(f'{fila}', end="\n")
    return board




class Reversi:

    def __init__(self):
        self.tablero = cargar_tablero()
        self.valor_blanca = 0
        self.valor_negra = 0
        self.player = 1
                    #Fila,Columna
        self.tablero[2][2] = 1
        self.tablero[2][3] = 2
        self.tablero[3][2] = 2
        self.tablero[3][3] = 1
    
    def start(self,dificultad):
        self.__init__()
    
    
    def fill_column(self,x,y):
        lista=[0,0,0,0]
        dimencion = len(self.tablero)
        cont_column = 0
        const = y
        findit1 = 0
        findit2 = 0
        if(self.player==1):
            for i in range(dimencion):
                if(self.tablero[i][const]==1 and findit1 < 1):
                    lista[0] = 1
                    lista[1] = const
                    findit1+=1
                
                if(self.tablero[i][const]==1 and findit2 < 2 and (self.tablero[i-1][const]!=0)):
                    lista[2] = i
                    lista[3] = const
                    findit1+=1
                    cont_column+=1
                
                if(self.tablero[i][const]==1 and findit1 > 1 and (self.tablero[i-1][const]!=0)):
                    lista[2] = i
                    lista[3] = const
                    findit1+=1
                    cont_column+=1
                    if(findit1>1):
                        x_variable = lista[0]
                        y_variable = lista[1]

                        x1 = lista[2]
                        y1 = lista[3]
                        while(x_variable <= x1):
                            self.tablero[x_variable][y1]=1
                            x_variable+=1
            lista =[0,0,0,0]
        if(self.player==2):
            for i in range(dimencion):
                if(self.tablero[i][const]==2 and findit2 < 1):
                    lista[0] = 1
                    lista[1] = const
                    findit2+=1
                if(self.tablero[i][const]==2 and findit2 < 2 and (self.tablero[i-1][const]!=0)):
                    lista[2] = i
                    lista[3] = const
                    findit2+=1
                    cont_column+=1
                if(self.tablero[i][const]==2 and findit2 > 1 and (self.tablero[i-1][const]!=0)):
                    lista[2] = i
                    lista[3] = const
                    findit2+=1
                    cont_column+=1
                    if(findit2 > 1):
                        x_variable = lista[0]
                        y_variable = lista[1]
                        x1 = lista[2]
                        y1 = lista[3]
                        while(x_variable <= x1):
                            self.tablero[x_variable][y1] = 2
                            x_variable+=1
            lista =[0,0,0,0]
        
        #self.tablero = fill_row()
    

    def fill_row(self):
        pass