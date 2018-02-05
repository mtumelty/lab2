#!/usr/bin/python

import pygame,sys

WINDOWWIDTH = 500
WINDOWHEIGHT = 400
BLUE = (0,0,255)
GREEN =(0,255,0)
BLACK = (0,0,0)
def draw_world(Surf):
  Surf.fill(BLUE) #Fills the main Surface where Surf = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT))
  pygame.draw.rect(Surf, GREEN, (0,380,500,20)) #Draws Green rectangle on surface
  Title = pygame.font.Font('freesansbold.ttf', 32)
  textSurfaceObj = Title.render('Launchr 1.0', True, BLACK, BLUE)
  textRectObj = textSurfaceObj.get_rect()
  textRectObj.center = (250,30)
  Surf.blit(textSurfaceObj, textRectObj)











#if (__name__ == "__main__"):
#pygame.init()	
#Surf = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT)) #creates surface
#draw_world(Surf)
