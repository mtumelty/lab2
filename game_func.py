#!/usr/bin/python

import pygame,sys
from colors import *

def draw_world(window):
  window.fill(BLUE) #Fills the main Surface where window = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT))
  pygame.draw.rect(window, GREEN, (0,380,500,20)) #Draws Green rectangle on surface
  Title = pygame.font.Font('freesansbold.ttf', 32)
  textSurfaceObj = Title.render('Launchr 1.0', True, BLACK, BLUE)
  textRectObj = textSurfaceObj.get_rect()
  textRectObj.center = (250,30)
  window.blit(textSurfaceObj, textRectObj)











#if (__name__ == "__main__"):
#pygame.init()	
#Surf = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT)) #creates surface
#draw_world(Surf)
