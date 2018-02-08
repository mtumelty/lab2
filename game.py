#!/usr/bin/python

import pygame
from colors import *
from pygame.locals import * #needed for QUIT function to work
from game_func import *


import launcher
import rock


pygame.init()
fpsClock = pygame.time.Clock()
window = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT))
my_launcher = launcher.Launcher(0, WINDOWHEIGHT-20)
my_rock = rock.Rock(0, WINDOWHEIGHT-20)

while True:
	draw_world(window)
	
	#Keyboard Read
	for event in pygame.event.get():
		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_UP:
				my_launcher.changeAngle(3)
			if event.key == pygame.K_DOWN:
				my_launcher.changeAngle(-3)
			if event.key == pygame.K_RIGHT:
				my_launcher.changeMagnitude(5)
			if event.key == pygame.K_LEFT:
				my_launcher.changeMagnitude(-5)
			if (event.key == pygame.K_SPACE) and (not my_rock.isMoving()):
				my_launcher.fire(my_rock)
				print('FIRE matey!!')
				

		if event.type == QUIT:
			pygame.quit()
			sys.exit()
			
	#Game Logic
	my_rock.move(1.0/FPS)		
			
	#draw onto the window		
	draw_world(window)
	my_launcher.draw(window)
	my_rock.draw(window)
	pygame.display.update()
	fpsClock.tick(FPS)

