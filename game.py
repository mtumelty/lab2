#!/usr/bin/python
import random 
import pygame
from colors import *
from pygame.locals import * #needed for QUIT function to work
from game_func import *

#object modules
import launcher
import rock
import target

pygame.init()
fpsClock = pygame.time.Clock()
window = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT))
my_launcher = launcher.Launcher(0, WINDOWHEIGHT-20)
my_rock = rock.Rock(0, WINDOWHEIGHT-20)
#my_target = target.Target((random.random()*280)+100, WINDOWHEIGHT-20)
my_target = target.Target(150, WINDOWHEIGHT-20)
FIRED = False

#and ((my_target.y+5)<my_rock.y and my_rock.y < (my_target.y-5) )
def isHit():
	if (((my_target.x-20)<my_rock.x and my_rock.x < (my_target.x+20)) and ((my_target.y-5)>my_rock.y and my_rock.y < (my_target.y+5) ) ):
		return True
	else:
		return False
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
				FIRED = True

		if event.type == QUIT:
			pygame.quit()
			sys.exit()
			
	#Game Logic
	if FIRED and (my_rock.y<400):
		my_rock.move(1.0/FPS)
	if isHit():
		my_rock.moveTo(0, WINDOWHEIGHT-20)
		print "Hit Target"
	elif my_rock.y>(WINDOWHEIGHT-10):
		my_rock.moveTo(0, WINDOWHEIGHT-20)
		print "You missed loser"
	
			
	#draw onto the window
		
	draw_world(window)
	my_launcher.draw(window)
	my_rock.draw(window)
	my_target.draw(window)
	pygame.display.update()
	fpsClock.tick(FPS)

