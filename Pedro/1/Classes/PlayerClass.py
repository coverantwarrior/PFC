"""
This class create a player that is able to :
Move
This class needs:
envoirment
"""
import pygame, numpy
class Player():
	scereen=pygame.display
	positionX=0
	positionY=0
	sprite =0
	width=0
	height=0
	def __init__(self,positionX,positionY,dimensions,sprite):
		self.positionY=positionY
		self.positionX=positionX
		width=dimensions[0]
		height=dimensions[1]
		self.scereen.set_mode(dimensions)
		self.sprite = sprite
	def move(self,event):
		if event.pos[1] < (height-100-image.get_rect().size[1]/2):
			self.positionX=event.pos[0]-image.get_rect().size[0]/2
			self.positionY=event.pos[1]-image.get_rect().size[1]/2
		else:
			self.positionX=event.pos[0]-image.get_rect().size[0]/2
			self.positionY=width-100-image.get_rect().size[1]
