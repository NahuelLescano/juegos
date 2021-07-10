import sys, pygame

#Inicializo pygame
pygame.init()

#Muestro una ventana de 800x600
size = 800, 600
screen = pygame.display.set_mode(size)

#Titulo del juego
pygame.display.set_caption("Juego de la pelotita v2.0")

#Inicializo variables
width, height = 800, 600
speed = [1, 1]
white = 255, 255, 255

#Crea un objeto imagen pelota y obtengo su rectángulo
ball = pygame.image.load("ball2.jpg")
ball_rect = ball.get_rect()

#Crea un objeto imagen bate y obtengo su rectángulo
bate = pygame.image.load("bate2.jpg")
bate_rect = bate.get_rect()

#Pongo el bate en el medio de la pantalla
bate_rect.move_ip(400, 300)

#Comienza el bucle del juego
run = True
while run:
	#Espero un tiempo (milisegundos) para que la pelota no se mueva tan rápido
	pygame.time.delay(2)
	#Capturo los eventos que se han producido
	for event in pygame.event.get():
		#Si el evento es salir de la ventana, se termina el juego
		if event.type == pygame.QUIT:
			run = False

		#Compruebo si se ha pulsado alguna tecla
		keys = pygame.key.get_pressed()
		if keys[pygame.K_UP]:
			bate_rect = bate_rect.move(0, -1)
		if keys[pygame.K_DOWN]:
			bate_rect = bate_rect.move(0, 1)

		#Compruebo si hubo alguna colisión
		if bate_rect.colliderect(ball_rect):
			speed[0] = -speed[0]

		#Muevo la pelotita
		ball_rect = bate_rect.move(speed)

		#Compruebo si la pelota llega a los límites de la ventana
		if ball_rect.left < 0 or ball_rect.right > width:
			speed[0] = -speed[0]
		if ball_rect.top < 0 or ball_rect.bottom > height:
			speed[1] = -speed[1]

		#Pinto el fondo de blancom, dibujo la pelota y actualizo la pantalla
		screen.fill(white)
		screen.blit(ball, ball_rect)
		#Dibujo el bate
		screen.blit(bate, ball_rect)
		pygame.display.flip()

#Salgo de pygame
pygame.quit()