import sys, pygame

#inicializo pygame
pygame.init()

#Muestro una ventana de 800x600
size = 800, 600
screen = pygame.display.set_mode(size)

#Titulo de la ventana
pygame.display.set_caption("Juego de la pelotita")

#inicializo variables
width, height = 800, 600
speed = [1,1]
white = 255, 255, 255

#Crea un objeto imagen y obtengo su rectangulo
ball = pygame.image.load("ball.jpg")
ball_rect = ball.get_rect()

#Comienza el bucle del juego
run = True

while run:
	#Espero un tiempo (milisegundos) para que la pelota no vaya muy rápido
	pygame.time.delay(2)
	#Capturo los eventos que se han producido
	for event in pygame.event.get():
		#Si el evento es salir de la ventana, se termina el juego.
		if event.type == pygame.QUIT:
			run = False

	#Muevo la pelotita
	ball_rect = ball_rect.move(speed)

	#Compruebo si la pelotita llega a los limites de la ventana
	if ball_rect.left < 0 or ball_rect.right > width:
		speed[0] = -speed[0]

	if ball_rect.top < 0 or ball_rect.bottom > height:
		speed[1] = -speed[1]

	#Pinto el fondo de blanco, dibulo la pelota y actualizo la pantalla
	screen.fill(white)
	screen.blit(ball, ball_rect)
	pygame.display.flip()

#Salgo de pygame
pygame.quit()