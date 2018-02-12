#!/usr/bin/python
from colors import *
import pygame
class Target:
  def __init__(self, x,y):
    self.x = x
    self.y = y
    
  def draw(self, surf):
    r= pygame.Rect((0,0,40,10))
    r.center = (self.x, self.y)
    pygame.draw.rect(surf, BLACK, r)

  def hitBy(self, obj):
    return self.rect.colliderect(obj.getRect())
