import numpy as np
def Hacertablero():
    board = [[0 for x in range(6)] for x in range(6)]
    board[2][2]=2
    board[2][3]=1
    board[3][2]=1
    board[3][3]=2
    return board

def imprimirTablero(TableroJugada):
  for fila in TableroJugada:
   print(f'{fila}', end="\n")

def busquedaRellenoColumna(TableroJugada,x,y,jugador):
  lista=[0,0,0,0]
  Dimencion =len(TableroJugada)
  contCol=0
  constante = y
  encontradas1=0
  encontradas2=0
  if(jugador == 1):
    for i in range(Dimencion):
      if(TableroJugada[i][constante]==1 and encontradas1 <1):
        lista[0] = i
        lista[1] = constante
        encontradas1 +=1
      if(TableroJugada[i][constante]==1 and encontradas1 <2 and (TableroJugada[i-1][constante]!=0)):
        lista[2] = i
        lista[3] = constante
        encontradas1 +=1
        contCol+=1
      if(TableroJugada[i][constante]==1 and encontradas1 >1 and (TableroJugada[i-1][constante]!=0)):
        lista[2] = i
        lista[3] = constante
        encontradas1 +=1
        contCol+=1
        if (encontradas1>1):
          xvariable = lista[0]
          yvariable = lista[1]
          x1= lista[2]
          y1= lista[3]   
          while(xvariable <= x1):
            TableroJugada[xvariable][y1] = 1
            xvariable +=1
    lista =[0,0,0,0]
  if (jugador == 2):
    for i in range(Dimencion):            
      if(TableroJugada[i][constante]==2 and encontradas2 <1):
        lista[0] = i
        lista[1] = constante
        encontradas2 +=1
      if(TableroJugada[i][constante]==2 and encontradas2 <2 and (TableroJugada[i-1][constante]!=0)):
        lista[2] = i
        lista[3] = constante
        encontradas2 +=1
        contCol+=1
      if(TableroJugada[i][constante]==2 and encontradas2 >1 and (TableroJugada[i-1][constante]!=0)):
        lista[2] = i
        lista[3] = constante
        encontradas2 +=1
        contCol+=1
        if (encontradas2>1):
          xvariable = lista[0]
          yvariable = lista[1]
          x1= lista[2]
          y1= lista[3]
          while(xvariable <= x1):
            TableroJugada[xvariable][y1] = 2
            xvariable +=1
    lista =[0,0,0,0]
  TableroJugada = BusquedaRellenoFila(TableroJugada,x,y,jugador)
  return TableroJugada

def BusquedaRellenoFila(TableroJugada,x,y,jugador):
  lista=[0,0,0,0]
  Dimencion =len(TableroJugada)
  contFila = 0
  constante = x
  encontradas1=0
  encontradas2=0
  if(jugador == 1):
    for i in range(Dimencion):
      if(TableroJugada[constante][i]==1 and encontradas1 <1):
        lista[0] = constante
        lista[1] = i
        encontradas1 +=1
      if(TableroJugada[constante][i]==1 and encontradas1 <2 and (TableroJugada[constante][i-1]!=0)):
        lista[2] = constante
        lista[3] = i
        encontradas1 +=1
        contFila+=1
      if(TableroJugada[i][constante]==1 and encontradas1 >1 and (TableroJugada[constante][i-1]!=0)):
        lista[2] = constante
        lista[3] = i
        encontradas1 +=1
        contFila+=1
        if (encontradas1>1):
          xvariable = lista[0]
          yvariable = lista[1]
          x1= lista[2]
          y1= lista[3]
          while(yvariable <= y1):
            TableroJugada[xvariable][yvariable] = 1
            yvariable +=1
    lista =[0,0,0,0]
  if(jugador == 2):
    for i in range(Dimencion):
      if(TableroJugada[constante][i]==2 and encontradas2 <1):
        lista[0] = constante
        lista[1] = i
        encontradas2 +=1
      if(TableroJugada[constante][i]==2 and encontradas2 <2 and (TableroJugada[constante][i-1]!=0)):
        lista[2] = constante
        lista[3] = i
        encontradas2 +=1
        contFila+=1
      if(TableroJugada[i][constante]==2 and encontradas2 >1 and (TableroJugada[constante][i-1]!=0)):
        lista[2] = constante
        lista[3] = i
        encontradas2 +=1
        contFila+=1
        if (encontradas2>1):
          xvariable = lista[0]
          yvariable = lista[1]
          x1= lista[2]
          y1= lista[3]
          while(yvariable <= y1):
            TableroJugada[xvariable][yvariable] = 2
            yvariable +=1
    lista =[0,0,0,0]
  TableroJugada = BusquedaRellenoDiagonal(TableroJugada,x,y,jugador)
  return TableroJugada

def BusquedaRellenoDiagonal(TableroJugada,x,y,jugador):
  print("prueba")
  lista=[0,0,0,0]
  Dimencion =len(TableroJugada)
  contDiag=0
  case1 =x
  case2 =y
  revisar = 1 
  encontradas1 =0
  encontradas2 =0
  if(jugador ==1): 
    if(revisar == 1): #este es  revisar para la diagonal superior izquierda 
      while(case1 >=0 and case2 >=0):
        case1 = case1-1
        case2 = case2-1
        print("RESTANDO RESTANDO::::::::::::::::::::::::::")
      print("sali del while")
      while(case1 <=5 and case2 <=5 ):
        print("estoy antes del primer if: ")
        if(TableroJugada[case1][case2] == 1 and encontradas1 <1):
          lista[0] = case1
          lista[1] = case2
          encontradas1 +=1
          print("QUE EH LLEGAO1")
        if(TableroJugada[case1][case2]==1 and encontradas1 <2 and (TableroJugada[case1-1][case2-1]!=0)):
          lista[2] = case1
          lista[3] = case2
          encontradas1 +=1
          print("QUE EH LLEGAO2")
        if (TableroJugada[case1][case2]==1 and encontradas1 >1 and (TableroJugada[case1-1][case2-1]!=0)):
          lista[2] = case1
          lista[3] = case2
          encontradas1 +=1
          print("QUE EH LLEGAO3")
          if (encontradas1>1):
            xvariable = lista[0]
            yvariable = lista[1]
            x1= lista[2]
            y1= lista[3]
            print("QUE EH LLEGAO4")
            while(xvariable<=x1 and yvariable<=y1):
              TableroJugada[xvariable][yvariable] =1
              yvariable +=1
              xvariable+=1
        case1+=1
        case2+=1
      print("sali del 2 while")
  if(jugador==2):
    if(revisar == 1): #este es  revisar para la diagonal superior izquierda 
      while(case1 >=0 and case2 >=0):
        case1 = case1-1
        case2 = case2-1
        print("RESTANDO RESTANDO::::::::::::::::::::::::::")
      print("sali del while")
      while(case1 <=5 and case2 <=5 ):
        print("estoy antes del primer if: ")
        if(TableroJugada[case1][case2] == 2 and encontradas2 <1):
          lista[0] = case1
          lista[1] = case2
          encontradas2 +=1
          print("QUE EH LLEGAO1")
        if(TableroJugada[case1][case2]==2 and encontradas2 <2 and (TableroJugada[case1-1][case2-1]!=0)):
          lista[2] = case1
          lista[3] = case2
          encontradas2 +=1
          print("QUE EH LLEGAO2")
        if (TableroJugada[case1][case2]==2 and encontradas2 >1 and (TableroJugada[case1-1][case2-1]!=0)):
          lista[2] = case1
          lista[3] = case2
          encontradas2 +=1
          print("QUE EH LLEGAO3")
          if (encontradas2>1):
            xvariable = lista[0]
            yvariable = lista[1]
            x1= lista[2]
            y1= lista[3]
            print("QUE EH LLEGAO4")
            while(xvariable<=x1 and yvariable<=y1):
              TableroJugada[xvariable][yvariable] =2
              yvariable +=1
              xvariable+=1
        case1+=1
        case2+=1
      print("sali del 2 while")
  TableroJugada = BusquedaRellenoDiagonal2(TableroJugada,x,y,jugador)
  return TableroJugada

def BusquedaRellenoDiagonal2(TableroJugada,x,y,jugador):
  print("prueba2")
  lista=[0,0,0,0]
  Dimencion =len(TableroJugada)
  contDiag=0
  case1 =x
  case2 =y
  revisar = 1 
  encontradas1 =0
  encontradas2 =0
  contador=0
  if(jugador ==1): 
    print("Case1:",case1,"case2:",case2)
    if(revisar == 1): #este es  revisar para la diagonal superior izquierda 
      while(case1 >0 and case2 <5):
        print("estoy en el while 1")
        case1 = case1-1
        case2 = case2+1
        print(":::::::::::::::::::::CALCULANDO::::::::::::::::::::::::::",contador)
        print("Case1:",case1,"case2:",case2)
        contador +=1
      print("sali del while")
      print("Case1:",case1,"case2:",case2)
      while(case1 <5 and case2 >0 ):
        print("estoy en el while 2")
        print("estoy antes del primer if: ")
        print("Case1:",case1,"case2:",case2)
        if(TableroJugada[case2][case1] == 1 and encontradas1 <1):
          print("se encontro un 1")
          lista[0] = case1
          lista[1] = case2
          encontradas1 +=1
          print("QUE EH LLEGAO1")
        if(TableroJugada[case2][case1]==1 and encontradas1 <2 ):
          print("se encontro otro 1")
          lista[2] = case1
          lista[3] = case2
          encontradas1 +=1
          print("QUE EH LLEGAO2")
        if (TableroJugada[case2][case1]==1 and encontradas1 >1 ):
          print("se encontro un 1mas !!!!!!!!!")
          lista[2] = case1
          lista[3] = case2
          encontradas1 +=1
          print("QUE EH LLEGAO3")
          if (encontradas1>1):
            xvariable = lista[0]
            yvariable = lista[1]
            x1= lista[2]
            y1= lista[3]
            print("QUE EH LLEGAO4")
            print("Xvariable, Yvariable,x1,y1",xvariable,yvariable,x1,y1)

            while(xvariable<=x1 and yvariable>=y1):
              TableroJugada[yvariable][xvariable] =1
              yvariable= yvariable -1
              xvariable+=1
        case1+=1
        case2=case2-1
      print("sali del 2 while")
  if(jugador ==2): 
    print("Case1:",case1,"case2:",case2)
    if(revisar == 1): #este es  revisar para la diagonal superior izquierda 
      while(case1 >0 and case2 <5):
        print("estoy en el while 1")
        case1 = case1-1
        case2 = case2+1
        print(":::::::::::::::::::::CALCULANDO::::::::::::::::::::::::::",contador)
        print("Case1:",case1,"case2:",case2)
        contador +=1
      print("sali del while")
      print("Case1:",case1,"case2:",case2)
      while(case1 <5 and case2 >0 ):
        print("estoy en el while 2")
        print("estoy antes del primer if: ")
        print("Case1:",case1,"case2:",case2)
        if(TableroJugada[case2][case1] == 2 and encontradas2 <1):
          print("se encontro un 1")
          lista[0] = case1
          lista[1] = case2
          encontradas2 +=1
          print("QUE EH LLEGAO1")
        if(TableroJugada[case2][case1]==2 and encontradas2 <2 ):
          print("se encontro otro 1")
          lista[2] = case1
          lista[3] = case2
          encontradas2 +=1
          print("QUE EH LLEGAO2")
        if (TableroJugada[case2][case1]==2 and encontradas2 >1 ):
          print("se encontro un 1mas !!!!!!!!!")
          lista[2] = case1
          lista[3] = case2
          encontradas2 +=1
          print("QUE EH LLEGAO3")
          if (encontradas2>1):
            xvariable = lista[0]
            yvariable = lista[1]
            x1= lista[2]
            y1= lista[3]
            print("QUE EH LLEGAO4")
            print("Xvariable, Yvariable,x1,y1",xvariable,yvariable,x1,y1)

            while(xvariable<=x1 and yvariable>=y1):
              TableroJugada[yvariable][xvariable] =2
              yvariable= yvariable -1
              xvariable+=1
        case1+=1
        case2=case2-1
      print("sali del 2 while")

  return TableroJugada


def rellenarTablero(TableroJugada,x,y,jugadorMov):
  TableroJugada[x][y] = jugadorMov
  print(jugadorMov)
  TableroJugada = busquedaRellenoColumna(TableroJugada,x,y,jugadorMov)
  return (TableroJugada)

def jugada():
  TableroJugada= Hacertablero()
  while True:
    jugadorMov = 1
    if jugadorMov ==1:
      jugador= input("x y: ")
      (x, y) = jugador.split()
      x = int(x)
      y = int(y)
      print(x,y)
      (TableroJugada) = rellenarTablero(TableroJugada,x,y,jugadorMov)
      imprimirTablero(TableroJugada)
      jugadorMov+=1
    if jugadorMov ==2: #cambiar para implementar la IA
      jugador= input("x y: ")
      (x, y) = jugador.split()
      x = int(x)
      y = int(y)
      (TableroJugada) = rellenarTablero(TableroJugada,x,y,jugadorMov)
      imprimirTablero(TableroJugada)
      jugadorMov-=1
prueba= jugada()


    