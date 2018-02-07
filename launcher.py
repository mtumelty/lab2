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
		rock.v_x = self.magnitude*np.cos(self.angle*np.pi/180)
		rock.v_y = self.magnitude*np.sin(self.angle*np.pi/180)
		
	def draw(self, surf):
		dx = self.magnitude*np.cos(self.angle*np.pi/180)
		dy = self.magnitude*np.sin(self.angle*np.pi/180)
		#not sure what 'np' is
		pygame.draw.line(surf, color, dx, dy, 5)
		
