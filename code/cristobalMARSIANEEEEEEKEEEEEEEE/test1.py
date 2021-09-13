import numpy as np
def Hacertablero():
    board = [[0 for x in range(6)] for x in range(6)]
    board[2][2]=2
    board[2][3]=1
    board[3][2]=1
    board[3][3]=2
    return board



def busquedaRelleno(TableroJugada,x,y,jugador):
  lista=[0,0,0,0]
  Dimencion =len(TableroJugada)
  salir=0
  contFila = 0
  contCol=0
  contDiag1=0
  conDiag2=0
  encontradas=0
  constante = y
  for i in range(6):
    if(TableroJugada[i][constante]==1 and encontradas ==0):
        print("Se encontro un 1: en la pocicion ",i,constante,"el valor encontrado",TableroJugada[i][constante])
        lista[0] = contFila
        lista[1] = y
        encontradas +=1


    '''if(TableroJugada[contFila][y]==1 and encontradas !=0):
        lista[2] = contFila
        lista[3] = y
        encontradas +=1
    contFila+=1
    salir+=1
    if (encontradas>1):
        x = lista[0]
        y = lista[1]
        x1= lista[2]
        y1= lista[3]
        lista =[0,0,0,0]
    else:
        break'''

  
def rellenarTablero(TableroJugada,x,y,jugadorMov):
  TableroJugada[x][y] = jugadorMov
  print(TableroJugada)
  TableroJugada = busquedaRelleno(TableroJugada,x,y,jugadorMov)
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
      print(TableroJugada)
      jugadorMov+=1
    if jugadorMov ==2: #cambiar para implementar la IA
      jugador= input("x y: ")
      (x, y) = jugador.split()
      x = int(x)
      y = int(y)
      (TableroJugada) = rellenarTablero(TableroJugada,x,y,jugadorMov)
      print(TableroJugada)
      jugadorMov-=1

prueba= jugada()