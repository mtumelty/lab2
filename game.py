#!/usr/bin/python

import serial
import pygame
from pygame.locals import * #needed for QUIT function to work
import sys


while(True):
	draw_wold(window)

	for event in pygame.event.get():
		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_UP:
				my_launcher.changeAngle(3)
			#TODO: handle rest of direction changes

		if event.type == QUIT:
			pygame.quit()
			sys.exit()

	my_launcher.draw(window)
	pygame.display.update()
	fpsClock.tick(FPS)

