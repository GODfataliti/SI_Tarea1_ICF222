import pygame

BACKGROUND = (25, 210, 150)
size = (560,630)
screen = pygame.display.set_mode(size)
title = "REVERSI"
pygame.display.set_caption(title)

#DIMENSIONES DEL TABLERO 70X70 POR CASILLA, POR LO QUE LA RESOLUCION DE LA PANTALLA DEBE SER MULTIPLO DE ESTE VALOR.


pygame.init()

ficha_negra = pygame.image.load(r'D:\Universidad\Programacion\Sistemas_Inteligentes\Tareas\01\SI_Tarea1_ICF222\src\img\ficha_negra.png')
ficha_blanca = pygame.image.load(r'D:\Universidad\Programacion\Sistemas_Inteligentes\Tareas\01\SI_Tarea1_ICF222\src\img\ficha_blanca.png')

img_grid = pygame.image.load(r'D:\Universidad\Programacion\Sistemas_Inteligentes\Tareas\01\SI_Tarea1_ICF222\src\img\Grid.png')
image_grid = pygame.transform.scale(img_grid, [420,420])
img_puntaje = pygame.image.load(r'D:\Universidad\Programacion\Sistemas_Inteligentes\Tareas\01\SI_Tarea1_ICF222\src\img\Puntaje.png')
img_titulo = pygame.image.load(r'D:\Universidad\Programacion\Sistemas_Inteligentes\Tareas\01\SI_Tarea1_ICF222\src\img\REVERSI.png')

coord_list = []

while True:
    screen.fill(BACKGROUND)
    screen.blit(image_grid, [70,160])
    screen.blit(img_puntaje, [70,90])
    screen.blit(img_titulo, [190,10])
    for event in pygame.event.get():
        #print(event)
        if event.type == pygame.QUIT:
            sys.exit()
      
        elif event.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            #print(pos)
            select_x = (pos[0] // 70)
            select_y = (pos[1] // 70)
            print(f' {select_x} , {select_y} ')
            coord_list.append([select_x,select_y])
        

        for value in coord_list:
            screen.blit(ficha_blanca,[value[0],value[1]])
    

    pygame.display.flip()

