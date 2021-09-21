dirx = [-1, 0, 1, -1, 1, -1, 0, 1]
diry = [-1, -1, -1, 0, 0, 1, 1, 1]  

n =6 #tamaño tablero 6x6
def cargar_tablero():
    board = [[0 for x in range(6)] for x in range(6)]
    # for fila in board:
    #     print(f'{fila}', end="\n")
    return board


minEvalBoard = -1 # min - 1
maxEvalBoard = n * n + 4 * n + 4 + 1 # max + 1


class Reversi:

    

    def ValidarMovimiento(self,tabla, x ,y ,jugador ): # de cris para mis compas, apoco no me quedo genial :)

        lista = [0,0] #sirve para poder guardar las posiciones si es que fuera necesario 
        print("estos son los valores que recibo",x,y)
        
        
        LugarARevisar = 0 #esta variable la usare para saber especificamente cual if es el que cumple la condicion 
        #esta variable podra alvergar del 1 al 8 significando especificamente 1 = diagonal arriba izquierda 2=diagonal derecha abajo 3=diagonal derecha arriba 4= diagonal izquierda abajo
        # 5 = arriba 6 = abajo 7 = izquierda 8 = derecha
         
        
         
        CondicionCumplida  = False
        ficha = jugador  
        movimiento= False
        if(tabla[y][x] !=1 and tabla[y][x]!= 2): # puede ser modificado a tabla[x][y] == 0 para lograr validar la primera parte del movimiento
            movimiento = True
            
        if (movimiento == True): #creo que puede ser modificado a if (movimiento) ya que entraria solo si es True
            if(x == 5 or y == 5 or x == 0 or y == 0 ):
                if(x == 5 and y == 5): # ver si hay alguna ficha del enemigo para validar el movimiento 
                    if(tabla[y-1][x] != ficha and tabla[y-1][x]!=0): #arriba -----------------------------
                        lista[0] = x
                        lista[1] = y-1
                        LugarARevisar = 5
                        CondicionCumplida = self.EncontrarFichaAmiga(tabla,lista[0],lista[1],LugarARevisar,ficha)
                        if(CondicionCumplida == True):
                            return CondicionCumplida # el movimiento es legal 
                    if(tabla[y][x-1] != ficha and tabla[y][x-1]!=0): #izquierda ----------------------------------
                        lista[0] = x-1
                        lista[1] = y
                        LugarARevisar = 7
                        CondicionCumplida= self.EncontrarFichaAmiga(tabla,lista[0],lista[1],LugarARevisar,ficha)
                        if(CondicionCumplida == True):
                            return CondicionCumplida # el movimiento es legal 
                    if(tabla[y-1][x-1] != ficha and tabla[y-1][x-1]!=0):#diagonal izquierda arriba -------------------------------
                        lista[0] = x-1
                        lista[1] = y-1
                        LugarARevisar = 1
                        CondicionCumplida= self.EncontrarFichaAmiga(tabla,lista[0],lista[1],LugarARevisar,ficha) 
                        if(CondicionCumplida == True):
                            return CondicionCumplida # el movimiento es legal 
                lista=[0,0]
                if(x == 0 and y == 5):
                    if(tabla[y-1][x]  != ficha and tabla[y-1][x] != 0): #arriba --------------------------
                        lista[0] = x
                        lista[1] = y-1
                        LugarARevisar =5
                        CondicionCumplida= self.EncontrarFichaAmiga(tabla,lista[0],lista[1],LugarARevisar,ficha)
                        if(CondicionCumplida == True):
                            return CondicionCumplida # el movimiento es legal 
                    if(tabla[y-1][x+1]  != ficha and tabla[y-1][x+1] != 0): # diagonal arriba derecha -----------------------------------
                        lista[0]= x+1 
                        lista[1] =y-1 
                        LugarARevisar = 3
                        CondicionCumplida= self.EncontrarFichaAmiga(tabla,lista[0],lista[1],LugarARevisar,ficha)
                        if(CondicionCumplida == True):
                            return CondicionCumplida # el movimiento es legal 
                    if(tabla[y][x+1]  != ficha and tabla[y][x+1] != 0): #derecha  --------------------------------
                        lista[0]=x+1
                        lista[1]=y
                        LugarARevisar = 8
                        CondicionCumplida= self.EncontrarFichaAmiga(tabla,lista[0],lista[1],LugarARevisar,ficha)
                        if(CondicionCumplida == True):
                            return CondicionCumplida # el movimiento es legal 
                if(x == 0 and y == 0):
                    if(tabla[y+1][x]  != ficha and tabla[y+1][x] != 0): #abajo ---------------------------------------
                        lista[0]= x
                        lista[1] =y+1 
                        LugarARevisar = 6
                        CondicionCumplida= self.EncontrarFichaAmiga(tabla,lista[0],lista[1],LugarARevisar,ficha)
                        if(CondicionCumplida == True):
                            return CondicionCumplida # el movimiento es legal 
                    if(tabla[y][x+1]  != ficha and tabla[y][x+1] != 0): #derecha -----------------------------
                        lista[0]= x+1 
                        lista[1] =y 
                        LugarARevisar = 8
                        CondicionCumplida= self.EncontrarFichaAmiga(tabla,lista[0],lista[1],LugarARevisar,ficha)
                        if(CondicionCumplida == True):
                            return CondicionCumplida # el movimiento es legal 
                    if(tabla[y+1][x+1]  != ficha and tabla[y+1][x+1] != 0): #diagonal abajo derecha --------------------------
                        lista[0]= x+1
                        lista[1] =y+1 
                        LugarARevisar = 2
                        CondicionCumplida= self.EncontrarFichaAmiga(tabla,lista[0],lista[1],LugarARevisar,ficha)
                        if(CondicionCumplida == True):
                            return CondicionCumplida # el movimiento es legal

                if(x == 5 and y == 0 ):
                    if(tabla[y][x-1]  != ficha and tabla[y][x-1] != 0): #izquierda ---------------------------------------------
                        lista[0]= x-1
                        lista[1] =y 
                        LugarARevisar = 7
                        CondicionCumplida= self.EncontrarFichaAmiga(tabla,lista[0],lista[1],LugarARevisar,ficha)
                        if(CondicionCumplida == True):
                            return CondicionCumplida # el movimiento es legal
                    if(tabla[y+1][x]  != ficha and tabla[y+1][x] != 0): #abajo --------------------------------------------------
                        lista[0]= x
                        lista[1] =y+1 
                        LugarARevisar = 6
                        CondicionCumplida= self.EncontrarFichaAmiga(tabla,lista[0],lista[1],LugarARevisar,ficha)
                        if(CondicionCumplida == True):
                            return CondicionCumplida # el movimiento es legal
                    if(tabla[y+1][x-1]  != ficha and tabla[y+1][x-1] != 0): #diagonal abajo izquierda ---------------------------
                        lista[0]= x-1
                        lista[1] =y+1 
                        LugarARevisar = 4
                        CondicionCumplida= self.EncontrarFichaAmiga(tabla,lista[0],lista[1],LugarARevisar,ficha)
                        if(CondicionCumplida == True):
                            return CondicionCumplida # el movimiento es legal
            
            if( x == 0 and y != 0 and y != 5 ): # izquierda --------------------------------------------------------------------------------##############
                if(tabla[y-1][x]  != ficha and tabla[y-1][x] != 0): #arriba --------------------------
                    lista[0] = x
                    lista[1] = y-1
                    LugarARevisar =5
                    CondicionCumplida= self.EncontrarFichaAmiga(tabla,lista[0],lista[1],LugarARevisar,ficha)
                    if(CondicionCumplida == True):
                        return CondicionCumplida # el movimiento es lega 
                if(tabla[y+1][x]  != ficha and tabla[y+1][x] != 0): #abajo --------------------------------------------------
                    lista[0]= x
                    lista[1] =y+1 
                    LugarARevisar = 6
                    CondicionCumplida= self.EncontrarFichaAmiga(tabla,lista[0],lista[1],LugarARevisar,ficha)
                    if(CondicionCumplida == True):
                        return CondicionCumplida # el movimiento es legal
                if(tabla[y-1][x+1]  != ficha and tabla[y-1][x+1] != 0): # diagonal arriba derecha -----------------------------------
                    lista[0]= x+1 
                    lista[1] =y-1 
                    LugarARevisar = 3
                    CondicionCumplida= self.EncontrarFichaAmiga(tabla,lista[0],lista[1],LugarARevisar,ficha)
                    if(CondicionCumplida == True):
                        return CondicionCumplida # el movimiento es legal 
                if(tabla[y][x+1]  != ficha and tabla[y][x+1] != 0): #derecha -----------------------------
                    lista[0]= x+1 
                    lista[1] =y 
                    LugarARevisar = 8 
                    CondicionCumplida= self.EncontrarFichaAmiga(tabla,lista[0],lista[1],LugarARevisar,ficha)
                    if(CondicionCumplida == True):
                        return CondicionCumplida # el movimiento es legal 
                if(tabla[y+1][x+1]  != ficha and tabla[y+1][x+1] != 0): #diagonal abajo derecha --------------------------
                    lista[0]= x+1
                    lista[1] =y+1 
                    LugarARevisar = 2
                    CondicionCumplida= self.EncontrarFichaAmiga(tabla,lista[0],lista[1],LugarARevisar,ficha)
                    if(CondicionCumplida == True):
                        return CondicionCumplida # el movimiento es legal
            if( x != 0 and y == 0 and x != 5 ): # arriba ------------------------------------------------------------###############################
                if(tabla[y][x-1]  != ficha and tabla[y][x-1] != 0): #izquierda ---------------------------------------------
                    lista[0]= x-1
                    lista[1] =y 
                    LugarARevisar = 7
                    CondicionCumplida= self.EncontrarFichaAmiga(tabla,lista[0],lista[1],LugarARevisar,ficha)
                    if(CondicionCumplida == True):
                        return CondicionCumplida # el movimiento es legal
                if(tabla[y][x+1]  != ficha and tabla[y][x+1] != 0): #derecha -----------------------------
                    lista[0]= x+1 
                    lista[1] =y 
                    LugarARevisar = 8 
                    CondicionCumplida= self.EncontrarFichaAmiga(tabla,lista[0],lista[1],LugarARevisar,ficha)
                    if(CondicionCumplida == True):
                        return CondicionCumplida # el movimiento es legal
                if(tabla[y+1][x-1]  != ficha and tabla[y+1][x-1] != 0): #diagonal abajo izquierda ---------------------------
                    lista[0]= x-1
                    lista[1] =y+1 
                    LugarARevisar = 4
                    CondicionCumplida= self.EncontrarFichaAmiga(tabla,lista[0],lista[1],LugarARevisar,ficha)
                    if(CondicionCumplida == True):
                        return CondicionCumplida # el movimiento es legal
                if(tabla[y+1][x]  != ficha and tabla[y+1][x] != 0): #abajo --------------------------------------------------
                    lista[0]= x
                    lista[1] =y+1 
                    LugarARevisar = 6
                    CondicionCumplida= self.EncontrarFichaAmiga(tabla,lista[0],lista[1],LugarARevisar,ficha)
                    if(CondicionCumplida == True):
                        return CondicionCumplida # el movimiento es legal
                if(tabla[y+1][x+1]  != ficha and tabla[y+1][x+1] != 0): #diagonal abajo derecha --------------------------
                    lista[0]= x+1
                    lista[1] =y+1 
                    LugarARevisar = 2
                    CondicionCumplida= self.EncontrarFichaAmiga(tabla,lista[0],lista[1],LugarARevisar,ficha)
                    if(CondicionCumplida == True):
                        return CondicionCumplida # el movimiento es legal
                

            if(x != 0 and y == 5 and x != 5): # abajo --------------------------------------##################################################
                if(tabla[y][x+1]  != ficha and tabla[y][x+1] != 0): #derecha -----------------------------
                    lista[0]= x+1 
                    lista[1] =y 
                    LugarARevisar = 8
                    CondicionCumplida= self.EncontrarFichaAmiga(tabla,lista[0],lista[1],LugarARevisar,ficha)
                    if(CondicionCumplida == True):
                        return CondicionCumplida # el movimiento es legal
                if(tabla[y][x-1]  != ficha and tabla[y][x-1] != 0): #izquierda ---------------------------------------------
                    lista[0]= x-1
                    lista[1] =y 
                    LugarARevisar = 7
                    CondicionCumplida= self.EncontrarFichaAmiga(tabla,lista[0],lista[1],LugarARevisar,ficha)
                    if(CondicionCumplida == True):
                        return CondicionCumplida # el movimiento es legal
                if(tabla[y-1][x+1]  != ficha and tabla[y-1][x+1] != 0): # diagonal arriba derecha -----------------------------------
                    lista[0]= x+1 
                    lista[1] =y-1 
                    LugarARevisar = 3
                    CondicionCumplida= self.EncontrarFichaAmiga(tabla,lista[0],lista[1],LugarARevisar,ficha)
                    if(CondicionCumplida == True):
                        return CondicionCumplida # el movimiento es legal 
                if(tabla[y-1][x]  != ficha and tabla[y-1][x] != 0): #arriba --------------------------
                    lista[0] = x
                    lista[1] = y-1
                    LugarARevisar =5
                    CondicionCumplida= self.EncontrarFichaAmiga(tabla,lista[0],lista[1],LugarARevisar,ficha)
                    if(CondicionCumplida == True):
                        return CondicionCumplida # el movimiento es lega 
                if(tabla[y-1][x-1] != ficha and tabla[y-1][x-1]!=0):#diagonal izquierda arriba -------------------------------
                    lista[0] = x-1
                    lista[1] = y-1
                    LugarARevisar = 1
                    CondicionCumplida= self.EncontrarFichaAmiga(tabla,lista[0],lista[1],LugarARevisar,ficha) 
                    if(CondicionCumplida == True):
                        return CondicionCumplida # el movimiento es legal 


            if(x == 5 and y != 0  and y != 5  ): # derecha ---------------------------------------------------------###############################
                if(tabla[y-1][x]  != ficha and tabla[y-1][x] != 0): #arriba --------------------------
            
                    lista[0] = x
                    lista[1] = y-1
                    LugarARevisar =8
                    CondicionCumplida= self.EncontrarFichaAmiga(tabla,lista[0],lista[1],LugarARevisar,ficha)
                    if(CondicionCumplida == True):
                        return CondicionCumplida # el movimiento es lega
                if(tabla[y+1][x]  != ficha and tabla[y+1][x] != 0): #abajo --------------------------------------------------
           
                    lista[0]= x
                    lista[1] =y+1 
                    LugarARevisar = 6
                    CondicionCumplida= self.EncontrarFichaAmiga(tabla,lista[0],lista[1],LugarARevisar,ficha)
                    if(CondicionCumplida == True):
                        return CondicionCumplida # el movimiento es legal
                if(tabla[y][x-1]  != ficha and tabla[y][x-1] != 0): #izquierda ---------------------------------------------
                    lista[0]= x-1
                    lista[1] =y 
                    LugarARevisar = 7
                    CondicionCumplida= self.EncontrarFichaAmiga(tabla,lista[0],lista[1],LugarARevisar,ficha)
                    if(CondicionCumplida == True):
                        return CondicionCumplida # el movimiento es legal
                if(tabla[y-1][x-1] != ficha and tabla[y-1][x-1]!=0):#diagonal izquierda arriba -------------------------------
                    lista[0] = x-1
                    lista[1] = y-1
                    LugarARevisar = 1
                    CondicionCumplida= self.EncontrarFichaAmiga(tabla,lista[0],lista[1],LugarARevisar,ficha) 
                    if(CondicionCumplida == True):
                        return CondicionCumplida # el movimiento es legal
                if(tabla[y+1][x-1]  != ficha and tabla[y+1][x-1] != 0): #diagonal abajo izquierda ---------------------------
                    
                    lista[0]= x-1
                    lista[1] =y+1 
                    LugarARevisar = 4
                    CondicionCumplida= self.EncontrarFichaAmiga(tabla,lista[0],lista[1],LugarARevisar,ficha)
                    if(CondicionCumplida == True):
                        return CondicionCumplida # el movimiento es legal
            if(x!=0 and x !=5 and y != 0 and y !=5): #-------------------------------------------##########################
                if(tabla[y+1][x-1]  != ficha and tabla[y+1][x-1] != 0): #diagonal abajo izquierda ---------------------------
                        
                    lista[0]= x-1
                    lista[1] =y+1 
                    LugarARevisar = 4
                    CondicionCumplida= self.EncontrarFichaAmiga(tabla,lista[0],lista[1],LugarARevisar,ficha)
                    if(CondicionCumplida == True):
          
                        return CondicionCumplida # el movimiento es legal
                if(tabla[y-1][x-1] != ficha and tabla[y-1][x-1]!=0):#diagonal izquierda arriba -------------------------------
                
                    lista[0] = x-1
                    lista[1] = y-1
                    LugarARevisar = 1
                    CondicionCumplida= self.EncontrarFichaAmiga(tabla,lista[0],lista[1],LugarARevisar,ficha) 
                    if(CondicionCumplida == True):
                 
                        return CondicionCumplida # el movimiento es legal
                if(tabla[y][x-1]  != ficha and tabla[y][x-1] != 0): #izquierda ---------------------------------------------
               
                    lista[0]= x-1
                    lista[1] =y 
                    LugarARevisar = 7
                    CondicionCumplida= self.EncontrarFichaAmiga(tabla,lista[0],lista[1],LugarARevisar,ficha)
                    if(CondicionCumplida == True):
                        return CondicionCumplida # el movimiento es legal
                if(tabla[y-1][x]  != ficha and tabla[y-1][x] != 0): #arriba --------------------------
              
                    lista[0] = x
                    lista[1] = y-1
                    LugarARevisar =5
                    CondicionCumplida= self.EncontrarFichaAmiga(tabla,lista[0],lista[1],LugarARevisar,ficha)
                    if(CondicionCumplida == True):
                        return CondicionCumplida # el movimiento es lega
                if(tabla[y+1][x]  != ficha and tabla[y+1][x] != 0): #abajo --------------------------------------------------
          
                    lista[0]= x
                    lista[1] =y+1 
                    LugarARevisar = 6
                    CondicionCumplida= self.EncontrarFichaAmiga(tabla,lista[0],lista[1],LugarARevisar,ficha)
                    if(CondicionCumplida == True):
                        return CondicionCumplida # el movimiento es legal
                if(tabla[y-1][x+1]  != ficha and tabla[y-1][x+1] != 0): # diagonal arriba derecha -----------------------------------
         
                    lista[0]= x+1 
                    lista[1] =y-1 
                    LugarARevisar = 3
                    CondicionCumplida= self.EncontrarFichaAmiga(tabla,lista[0],lista[1],LugarARevisar,ficha)
                    if(CondicionCumplida == True):
         
                        return CondicionCumplida # el movimiento es legal
                if(tabla[y][x+1]  != ficha and tabla[y][x+1] != 0): #derecha -----------------------------

                    lista[0]= x+1 
                    lista[1] =y 
                    LugarARevisar = 8 
                    print("VALOR CONDIOCION1: ", CondicionCumplida)
                    CondicionCumplida= self.EncontrarFichaAmiga(tabla,lista[0],lista[1],LugarARevisar,ficha)
                    print("VALOR CONDIOCION2: ", CondicionCumplida)
                    if(CondicionCumplida == True):
                        return CondicionCumplida # el movimiento es legal
                if(tabla[y+1][x+1]  != ficha and tabla[y+1][x+1] != 0): #diagonal abajo derecha --------------------------

                    lista[0]= x+1
                    lista[1] =y+1 
                    LugarARevisar = 2
                    CondicionCumplida= self.EncontrarFichaAmiga(tabla,lista[0],lista[1],LugarARevisar,ficha)
                    print(CondicionCumplida)
                    if(CondicionCumplida == True):

                        return CondicionCumplida # el movimiento es legal
            return CondicionCumplida   




    def EncontrarFichaAmiga(self,tabla,x, y,LugarARevisar,ficha):
        case1 = x
        case2 = y
        MovimientoLegal = False
        if(LugarARevisar == 1 ): #diagonal izquierda arriba ----------------------------
            while(case1>= 0 and case2 >= 0):
                if(tabla[case2][case1] == ficha ):
                    MovimientoLegal = True
                    return MovimientoLegal
                else:
                    case1-=1
                    case2-=1
        case1 = x
        case2 = y

        if(LugarARevisar ==2 ): #diagonal abajo derecha ---------------------------------
            while(case1 <= 5 and case2 <=5):
 
                if(tabla[case2][case1] == ficha ):

                    MovimientoLegal = True
                    print(MovimientoLegal)
                    return MovimientoLegal
                else:
                    case1+=1
                    case2+=1
        case1 =x 
        case2 =y

        if(LugarARevisar ==3 ): #diagonal arriba derecha ---------------------------------
            while(case1 <= 5 and case2 >= 0):
                if(tabla[case2][case1]== ficha):
                    MovimientoLegal = True 
                    return MovimientoLegal
                else:
                    case1+=1
                    case2-=1
                
        case1 =x
        case2 =y


        if(LugarARevisar ==4 ): #diagonal abajo izquierda ---------------------------------
           while(case1 >= 0 and case2 <= 5):
                if(tabla[case2][case1]== ficha):
                    MovimientoLegal = True 
                    return MovimientoLegal
                else:
                    case1-=1
                    case2+=1
        
        case1 =x
        case2 =y

        if(LugarARevisar ==5 ): #arriba ----------------------------------------------------
            while(case2>=0 ):
                if(tabla[case2][case1] == ficha):
                    MovimientoLegal =True 
                    return MovimientoLegal
                else:
                    case2-=1
        case1 = x
        case2 = y
        if(LugarARevisar ==6 ): #abajo ------------------------------------------------------
            while(case2<=5 ):
                if(tabla[case2][case1] == ficha):
                    MovimientoLegal =True 
                    return MovimientoLegal
                else:
                    case2+=1
        case1 = x
        case2 = y
        if(LugarARevisar ==7 ): #izquierda --------------------------------------------------
            while(case1>=0 ):
                if(tabla[case2][case1] == ficha):
                    MovimientoLegal =True 
                    return MovimientoLegal
                else:
                    case1-=1
        case1 = x 
        case2 = y

        if(LugarARevisar == 8 ): #derecha ---------------------------------------------------
            while(case1 <=5 ):
                if(tabla[case2][case1] == ficha):
                    MovimientoLegal =True 
                    return MovimientoLegal
                else:
                    case1+=1

        return MovimientoLegal


    def __init__(self):
        self.tablero = cargar_tablero()
        self.valor_blanca = 0
        self.valor_negra = 0
        self.player = 1
                    #Fila,Columna
        self.tablero[2][2] = 2
        self.tablero[2][3] = 1
        self.tablero[3][2] = 1
        self.tablero[3][3] = 2
    
    def __setitem__(self, x,y, valor):
        self.tablero[x][y] = valor

    def start(self):
        self.__init__()
        print(self.tablero)
    
    
    def fill_column(self,columna,fila):
        dimencion = len(self.tablero)
        print("RANGOS UTILIZADOS: dimencion, x y ",dimencion,columna,fila)
        constante = fila
        if(self.player==1):
            x_temp = columna
            i=columna+1
            #derecha se le suma 1 a las columnas 
            while(i<5): #revisando las columnas a la derecha del movimiento del jugador 
                if(self.tablero[constante][i] == 0):
                    break
                if(self.tablero[constante][i]==1):
                    x_variable = i
                    y_variable = constante
                    while(x_temp < x_variable):
                        self.tablero[y_variable][x_temp] = 1
                        self.__setitem__(y_variable,x_temp,1)
                        print("dato 1 tablero: ",self.tablero[y_variable][x_temp])
                        x_temp+=1
                    break
                if(self.tablero[constante][i] == 2):
                    i+=1
            x_temp = columna
            i = columna-1
            while(i>0):
                if(self.tablero[constante][i] == 0):
                    break
                if(self.tablero[constante][i]==1):
                    x_variable = i
                    y_variable = constante
                    while(x_temp > x_variable):
                        self.tablero[y_variable][x_variable] = 1
                        self.__setitem__(y_variable,x_variable,1)
                        print("dato 1 tablero: ",self.tablero[y_variable][x_variable])
                        x_variable+=1
                    break
                if(self.tablero[constante][i] == 2):
                    i-=1
        if(self.player==2):
            x_temp = columna
            i=columna+1
            #derecha se le suma 1 a las columnas 
            while(i<5): #revisando las columnas a la derecha del movimiento del jugador 
                if(self.tablero[constante][i] == 0):
                    break
                if(self.tablero[constante][i]==2):
                    x_variable = i
                    y_variable = constante
                    while(x_temp < x_variable):
                        self.tablero[y_variable][x_temp] = 2
                        self.__setitem__(y_variable,x_temp,2)
                        print("dato 1 tablero: ",self.tablero[y_variable][x_temp])
                        x_temp+=1
                    break
                if(self.tablero[constante][i] == 1):
                    i+=1
            x_temp = columna
            i = columna-1
            while(i>=0):
                if(self.tablero[constante][i] == 0):
                    break
                if(self.tablero[constante][i]==2):
                    x_variable = i
                    y_variable = constante
                    while(x_temp > x_variable):
                        self.tablero[y_variable][x_variable] = 2
                        self.__setitem__(y_variable,x_variable,2)
                        print("dato 1 tablero: ",self.tablero[y_variable][x_variable])
                        x_variable+=1
                    break
                if(self.tablero[constante][i] == 1):
                    i-=1

        self.tablero = self.fill_row(columna,fila)
        return self.tablero
    

    def fill_row(self,columna,fila):
        constante = columna
        if(self.player==1):
            y_temp = fila
            i=fila+1
            #derecha se le suma 1 a las filas 
            while(i<5): #revisando las fllas a la derecha del movimiento del jugador 
                if(self.tablero[i][constante] == 0):
                    break
                if(self.tablero[i][constante]==1):
                    x_variable = constante
                    y_variable = i

                    while(y_temp < y_variable):
                        self.tablero[y_temp][x_variable] = 1
                        self.__setitem__(y_temp,x_variable,1)
                        print("dato 1 tablero: ",self.tablero[y_temp][x_variable])
                        y_temp+=1
                    break
                if(self.tablero[i][constante] == 2):
                    i+=1
            y_temp = fila
            i = fila-1
            while(i>0):
                if(self.tablero[i][constante] == 0):
                    break
                if(self.tablero[i][constante]==1):
                    x_variable = constante
                    y_variable = i
                    while(y_temp > y_variable):
                        self.tablero[y_variable][x_variable] = 1
                        self.__setitem__(y_variable,x_variable,1)
                        print("dato 1 tablero: ",self.tablero[y_variable][x_variable])
                        y_variable+=1
                    break
                if(self.tablero[i][constante] == 2):
                    i-=1
        constante = columna
        if(self.player==2):
            y_temp = fila
            i=fila+1
            #derecha se le suma 1 a las filas 
            while(i<5): #revisando las fllas a la derecha del movimiento del jugador 
                if(self.tablero[i][constante] == 0):
                    break
                if(self.tablero[i][constante]==2):
                    x_variable = constante
                    y_variable = i

                    while(y_temp < y_variable):
                        self.tablero[y_temp][x_variable] = 2
                        self.__setitem__(y_temp,x_variable,2)
                        print("dato 1 tablero: ",self.tablero[y_temp][x_variable])
                        y_temp+=1
                    break
                if(self.tablero[i][constante] == 1):
                    i+=1
            y_temp = fila
            i = fila-1
            while(i>0):
                if(self.tablero[i][constante] == 0):
                    break
                if(self.tablero[i][constante]==2):
                    x_variable = constante
                    y_variable = i
                    while(y_temp > y_variable):
                        self.tablero[y_variable][x_variable] = 2
                        self.__setitem__(y_variable,x_variable,2)
                        print("dato 1 tablero: ",self.tablero[y_variable][x_variable])
                        y_variable+=1
                    break
                if(self.tablero[i][constante] == 1):
                    i-=1
        
        self.tablero = self.fill_diag_sup(columna,fila)
       
        return self.tablero


    def fill_diag_sup(self,columna,fila):
        if(self.player==1):
            y_temp2 = fila
            x_temp2 = columna
            
            y_temp=fila-1
            x_temp=columna+1
            
            while(y_temp >0 and x_temp < 5): #revisamos la diagonal arriba derecha
                if(self.tablero[y_temp][x_temp] == 0):
                        break
                if(self.tablero[y_temp][x_temp]==1):
                        x_variable = x_temp
                        y_variable = y_temp

                        while(x_temp2 < x_variable and y_temp2 > y_variable):
                            self.tablero[y_temp2][x_temp2] = 1
                            self.__setitem__(y_temp2,x_temp2,1)
                            x_temp2+=1
                            y_temp2-=1
                        break 
                if(self.tablero[y_temp][x_temp] == 2):
                    y_temp-=1
                    x_temp+=1
            #revisamos la diagonal abajo izquierda
            y_temp2 = fila
            x_temp2 = columna
            
            y_temp = fila +1
            x_temp = columna -1
            while(y_temp < 5 and x_temp >0):
                if(self.tablero[y_temp][x_temp] == 0):
                        break
                if(self.tablero[y_temp][x_temp]==1):
                        x_variable = x_temp
                        y_variable = y_temp

                        while(x_temp2 > x_variable and y_temp2 < y_variable):
                            self.tablero[y_temp2][x_temp2] = 1
                            self.__setitem__(y_temp2,x_temp2,1)
                            x_temp2-=1
                            y_temp2+=1
                        break 
                if(self.tablero[y_temp][x_temp] == 2):
                    y_temp+=1
                    x_temp-=1
        if(self.player==2):
            y_temp2 = fila
            x_temp2 = columna
            
            y_temp=fila-1
            x_temp=columna+1
            
            while(y_temp >0 and x_temp < 5): #revisamos la diagonal arriba derecha
                if(self.tablero[y_temp][x_temp] == 0):
                        break
                if(self.tablero[y_temp][x_temp]==2):
                        x_variable = x_temp
                        y_variable = y_temp

                        while(x_temp2 < x_variable and y_temp2 > y_variable):
                            self.tablero[y_temp2][x_temp2] = 2
                            self.__setitem__(y_temp2,x_temp2,2)
                            x_temp2+=1
                            y_temp2-=1
                        break 
                if(self.tablero[y_temp][x_temp] == 1):
                    y_temp-=1
                    x_temp+=1
            #revisamos la diagonal abajo izquierda
            y_temp2 = fila
            x_temp2 = columna
            
            y_temp = fila +1
            x_temp = columna -1
            while(y_temp < 5 and x_temp >0):
                if(self.tablero[y_temp][x_temp] == 0):
                        break
                if(self.tablero[y_temp][x_temp]==2):
                        x_variable = x_temp
                        y_variable = y_temp

                        while(x_temp2 > x_variable and y_temp2 < y_variable):
                            self.tablero[y_temp2][x_temp2] = 2
                            self.__setitem__(y_temp2,x_temp2,2)
                            x_temp2-=1
                            y_temp2+=1
                        break 
                if(self.tablero[y_temp][x_temp] == 1):
                    y_temp+=1
                    x_temp-=1

        self.tablero = self.fill_diag_sup2(columna,fila)
        return self.tablero

    
    def fill_diag_sup2(self,columna,fila):
        if(self.player==1):
            y_temp2 = fila
            x_temp2 = columna
            
            y_temp=fila+1
            x_temp=columna+1
            
            while(y_temp <5 and x_temp < 5): #revisamos la diagonal abajo derecha
                if(self.tablero[y_temp][x_temp] == 0):
                        break
                if(self.tablero[y_temp][x_temp]==1):
                        x_variable = x_temp
                        y_variable = y_temp

                        while(x_temp2 < x_variable and y_temp2 < y_variable):
                            self.tablero[y_temp2][x_temp2] = 1
                            self.__setitem__(y_temp2,x_temp2,1)
                            x_temp2+=1
                            y_temp2+=1
                        break 
                if(self.tablero[y_temp][x_temp] == 2):
                    y_temp+=1
                    x_temp+=1
            #revisamos la diagonal arriba izquierda
            y_temp2 = fila
            x_temp2 = columna
            
            y_temp = fila -1
            x_temp = columna -1
            while(y_temp >0 and x_temp >0):
                if(self.tablero[y_temp][x_temp] == 0):
                        break
                if(self.tablero[y_temp][x_temp]==1):
                        x_variable = x_temp
                        y_variable = y_temp

                        while(x_temp2 > x_variable and y_temp2 > y_variable):
                            self.tablero[y_temp2][x_temp2] = 1
                            self.__setitem__(y_temp2,x_temp2,1)
                            x_temp2-=1
                            y_temp2-=1
                        break 
                if(self.tablero[y_temp][x_temp] == 2):
                    y_temp-=1
                    x_temp-=1
        if(self.player==2):
            y_temp2 = fila
            x_temp2 = columna
            
            y_temp=fila+1
            x_temp=columna+1
            
            while(y_temp <5 and x_temp < 5): #revisamos la diagonal abajo derecha
                if(self.tablero[y_temp][x_temp] == 0):
                        break
                if(self.tablero[y_temp][x_temp]==2):
                        x_variable = x_temp
                        y_variable = y_temp

                        while(x_temp2 < x_variable and y_temp2 < y_variable):
                            self.tablero[y_temp2][x_temp2] = 2
                            self.__setitem__(y_temp2,x_temp2,2)
                            x_temp2+=1
                            y_temp2+=1
                        break 
                if(self.tablero[y_temp][x_temp] == 1):
                    y_temp+=1
                    x_temp+=1
            #revisamos la diagonal arriba izquierda
            y_temp2 = fila
            x_temp2 = columna
            
            y_temp = fila -1
            x_temp = columna -1
            while(y_temp >0 and x_temp >0):
                if(self.tablero[y_temp][x_temp] == 0):
                        break
                if(self.tablero[y_temp][x_temp]==2):
                        x_variable = x_temp
                        y_variable = y_temp

                        while(x_temp2 > x_variable and y_temp2 > y_variable):
                            self.tablero[y_temp2][x_temp2] = 2
                            self.__setitem__(y_temp2,x_temp2,2)
                            x_temp2-=1
                            y_temp2-=1
                        break 
                if(self.tablero[y_temp][x_temp] == 1):
                    y_temp-=1
                    x_temp-=1

        return self.tablero


