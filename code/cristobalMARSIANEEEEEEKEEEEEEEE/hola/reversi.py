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
    
    
    def fill_column(self,x,y):
        print("1")
        lista=[0,0,0,0]
        
        dimencion = len(self.tablero)
        print("RANGOS UTILIZADOS: dimencion, x y ",dimencion,x,y)
        cont_column = 0
        constante = y
        findit1 = 0
        findit2 = 0
        if(self.player==1):
            for i in range(dimencion):
                if(self.tablero[i][constante]==1 and findit1 < 1):
                    lista[0] = i
                    lista[1] = constante
                    findit1+=1
                
                if(self.tablero[i][constante]==1 and findit1 < 2 and (self.tablero[i-1][constante]!=0)):
                    lista[2] = i
                    lista[3] = constante
                    findit1+=1
                    cont_column+=1
                
                if(self.tablero[i][constante]==1 and findit1 > 1 and (self.tablero[i-1][constante]!=0)):
                    lista[2] = i
                    lista[3] = constante
                    findit1+=1
                    cont_column+=1
                    if(findit1>1):
                        x_variable = lista[0]
                        y_variable = lista[1]

                        x1 = lista[2]
                        y1 = lista[3]
                        print("LISTA QUE ESTA REVISANDO",x_variable,y_variable,x1,y1)
                        while(x_variable <= x1):
                            self.tablero[x_variable][y1]=1
                            self.__setitem__(x_variable,y1,1)
  

                            print("dato 1 tablero: ",self.tablero[y_variable][x_variable])
                            x_variable+=1
            lista =[0,0,0,0]
        if(self.player==2):
            for i in range(dimencion):
                if(self.tablero[i][constante]==2 and findit2 < 1):
                    lista[0] = i
                    lista[1] = constante
                    findit2+=1
                if(self.tablero[i][constante]==2 and findit2 < 2 and (self.tablero[i-1][constante]!=0)):
                    lista[2] = i
                    lista[3] = constante
                    findit2+=1
                    cont_column+=1
                if(self.tablero[i][constante]==2 and findit2 > 1 and (self.tablero[i-1][constante]!=0)):
                    lista[2] = i
                    lista[3] = constante
                    findit2+=1
                    cont_column+=1
                    if(findit2 > 1):
                        x_variable = lista[0]
                        y_variable = lista[1]
                        x1 = lista[2]
                        y1 = lista[3]
                        print("LISTA QUE ESTA REVISANDO",x_variable,y_variable,x1,y1)
                        while(x_variable <= x1):
                            
                            self.tablero[x_variable][y1] = 2
                            self.__setitem__(x_variable,y1,2)
                            print("dato 2 tablero: ",self.tablero[y_variable][x_variable])
                            x_variable+=1
            lista =[0,0,0,0]
        
        self.tablero = self.fill_row(x,y)
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
            if(review==1): #Superior Izquierda
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

    
    
    
    
    

    
    #----------------------------------------------------------------------------------------------
    def EvalBoard(board, player):
        tot = 0
        for y in range(n):
            for x in range(n):
                if board[y][x] == player:
                    if (x == 0 or x == n - 1) and (y == 0 or y == n - 1):
                        tot += 4 # corner
                    elif (x == 0 or x == n - 1) or (y == 0 or y == n - 1):
                        tot += 2 # side
                    else:
                        tot += 1
        return tot
    def MakeMove(board, x, y, player): # assuming valid move
        totctr = 0 # total number of opponent pieces taken
        board[y][x] = player
        for d in range(8): # 8 directions
            ctr = 0
            for i in range(n):
                dx = x + dirx[d] * (i + 1)
                dy = y + diry[d] * (i + 1)
                if dx < 0 or dx > n - 1 or dy < 0 or dy > n - 1:
                    ctr = 0; break
                elif board[dy][dx] == player:
                    break
                elif board[dy][dx] == '0':
                    ctr = 0; break
                else:
                    ctr += 1
            for i in range(ctr):
                dx = x + dirx[d] * (i + 1)
                dy = y + diry[d] * (i + 1)
                board[dy][dx] = player
            totctr += ctr
        return (board, totctr)

    def ValidMove(board, x, y, player):
        if x < 0 or x > n - 1 or y < 0 or y > n - 1:
            return False
        if board[y][x] != '0':
            return False
        (boardTemp, totctr) = MakeMove(copy.deepcopy(board), x, y, player)
        if totctr == 0:
            return False
        return True



        # if no valid move(s) possible then True
    def IsTerminalNode(board, player):
        for y in range(n):
            for x in range(n):
                if ValidMove(board, x, y, player):
                    return False
        return True

    def GetSortedNodes(board, player):
        sortedNodes = []
        for y in range(n):
            for x in range(n):
                if ValidMove(board, x, y, player):
                    (boardTemp, totctr) = MakeMove(copy.deepcopy(board), x, y, player)
                    sortedNodes.append((boardTemp, EvalBoard(boardTemp, player)))
        sortedNodes = sorted(sortedNodes, key = lambda node: node[1], reverse = True)
        sortedNodes = [node[0] for node in sortedNodes]
        return sortedNodes
        
    def AlphaBeta(board, player, depth, alpha, beta, maximizingPlayer):
        if depth == 0 or IsTerminalNode(board, player):
            return EvalBoard(board, player)

        if maximizingPlayer:
            v = minEvalBoard
            for y in range(n):
                for x in range(n):
                    if ValidMove(board, x, y, player):
                        (boardTemp, totctr) = MakeMove(copy.deepcopy(board), x, y, player)
                        v = max(v, AlphaBeta(boardTemp, player, depth - 1, alpha, beta, False))
                        alpha = max(alpha, v)
                        if beta <= alpha:
                            break # beta cut-off
            return v
        else: # minimizingPlayer
            v = maxEvalBoard
            for y in range(n):
                for x in range(n):
                    if ValidMove(board, x, y, player):
                        (boardTemp, totctr) = MakeMove(copy.deepcopy(board), x, y, player)
                        v = min(v, AlphaBeta(boardTemp, player, depth - 1, alpha, beta, True))
                        beta = min(beta, v)
                        if beta <= alpha:
                            break # alpha cut-off
            return v

    def BestMove(board, player):
        maxPoints = 0
        mx = -1; my = -1
        inicio=default_timer()
        for y in range(n):
            for x in range(n):
                if ValidMove(board, x, y, player):
                    (boardTemp, totctr) = MakeMove(copy.deepcopy(board), x, y, player)
                    if opt == 0:
                        points = EvalBoard(boardTemp, player) 
                    elif opt == 1:
                        
                        points = Minimax(boardTemp, player, depth, True)
                    elif opt == 2:
                        points = AlphaBeta(board, player, depth, minEvalBoard, maxEvalBoard, True)
                        
                    elif opt == 3:
                        points = AlphaBetaSN(board, player, depth, minEvalBoard, maxEvalBoard, True)

                    if points > maxPoints:
                        maxPoints = points
                        mx = x; my = y
        fin=default_timer()
        print(fin-inicio)               
        return (mx, my)

    #-----------------------------------------------------------------------------------------------

        pass


