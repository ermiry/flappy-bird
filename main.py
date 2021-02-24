import os
import pygame

from bird import Bird
from pipe import Pipe

WIN_WIDTH = 600
WIN_HEIGHT = 800

WIN = pygame.display.set_mode ((WIN_WIDTH, WIN_HEIGHT))
pygame.display.set_caption ("Flappy Bird")

bg_img = pygame.transform.scale (pygame.image.load (os.path.join ("assets", "bg.png")).convert_alpha (), (600, 900))

def draw(win, bird, pipes, base):
	win.blit (bg_img, (0, 0))

	for p in pipes:
		p.draw (win)

	base.draw (win)

	bird.draw (win)

	pygame.display.update ()

def main():
	clock = pygame.time.Clock ()
	win = pygame.display.set_mode ((WIN_WIDTH, WIN_HEIGHT))

	bird = Bird (230, 350)

	run = True
	while run:
		clock.tick(30)
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				run = False
		
		bird.move ()

		draw (win, bird)

	pygame.quit()
	quit ()

main ()