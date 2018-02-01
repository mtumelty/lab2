#!/usr/bin/python

import math
import pygame

MAX_MAG = 100
MIN_MAG = 10
MAX_ANGLE = 90
MIN_ANGLE = 0

def class Launcher:
	def __init__(self, x, y):
		self.x = 0
		self.y = 0
		self.magnitude = 30
		self.angle = 45
		
	def changeMagnitude(self, delta):
		self.magnitude += delta
		if self.magnitude > 100:
			self.magnitude = 100
		if self.magnitude <10:
			self.magnitude = 10
			
	def changeAngle(self, delta):
		self.angle += delta
		if self.angle >90:
			self.angle = 90
		if self.angle <0:
			self.angle = 0
			
	def draw(self, surf):
		#need to do the math
		pygame.draw.line(surf, color, start pos, stop pos, 5)
		
