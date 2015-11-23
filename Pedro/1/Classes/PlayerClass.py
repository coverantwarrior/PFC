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
	menu=0
	def __init__(self,positionX,positionY,dimensions,sprite,menu):
		self.positionY=positionY
		self.positionX=positionX
		self.width=dimensions[0]
		self.height=dimensions[1]
		self.scereen.set_mode(dimensions)
		self.sprite = sprite
		self.menu =menu

	def move(self,event):
		if pygame.mouse.get_pos()[0]>self.positionX and pygame.mouse.get_pos()[0]< self.positionX + self.width and pygame.mouse.get_pos()[1]>self.positionY and pygame.mouse.get_pos()[1] < self.positionY+self.height:
			if event.pos[0] > self.sprite.get_rect().size[0] / 2 and event.pos[0] < self.width-self.menu[0] - self.sprite.get_rect().size[0] / 2 :
				self.positionX = event.pos[0] - self.sprite.get_rect().size[0] / 2
			if event.pos[1] > self.sprite.get_rect().size[1] / 2 and event.pos[1] < self.height-self.menu[1] - self.sprite.get_rect().size[1] / 2 :
				self.positionY = event.pos[1] - self.sprite.get_rect().size[1] / 2


		#if event.pos[1] < (self.TFINESTRA_ALTURA-100-self.sprite.get_rect().size[1]/2):
		#	self.positionX=event.pos[0]-self.sprite.get_rect().size[0]/2
		#	self.positionY=event.pos[1]-self.sprite.get_rect().size[1]/2
		#	print "zona 1"+str(self.TFINESTRA_ALTURA)
		#else:
		#	self.positionX=event.pos[0]-self.sprite.get_rect().size[0]/2
		#	self.positionY=self.TFINESTRA_ALTURA-100-self.sprite.get_rect().size[1]

		#	print "zona 2"+str(self.TFINESTRA_ALTURA)


		
