#!/usr/bin/python

import math
import pygame
from colors import *
MAX_MAG = 100
MIN_MAG = 10
MAX_ANGLE = 90
MIN_ANGLE = 0

class Launcher:
	def __init__(self, x, y):
		self.x = x
		self.y = y
		self.magnitude = 30
		self.angle = 45
		
	def changeMagnitude(self, delta):
		self.magnitude += delta
		if self.magnitude > MAX_MAG:
			self.magnitude = MAX_MAG
		if self.magnitude < MIN_MAG:
			self.magnitude = MIN_MAG
			
	def changeAngle(self, delta):
		self.angle += delta
		if self.angle > MAX_ANGLE:
			self.angle = MAX_ANGLE
		if self.angle < MIN_ANGLE:
			self.angle = MIN_ANGLE
			
	def fire(self, rock):
		rock.v_x = self.magnitude*math.cos(self.angle*math.pi/180)
		rock.v_y = self.magnitude*math.sin(self.angle*math.pi/180)
		
	def draw(self, surf):
		dx = self.magnitude * math.cos(self.angle*(math.pi/180))
		dy = self.magnitude * math.sin(self.angle*(math.pi/180))
	
		pygame.draw.line(surf, RED, (self.x, self.y), (self.x+dx,self.y-dy), 3)
		
