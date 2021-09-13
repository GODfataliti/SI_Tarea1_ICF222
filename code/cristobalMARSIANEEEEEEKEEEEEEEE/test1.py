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
  return TableroJugada

def rellenarTablero(TableroJugada,x,y,jugadorMov):
  TableroJugada[x][y] = jugadorMov
  print(jugadorMov)
  imprimirTablero(TableroJugada)
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


    