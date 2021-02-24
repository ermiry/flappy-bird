import os
import pygame

base_img = None

def load_base ():
	global base_img
	base_img = pygame.transform.scale2x (pygame.image.load (os.path.join ("assets", "base.png")).convert_alpha ())

class Base:
	VEL = 5
	
	def __init__(self, y):
		self.x1 = 0
		self.WIDTH = base_img.get_width()
		self.x2 = self.WIDTH
		self.y = y

		self.IMG = base_img

	def move(self):
		self.x1 -= self.VEL
		self.x2 -= self.VEL
		if self.x1 + self.WIDTH < 0:
			self.x1 = self.x2 + self.WIDTH

		if self.x2 + self.WIDTH < 0:
			self.x2 = self.x1 + self.WIDTH

	def draw(self, win):
		win.blit(self.IMG, (self.x1, self.y))
		win.blit(self.IMG, (self.x2, self.y))