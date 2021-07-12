import pygame,sys
from pygame.locals import*
pygame.init()
#Cargar imagen
img = pygame.image.load(".vscode\Pygame\Fondo.jpg")
img=pygame.transform.scale(img,(800,600))
#Colores
black=(0,0,0)
black=(255,255,255)
black=(0,0,255)

#Crear ventana para mostrar
ventana=pygame.display.set_mode((800,600))

#Crear un temporisador para los fps
clock=pygame.time.Clock()
#Fin del juego
game_over=False

#Coordenadas y velocidad del jugaror 1

cordenada_1_x=1
cordenada_1_y=300-90
velocidad_1=0

#Coordenadas y velocidad del jugaror 2

cordenada_2_x=775
cordenada_2_y=300-90
velocidad_2=0

#Coordenadas de la pelota

pelota_x=400
pelota_y=300
velocidad_x=3
velocidad_y=3

#Comienzo del juego
while not game_over:
    #Dar fondo de color
    ventana.blit(img,[0,0])
    #Cierre de ventana
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            game_over=True

        if event.type==pygame.KEYDOWN:
            #Jugador 1
            if event.key==pygame.K_w:
                velocidad_1=-5
            if event.key==pygame.K_s:
                velocidad_1=5
            #Jugador 2
            if event.key==pygame.K_UP:
                velocidad_2=-5
            if event.key==pygame.K_DOWN:
                velocidad_2=5
        if event.type==pygame.KEYUP:
            #Jugador 1
            if event.key==pygame.K_w:
                velocidad_1=0
            if event.key==pygame.K_s:
                velocidad_1=0
            #Jugador 2
            if event.key==pygame.K_UP:
                velocidad_2=0
            if event.key==pygame.K_DOWN:
                velocidad_2=0
     #Definir margenes de jugador
    if cordenada_1_y>=500 or cordenada_1_y<=0:
        velocidad_1*=(-1)
    if cordenada_2_y>500 or cordenada_2_y<0:
        velocidad_2*=(-1)
    #Definir limites de la pelota
    if (pelota_y>590 or pelota_y<10):
        velocidad_y*=-1
    #lado derecho
    if pelota_x>800:
        pelota_x=400
        pelota_y=300
        velocidad_x*=-1
        velocidad_y*=-1
    #Lado izquierdo
    if pelota_x<0:
        pelota_x=400
        pelota_y=300
        velocidad_x*=-1
        velocidad_y*=-1

    #MODIFICA LAS COORDENADAS
    cordenada_1_y+=velocidad_1
    cordenada_2_y+=velocidad_2
    #Movimiento pelota
    pelota_x+=velocidad_x
    pelota_y+=velocidad_y
    #Zona de dibujo
    jugador_1=pygame.draw.rect(ventana,black,(cordenada_1_x,cordenada_1_y,15,90))
    jugador_2=pygame.draw.rect(ventana,black,(cordenada_2_x,cordenada_2_y,15,90))
    pelota=pygame.draw.circle(ventana,black,(pelota_x,pelota_y),10)
    #Detectar colision
    if pelota.colliderect(jugador_1) or pelota.colliderect(jugador_2):
        velocidad_x*=(-1)
    #Actualizar pantalla
    pygame.display.flip()
    #Manejar fps por segundo
    clock.tick(60)

#pygame.quit()