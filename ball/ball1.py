#Version 1.0
import sys, pygame

#inicializa pygame
pygame.init()

#tamaño de la ventana
size = 800, 600
pygame.display.set_mode(size)

#titulo del juego
pygame.display.set_caption("ola ke ace")

#comienza el bucle del juego
run = True

while run:
	#captura los eventos que se producen, en este caso uno solo.
	for event in pygame.event.get():
		#si el evento es salir de la ventana, se termina el juego. 
		if event.type == pygame.QUIT:
			run = False

#Sale de pygame.
pygame.quit()