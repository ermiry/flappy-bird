import os
import pygame

from base import Base, load_base
from bird import Bird
from pipe import Pipe, load_pipe

WIN_WIDTH = 600
WIN_HEIGHT = 800

WIN = pygame.display.set_mode ((WIN_WIDTH, WIN_HEIGHT))
pygame.display.set_caption ("Flappy Bird")

pygame.font.init ()
STAT_FONT = pygame.font.SysFont ("comicsans", 48)
END_FONT = pygame.font.SysFont ("comicsans", 72)

bg_img = pygame.transform.scale (pygame.image.load (os.path.join ("assets", "bg.png")).convert_alpha (), (600, 900))

load_base ()
load_pipe ()

def draw(win, bird, pipes, base, score):
	win.blit (bg_img, (0, 0))

	for p in pipes:
		p.draw (win)

	base.draw (win)

	bird.draw (win)

	text = STAT_FONT.render ("Score: " + str (score), 1, (255, 255, 255))
	win.blit (text, (WIN_WIDTH - 10 - text.get_width (), 10))

	pygame.display.update ()

def main():
	clock = pygame.time.Clock ()

	base = Base (730)
	bird = Bird (230, 350)
	pipes = [Pipe (WIN_WIDTH)]

	score = 0

	run = True
	while run:
		clock.tick(30)
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				run = False
		
		# bird.move ()
		base.move ()

		rem = []
		add_pipe = False
		for p in pipes:
			if p.collide (bird):
				pass
			
			if p.x + p.PIPE_TOP.get_width () < 0:
				rem.append (p)

			if not p.passed and p.x < bird.x:
				p.passed = True
				add_pipe = True

			p.move ()

		if add_pipe:
			score += 1
			pipes.append (Pipe (WIN_WIDTH))

		for r in rem:
			pipes.remove (r)

		# check if the bird hit the floor
		if bird.y + bird.img.get_height () >= 730:
			pass

		draw (WIN, bird, pipes, base, score)

	pygame.quit()
	quit ()

main ()