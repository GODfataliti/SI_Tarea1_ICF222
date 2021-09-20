


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
        self.tablero[2][2] = 2
        self.tablero[2][3] = 1
        self.tablero[3][2] = 1
        self.tablero[3][3] = 2
    
    def start(self):
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
                            valor = 1
                            self.tablero[x_variable][y1]=1
                            if(self.tablero[x_variable][y1]!=1):
                                self.tablero[x_variable][y1]=1
                                print("aun no puedo salir")

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
        if(self.player==1):
            for i in range(dimencion):
                if(self.tablero[constante][i]==1 and findit1 < 1):
                    lista[0] = constante
                    lista[1] = i
                    findit1+=1
                if(self.tablero[constante][i]==1 and findit1 < 2 and (self.tablero[constante][i-1]!=0)):
                    lista[2] = constante
                    lista[3] = i
                    findit1+=1
                    cont_row+=1
                if(self.tablero[constante][i]==1 and findit1 > 1 and (self.tablero[constante][i-1]!=0)):
                    lista[2] = constante
                    lista[3] = i
                    findit1+=1
                    cont_row+=1
                    if(findit1>1):
                        x_variable = lista[0]
                        y_variable = lista[1]
                        x1 = lista[2]
                        y1 = lista[3]
                        print("LISTA QUE ESTA REVISANDO",x_variable,y_variable,x1,y1)
                        while(y_variable <= y1):
                            valor = 1
                            self.tablero[x_variable][y_variable] = 1
                            print("dato 1 tablero: ",self.tablero[y_variable][x_variable])
                            if(self.tablero[x_variable][y1]!=1):
                                self.tablero[x_variable][y1]=1
                                print("aun no puedo salir")
                            y_variable+=1
            lista =[0,0,0,0]
        if(self.player==2):
            for i in range(dimencion):
                if(self.tablero[constante][i]==2 and findit2 < 1):
                    lista[0] = constante
                    lista[1] = i
                    findit2+=1
                if(self.tablero[constante][i]==2 and findit2 < 2 and (self.tablero[constante][i-1]!=0)):
                    lista[2] = constante
                    lista[3] = i
                    findit2+=1
                    cont_row+=1
                if(self.tablero[constante][i]==2 and findit2 > 1 and (self.tablero[constante][i-1]!=0)):
                    lista[2] = constante
                    lista[3] = i
                    findit2+=1
                    cont_row+=1
                    if(findit2>1):
                        x_variable = lista[0]
                        y_variable = lista[1]
                        x1 = lista[2]
                        y1 = lista[3]
                        print("LISTA QUE ESTA REVISANDO",x_variable,y_variable,x1,y1)
                        while(y_variable <= 1):
                            
                            self.tablero[x_variable][y_variable] = 2
                            print("dato 2  tablero: ",self.tablero[y_variable][x_variable])
                            y_variable+=1
            lista =[0,0,0,0]
        
        self.tablero = self.fill_diag_sup(x,y)
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
                                valor = 1
                                self.tablero[x_variable][y_variable]=1
                                print("dato 1 tablero: ",self.tablero[y_variable][x_variable])
                                if(self.tablero[x_variable][y1]!=1):
                                    self.tablero[x_variable][y1]=1
                                    print("aun no puedo salir")
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
                while(case1 >0 and case2 <5):
                    case1-=1
                    case2+=1
                    cont+=1
                while(case1 <5 and case2 >0):
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
                                if(self.tablero[x_variable][y1]!=1):
                                    self.tablero[x_variable][y1]=1
                                    print("aun no puedo salir")
                                y_variable-=1
                                x_variable+=1
                    case1+=1
                    case2-=1
        print("sali")
        if(self.player==2):
            if(review==1): #Superior Izquierda
                while(case1 >0 and case2 <5):
                    case1-=1
                    case2+=1
                    cont+=1
                while(case1 <5 and case2 >0):
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
                    if(self.tablero[case2][case1]==2 and findit2 > 1):
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

                                y_variable-=1
                                x_variable+=1
                                print("dato 2 tablero: ",self.tablero[y_variable][x_variable])
                    case1+=1
                    case2-=1
            print("sali de player 2 ")
        return self.tablero



