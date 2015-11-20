"""
This class create a player that is able to :
Move
This class needs:
envoirment
"""
import pygame
class Player():
	scereen=pygame.display
	positionX=0
	positionY=0
	sprite =0
	width=0
	height=0
	def __init__(self,positionX,positionY,dimensions,sprite,TFINESTRA_ALTURA):
		self.positionY=positionY
		self.positionX=positionX
		width=dimensions[0]
		height=dimensions[1]
		self.scereen.set_mode(dimensions)
		self.sprite = sprite
		self.TFINESTRA_ALTURA=TFINESTRA_ALTURA
	def move(self,event):
		if event.pos[1] < (self.TFINESTRA_ALTURA-100-self.sprite.get_rect().size[1]/2):
			self.positionX=event.pos[0]-self.sprite.get_rect().size[0]/2
			self.positionY=event.pos[1]-self.sprite.get_rect().size[1]/2
			print "zona 1"+str(self.TFINESTRA_ALTURA)
		else:
			self.positionX=event.pos[0]-self.sprite.get_rect().size[0]/2
			self.positionY=self.TFINESTRA_ALTURA-100-self.sprite.get_rect().size[1]

			print "zona 2"+str(self.TFINESTRA_ALTURA)


		
