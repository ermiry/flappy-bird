import os
import pygame

from bird import Bird

WIN_WIDTH = 600
WIN_HEIGHT = 800

WIN = pygame.display.set_mode ((WIN_WIDTH, WIN_HEIGHT))
pygame.display.set_caption ("Flappy Bird")

pipe_img = pygame.transform.scale2x (pygame.image.load (os.path.join ("assets", "pipe.png")).convert_alpha ())
bg_img = pygame.transform.scale (pygame.image.load (os.path.join ("assets", "bg.png")).convert_alpha (), (600, 900))
base_img = pygame.transform.scale2x (pygame.image.load (os.path.join ("assets", "base.png")).convert_alpha ())

def draw(win, bird):
	win.blit (bg_img, (0, 0))
	bird.draw (win)
	pygame.display.update ()

def main():
	clock = pygame.time.Clock ()
	win = pygame.display.set_mode ((WIN_WIDTH, WIN_HEIGHT))

	bird = Bird (200, 200)

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