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
                    if(tabla[y][x+1]  != ficha and tabla[x+1][y] != 0): #derecha -----------------------------
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
            
            elif( x != 0 and y == 0 and x != 5  ): # izquierda --------------------------------------------------------------------------------##############
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
                if(tabla[y][x+1]  != ficha and tabla[x+1][y] != 0): #derecha -----------------------------
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
            elif(x == 0 and y != 0 and y != 5 ): # arriba ------------------------------------------------------------###############################
                if(tabla[y][x-1]  != ficha and tabla[y][x-1] != 0): #izquierda ---------------------------------------------
                        lista[0]= x-1
                        lista[1] =y 
                        LugarARevisar = 7
                        CondicionCumplida= self.EncontrarFichaAmiga(tabla,lista[0],lista[1],LugarARevisar,ficha)
                        if(CondicionCumplida == True):
                            return CondicionCumplida # el movimiento es legal
                if(tabla[y][x+1]  != ficha and tabla[x+1][y] != 0): #derecha -----------------------------
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
                

            elif(x == 5 and y != 0  and y != 5 ): # abajo --------------------------------------##################################################
                if(tabla[y][x+1]  != ficha and tabla[x+1][y] != 0): #derecha -----------------------------
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


            elif(x != 0 and y == 5 and x != 5 ): # derecha ---------------------------------------------------------###############################
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
            else: #-------------------------------------------##########################
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
                if(tabla[y][x+1]  != ficha and tabla[x+1][y] != 0): #derecha -----------------------------
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
            return CondicionCumplida   




    def EncontrarFichaAmiga(self,tabla,x, y,LugarARevisar,ficha):
        case1 = x
        case2 = y
        MovimientoLegal = False
        if(LugarARevisar == 1 ): #diagonal izquierda arriba ----------------------------
            while(case1>= 0 and case2 >= 0):
                if(tabla[case2][case1] == ficha ):
                    MovimientoLegal == True
                    return MovimientoLegal
                else:
                    case1-=1
                    case2-=1
        case1 = x
        case2 = y

        if(LugarARevisar ==2 ): #diagonal abajo derecha ---------------------------------
            while(case1 < 5 and case2 <5):
                if(tabla[case2][case1] == ficha ):
                    MovimientoLegal == True
                    return MovimientoLegal
                else:
                    case1+=1
                    case2+=1
        case1 =x 
        case2 =y

        if(LugarARevisar ==3 ): #diagonal arriba derecha ---------------------------------
            while(case1 <5 and case2 >0):
                if(tabla[case2][case1]== ficha):
                    MovimientoLegal = True 
                    return MovimientoLegal
                else:
                    case1+=1
                    case2-=1
                
        case1 =x
        case2 =y


        if(LugarARevisar ==4 ): #diagonal abajo izquierda ---------------------------------
           while(case1 > 5 and case2 < 0):
                if(tabla[case2][case1]== ficha):
                    MovimientoLegal = True 
                    return MovimientoLegal
                else:
                    case1-=1
                    case2+=1
        
        case1 =x
        case2 =y

        if(LugarARevisar ==5 ): #arriba ----------------------------------------------------
            while(case2>0 ):
                if(tabla[case2][case1] == ficha):
                    MovimientoLegal =True 
                    return MovimientoLegal
                else:
                    case2-=1
        case1 = x
        case2 = y
        if(LugarARevisar ==6 ): #abajo ------------------------------------------------------
            while(case2<5 ):
                if(tabla[case2][case1] == ficha):
                    MovimientoLegal =True 
                    return MovimientoLegal
                else:
                    case2+=1
        case1 = x
        case2 = y
        if(LugarARevisar ==7 ): #izquierda --------------------------------------------------
            while(case1>0 ):
                if(tabla[case2][case1] == ficha):
                    MovimientoLegal =True 
                    return MovimientoLegal
                else:
                    case1-=1
        case1 = x 
        case2 = y

        if(LugarARevisar == 8 ): #derecha ---------------------------------------------------
            while(case1 <5 ):
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

    def start(self,dificultad):
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
            while(i>0):
                if(self.tablero[constante][i] == 0):
                    break
                if(self.tablero[constante][i]==1):
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
    

    def fill_row(self,x,y):
        print("2")
        lista=[0,0,0,0]
        dimencion = len(self.tablero)
        print("RANGOS UTILIZADOS: dimencion, x y ",dimencion,x,y)

        cont_row = 0
        constante = x
        findit1 = 0
        findit2 = 0
        print("____________________ENTRE A FILA _____________________")
        if(self.player==1):
            print("____________________INICIANDO ¨FOR _____________________")
            for i in range(dimencion):
                
                if(self.tablero[constante][i]==1 and findit1 < 1):
                    print("constante y i : ",constante,i)
                    lista[0] = constante
                    lista[1] = i
                    findit1+=1
                    print("lista 0, lista 1, findit1",lista[0],lista[1],findit1)
                if(self.tablero[constante][i]==1 and findit1 < 2 and (self.tablero[constante][i-1]!=0)):
                    print("constante y i : ",constante,i)
                    lista[2] = constante
                    lista[3] = i
                    findit1+=1
                    cont_row+=1
                    print("lista 0, lista 1, findit1",lista[0],lista[1],findit1)
                if(self.tablero[constante][i]==1 and findit1 > 1 and (self.tablero[constante][i-1]!=0)):
                    print("constante y i : ",constante,i)
                    lista[2] = constante
                    lista[3] = i
                    findit1+=1
                    cont_row+=1
                    print("lista 0, lista 1, findit1",lista[0],lista[1],findit1)
                    if(findit1>1):
                        x_variable = lista[0]
                        y_variable = lista[1]
                        x1 = lista[2]
                        y1 = lista[3]
                        print("LISTA QUE ESTA REVISANDO",x_variable,y_variable,x1,y1)
                        while(y_variable <= y1):
                            self.tablero[x_variable][y_variable] = 1
                            print("dato 1 tablero: ",self.tablero[y_variable][x_variable])
                            self.__setitem__(x_variable,y_variable,1)
                            y_variable+=1
            lista =[0,0,0,0]
        if(self.player==2):
            print("____________________INICIANDO ¨FOR _____________________")
            for i in range(dimencion):
                
                if(self.tablero[constante][i]==2 and findit2 < 1):
                    print("constante y i : ",constante,i)
                    lista[0] = constante
                    lista[1] = i
                    findit2+=1
                    print("lista 0, lista 1, findit2",lista[0],lista[1],findit2)
                if(self.tablero[constante][i]==2 and findit2 < 2 and (self.tablero[constante][i-1]!=0)):
                    print("constante y i : ",constante,i)
                    lista[2] = constante
                    lista[3] = i
                    findit2+=1
                    print("lista 0, lista 1, findit2",lista[0],lista[1],findit2)
                    cont_row+=1
                if(self.tablero[constante][i]==2 and findit2 > 1 and (self.tablero[constante][i-1]!=0)):
                    print("constante y i : ",constante,i)
                    lista[2] = constante
                    lista[3] = i
                    findit2+=1
                    cont_row+=1
                    print("lista 0, lista 1, findit2",lista[0],lista[1],findit2)
                    if(findit2>1):
                        x_variable = lista[0]
                        y_variable = lista[1]
                        x1 = lista[2]
                        y1 = lista[3]
                        print("LISTA QUE ESTA REVISANDO",x_variable,y_variable,x1,y1)
                        while(y_variable <= y1):
                            
                            self.tablero[x_variable][y_variable] = 2


                            self.__setitem__(x_variable,y_variable,2)
                            print("dato 2  tablero: ",self.tablero[y_variable][x_variable])
                            y_variable+=1
            lista =[0,0,0,0]
        
        self.tablero = self.fill_diag_sup(x,y)
        print("____________________SALI DE FILA _____________________")
        return self.tablero
        
        
    
    def fill_diag_sup(self,x,y):
        print("3")
        lista=[0,0,0,0]
        dimencion = len(self.tablero)
        print("RANGOS UTILIZADOS: dimencion, x y ",dimencion,x,y)
        cont_diag = 0
        case1 = x
        case2 = y
        review = 1
        findit1 = 0
        findit2 = 0
        if(self.player==1):
            if(review==1): #Superior izquierda
                while(case1>=0 and case2>=0):
                    case1-=1
                    case2-=1
                while(case1 <= 5 and case2 <=5):
                    if(self.tablero[case1][case2]==1 and findit1<1):
                        lista[0] = case1
                        lista[1] = case2
                        findit1+=1
                    if(self.tablero[case1][case2]==1 and findit1 < 2 and (self.tablero[case1-1][case2-1]!=0)):
                        lista[2] = case1
                        lista[3] = case2
                        findit1+=1
                    if(self.tablero[case1][case2]==1 and findit1 > 1 and (self.tablero[case1-1][case2-1]!=0)):
                        lista[2] = case1
                        lista[3] = case2
                        findit1+=1
                        if(findit1>1):
                            x_variable = lista[0]
                            y_variable = lista[1]
                            x1 = lista[2]
                            y1 = lista[3]
                            print("LISTA QUE ESTA REVISANDO",x_variable,y_variable,x1,y1)
                            while(x_variable<=x1 and y_variable<=y1):
                                self.tablero[x_variable][y_variable]=1
                                print("dato 1 tablero: ",self.tablero[y_variable][x_variable])
                                self.__setitem__(x_variable,y_variable,1)
                                y_variable+=1
                                x_variable+=1
                    case1+=1
                    case2+=1
        if(self.player==2):
            if(review==1): #Superior izquierda
                while(case1>=0 and case2>=0):
                    case1-=1
                    case2-=1
                while(case1 <= 5 and case2 <=5):
                    if(self.tablero[case1][case2]==2 and findit2<1):
                        lista[0] = case1
                        lista[1] = case2
                        findit2+=1
                    if(self.tablero[case1][case2]==2 and findit2 < 2 and (self.tablero[case1-1][case2-1]!=0)):
                        lista[2] = case1
                        lista[3] = case2
                        findit2+=1
                    if(self.tablero[case1][case2]==2 and findit2 > 1 and (self.tablero[case1-1][case2-1]!=0)):
                        lista[2] = case1
                        lista[3] = case2
                        findit2+=1
                        if(findit2>1):
                            x_variable = lista[0]
                            y_variable = lista[1]
                            x1 = lista[2]
                            y1 = lista[3]
                            print("LISTA QUE ESTA REVISANDO",x_variable,y_variable,x1,y1)
                            while(x_variable<=x1 and y_variable<=y1):
                                self.tablero[x_variable][y_variable]= 2
                                self.__setitem__(x_variable,y_variable,2)
                                print("dato 2 tablero: ",self.tablero[y_variable][x_variable])
                                y_variable+=1
                                x_variable+=1
                    case1+=1
                    case2+=1
        self.tablero = self.fill_diag_sup2(x,y)
        return self.tablero

    
    def fill_diag_sup2(self,x,y):
        print("4")
        lista=[0,0,0,0]
        dimencion = len(self.tablero)
        print("RANGOS UTILIZADOS: dimencion, x y ",dimencion,x,y)
        cont_diag = 0
        case1 = x
        case2 = y
        review = 1
        findit1 = 0
        findit2 = 0
        cont = 0
        if(self.player==1):
            print("pllegue a 1 ")
            if(review==1): #Superior derecha
                print("pllegue a 2 ")
                print("primer case: ",case1,case2)
                while(case1 >0 and case2 <5):
                    print("dentro del while: ",case1,case2)
                    case1= case1-1
                    case2+=1
                    cont+=1
                while(case1 <=5 and case2 >=0):
                    if(self.tablero[case2][case1]==1 and findit1< 1):
                        lista[0] = case1
                        lista[1] = case2
                        findit1+=1
                    if(self.tablero[case2][case1]==1 and findit1 < 2):
                        lista[2] = case1
                        lista[3] = case2
                        findit1+=1
                    if(self.tablero[case2][case1]==1 and findit1 > 1):
                        lista[2] = case1
                        lista[3] = case2
                        findit1+=1
                        if(findit1>1):
                            x_variable = lista[0]
                            y_variable = lista[1]
                            x1 = lista[2]
                            y1 = lista[3]
                            print("LISTA QUE ESTA REVISANDO",x_variable,y_variable,x1,y1)
                            print("pllegue a 3 ")
                            while(x_variable<=x1 and y_variable>=1):
                                self.tablero[y_variable][x_variable]=1
                                print("dato 1 tablero: ",self.tablero[y_variable][x_variable])
                                self.__setitem__(y_variable,x_variable,1)
                                y_variable-=1
                                x_variable+=1
                    case1+=1
                    case2-=1
        print("sali")
        if(self.player==2):
            if(review==1): #Superior Izquierda
                print("primer case: ",case1,case2)
                while(case1 >0 and case2 <5):
                    print("dentro del while: ",case1,case2)
                    case1-=1
                    case2+=1
                    cont+=1
                while(case1 <=5 and case2 >=0):
                    if(self.tablero[case2][case1]==2 and findit2< 1):
                        lista[0] = case1
                        lista[1] = case2
                        findit2+=1
                        print("saliendo del primer if")
                    if(self.tablero[case2][case1]==2 and findit2 < 2):
                        lista[2] = case1
                        lista[3] = case2
                        findit2+=1
                        print("saliendo del 2 if")
                        print(findit2)
                    if(self.tablero[case2][case1]==2 and findit2 > 1 ):
                        lista[2] = case1
                        lista[3] = case2
                        findit2+=1
                        print(findit2)
                        if(findit2 > 1):
                            x_variable = lista[0]
                            y_variable = lista[1]
                            x1 = lista[2]
                            y1 = lista[3]
                            print("LISTA QUE ESTA REVISANDO: el player2: ",x_variable,y_variable,x1,y1)
                            while(x_variable<=x1 and y_variable>=y1):
                                print("calculanding")
                                
                                self.tablero[y_variable][x_variable]= 2
                                self.__setitem__(y_variable,x_variable,2)
                                y_variable-=1
                                x_variable+=1
                                print("dato 2 tablero: ",self.tablero[y_variable][x_variable])
                    case1+=1
                    case2-=1
            print("sali de player 2 ")
        return self.tablero

    
    
    
    
    

    
    # #----------------------------------------------------------------------------------------------
    # def EvalBoard(board, player):
    #     tot = 0
    #     for y in range(n):
    #         for x in range(n):
    #             if board[y][x] == player:
    #                 if (x == 0 or x == n - 1) and (y == 0 or y == n - 1):
    #                     tot += 4 # corner
    #                 elif (x == 0 or x == n - 1) or (y == 0 or y == n - 1):
    #                     tot += 2 # side
    #                 else:
    #                     tot += 1
    #     return tot
    # def MakeMove(board, x, y, player): # assuming valid move
    #     totctr = 0 # total number of opponent pieces taken
    #     board[y][x] = player
    #     for d in range(8): # 8 directions
    #         ctr = 0
    #         for i in range(n):
    #             dx = x + dirx[d] * (i + 1)
    #             dy = y + diry[d] * (i + 1)
    #             if dx < 0 or dx > n - 1 or dy < 0 or dy > n - 1:
    #                 ctr = 0; break
    #             elif board[dy][dx] == player:
    #                 break
    #             elif board[dy][dx] == '0':
    #                 ctr = 0; break
    #             else:
    #                 ctr += 1
    #         for i in range(ctr):
    #             dx = x + dirx[d] * (i + 1)
    #             dy = y + diry[d] * (i + 1)
    #             board[dy][dx] = player
    #         totctr += ctr
    #     return (board, totctr)

    # def ValidMove(board, x, y, player):
    #     if x < 0 or x > n - 1 or y < 0 or y > n - 1:
    #         return False
    #     if board[y][x] != '0':
    #         return False
    #     (boardTemp, totctr) = MakeMove(copy.deepcopy(board), x, y, player)
    #     if totctr == 0:
    #         return False
    #     return True



    #     # if no valid move(s) possible then True
    # def IsTerminalNode(board, player):
    #     for y in range(n):
    #         for x in range(n):
    #             if ValidMove(board, x, y, player):
    #                 return False
    #     return True

    # def GetSortedNodes(board, player):
    #     sortedNodes = []
    #     for y in range(n):
    #         for x in range(n):
    #             if ValidMove(board, x, y, player):
    #                 (boardTemp, totctr) = MakeMove(copy.deepcopy(board), x, y, player)
    #                 sortedNodes.append((boardTemp, EvalBoard(boardTemp, player)))
    #     sortedNodes = sorted(sortedNodes, key = lambda node: node[1], reverse = True)
    #     sortedNodes = [node[0] for node in sortedNodes]
    #     return sortedNodes
        
    # def AlphaBeta(board, player, depth, alpha, beta, maximizingPlayer):
    #     if depth == 0 or IsTerminalNode(board, player):
    #         return EvalBoard(board, player)

    #     if maximizingPlayer:
    #         v = minEvalBoard
    #         for y in range(n):
    #             for x in range(n):
    #                 if ValidMove(board, x, y, player):
    #                     (boardTemp, totctr) = MakeMove(copy.deepcopy(board), x, y, player)
    #                     v = max(v, AlphaBeta(boardTemp, player, depth - 1, alpha, beta, False))
    #                     alpha = max(alpha, v)
    #                     if beta <= alpha:
    #                         break # beta cut-off
    #         return v
    #     else: # minimizingPlayer
    #         v = maxEvalBoard
    #         for y in range(n):
    #             for x in range(n):
    #                 if ValidMove(board, x, y, player):
    #                     (boardTemp, totctr) = MakeMove(copy.deepcopy(board), x, y, player)
    #                     v = min(v, AlphaBeta(boardTemp, player, depth - 1, alpha, beta, True))
    #                     beta = min(beta, v)
    #                     if beta <= alpha:
    #                         break # alpha cut-off
    #         return v

    # def BestMove(board, player):
    #     maxPoints = 0
    #     mx = -1; my = -1
    #     inicio=default_timer()
    #     for y in range(n):
    #         for x in range(n):
    #             if ValidMove(board, x, y, player):
    #                 (boardTemp, totctr) = MakeMove(copy.deepcopy(board), x, y, player)
    #                 if opt == 0:
    #                     points = EvalBoard(boardTemp, player) 
    #                 elif opt == 1:
                        
    #                     points = Minimax(boardTemp, player, depth, True)
    #                 elif opt == 2:
    #                     points = AlphaBeta(board, player, depth, minEvalBoard, maxEvalBoard, True)
                        
    #                 elif opt == 3:
    #                     points = AlphaBetaSN(board, player, depth, minEvalBoard, maxEvalBoard, True)

    #                 if points > maxPoints:
    #                     maxPoints = points
    #                     mx = x; my = y
    #     fin=default_timer()
    #     print(fin-inicio)               
    #     return (mx, my)

    #-----------------------------------------------------------------------------------------------

        pass


