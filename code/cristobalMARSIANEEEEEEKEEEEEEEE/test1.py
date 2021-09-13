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

def busquedaRelleno(TableroJugada,x,y,jugador):
  lista=[0,0,0,0]
  Dimencion =len(TableroJugada)
  contFila = 0
  contCol=0
  contDiag1=0
  conDiag2=0
  constante = y
  encontradas1=0
  encontradas2=0
  print("_______________________________-----------------------------------------_________________________")
  if(jugador == 1):
    for i in range(Dimencion):
      print("valor encontrado: ",TableroJugada[i][constante])
      print("posicion revisada: ",i,constante)
      print("IMPORTANTE IMPORTANTE IMPORTANTE 1 ENCONTRADOS: CANTIDADA:", encontradas1)
      if(TableroJugada[i][constante]==1 and encontradas1 <1):
        print("Se encontro un 1: en la pocicion ",i,constante,"el valor encontrado",TableroJugada[i][constante])
        lista[0] = i
        lista[1] = constante
        encontradas1 +=1
        print("esta es la lista: ",lista)
      if(TableroJugada[i][constante]==1 and encontradas1 <2 and (TableroJugada[i-1][constante]!=0)):
        lista[2] = i
        lista[3] = constante
        encontradas1 +=1
        contFila+=1
      if(TableroJugada[i][constante]==1 and encontradas1 >1 and (TableroJugada[i-1][constante]!=0)):
        print("no encontre ningun 0 en medio ")
        lista[2] = i
        lista[3] = constante
        encontradas1 +=1
        contFila+=1
        print("esta es la lista cuando encuentra dos 1 :",lista)
        if (encontradas1>1):
          print("LLegue hasta aqui")
          xvariable = lista[0]
          y = lista[1]
          x1= lista[2]
          y1= lista[3]
          print("posiciones a rellenar: x1 y1 x2 y2",xvariable,y,x1,y1)
          
          while(xvariable <= x1):
            print("Estoy realizando el for de llenado")
            TableroJugada[xvariable][y1] = 1
            xvariable +=1
            print("EH LLENADO UNA CASILLA CON EL VALOR CORRESPONDIENTE :) ")
    lista =[0,0,0,0]
    print("_______________________________-----------------------------------------_________________________")  
  if (jugador == 2):
    for i in range(Dimencion):            
      print("valor encontrado: ",TableroJugada[i][constante])
      print("posicion revisada: ",i,constante)
      print("IMPORTANTE IMPORTANTE IMPORTANTE 2 ENCONTRADOS: CANTIDADA:", encontradas1)
      if(TableroJugada[i][constante]==2 and encontradas2 <1):
        print("Se encontro un 2: en la pocicion ",i,constante,"el valor encontrado",TableroJugada[i][constante])
        lista[0] = i
        lista[1] = constante
        encontradas2 +=1
        print("esta es la lista: ",lista)
      if(TableroJugada[i][constante]==2 and encontradas2 <2 and (TableroJugada[i-1][constante]!=0)):
        lista[2] = i
        lista[3] = constante
        encontradas2 +=1
        contFila+=1
      if(TableroJugada[i][constante]==2 and encontradas2 >1 and (TableroJugada[i-1][constante]!=0)):
        print("no encontre ningun 0 en medio ")
        lista[2] = i
        lista[3] = constante
        encontradas2 +=1
        contFila+=1
        print("esta es la lista cuando encuentra dos 2 :",lista)
        if (encontradas2>1):
          print("LLegue hasta aqui")
          xvariable = lista[0]
          y = lista[1]
          x1= lista[2]
          y1= lista[3]
          print("posiciones a rellenar: x1 y1 x2 y2",xvariable,y,x1,y1)
          
          while(xvariable <= x1):
            print("Estoy realizando el for de llenado")
            TableroJugada[xvariable][y1] = 2
            xvariable +=1
            print("EH LLENADO UNA CASILLA CON EL VALOR CORRESPONDIENTE :) ")
    lista =[0,0,0,0]
    print("_______________________________-----------------------------------------_________________________")


  return TableroJugada

  
def rellenarTablero(TableroJugada,x,y,jugadorMov):
  TableroJugada[x][y] = jugadorMov
  print(jugadorMov)
  imprimirTablero(TableroJugada)
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


    