#!/usr/bin/python

import pygame, sys
from colors import *
from pygame.locals import * #needed for QUIT function to work



import launcher
import rock
import game_func

def main():
	pygame.init()
	fpsClock = pygame.time.Clock()



while(True):
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

