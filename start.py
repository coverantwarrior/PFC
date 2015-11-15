#!/usr/bin/env python
# -*- coding: utf-8 -*-
try:
    import pygame, numpy
except ImportError, message:
    raise SystemExit,  "Unable to load module. %s" % message

def update_pos(event):
    if event.pos[1] < (TFINESTRA_ALTURA-100-image.get_rect().size[1]/2):
        posX=event.pos[0]-image.get_rect().size[0]/2
        posY=event.pos[1]-image.get_rect().size[1]/2
    else:
        posX=event.pos[0]-image.get_rect().size[0]/2
        posY=TFINESTRA_ALTURA-100-image.get_rect().size[1]
    return posX,posY
    
def grayscale(img):
    arr = pygame.surfarray.array3d(img)
    #luminosity filter
    avgs = [[(r*0.298 + g*0.587 + b*0.114) for (r,g,b) in col] for col in arr]
    arr = numpy.array([[[avg,avg,avg] for avg in col] for col in avgs])
    return pygame.surfarray.make_surface(arr)

pygame.init()
fuente = pygame.font.Font('freesansbold.ttf', 16)

TFINESTRA_LATERAL=800
TFINESTRA_ALTURA=600
screen = pygame.display.set_mode((TFINESTRA_LATERAL, TFINESTRA_ALTURA))

pygame.display.set_caption("Demigrant Game")
pygame.mouse.set_cursor(*pygame.cursors.diamond)

clock = pygame.time.Clock()
 
BLACK = (  0,   0,   0)
WHITE = (255, 255, 255)
BLUE =  (  0,   0, 255)
GREEN = (  0, 255,   0)
RED =   (255,   0,   0)
image = pygame.image.load("./data/images/roto2.gif").convert()
menu = pygame.image.load("./data/images/menu.bmp").convert()
fondo = pygame.image.load("./data/images/fondo.jpg").convert()

x=0
y=0

click_apretat = False
done = False
while not done:
    clock.tick(60)
#events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done=True
        elif event.type == pygame.MOUSEBUTTONDOWN:
            click_apretat = True
            x,y=update_pos(event)

        elif event.type == pygame.MOUSEBUTTONUP:
            click_apretat = False
        elif click_apretat & (event.type == pygame.MOUSEMOTION):
            x,y=update_pos(event)

#Comença el programa
    #pygame.display.set_caption("fps: " + str(clock.get_fps()))

    screen.blit(fondo,[0,0])
    #pygame.draw.rect(screen, BLACK, [75, 10, 50, 20], 2)
    screen.blit(menu,(0,TFINESTRA_ALTURA-100))
    screen.blit(image, (x, y))

         
    texto = fuente.render("x: " + str(x)+" y: "+str(y), True, BLACK)
    screen.blit(texto, [10, TFINESTRA_ALTURA-50])

    fps = fuente.render("FPS: " + str(clock.get_fps()), True, BLACK)
    screen.blit(fps, [10, 10])

    

    pygame.display.flip()



pygame.quit()
quit()