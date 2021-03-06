#!/usr/bin/env python
# coding=utf-8
""" 
 Mostramos como usar un sprite respaldado por un grafico.
  
 Sample Python/Pygame Programs
 Simpson College Computer Science
 http://programarcadegames.com/
 http://simpson.edu/computer-science/
 
 Video explicativo: http://youtu.be/vRB_983kUMc
"""
 
import pygame , numpy
from Classes.PlayerClass import *
from Classes.colors import*

pygame.init()

# Establecemos las dimensiones de la pantalla [largo,altura]
TFINESTRA_LATERAL=800
TFINESTRA_ALTURA=600
dimensiones = (TFINESTRA_LATERAL,TFINESTRA_ALTURA)
pantalla = pygame.display.set_mode((dimensiones),pygame.HWSURFACE|pygame.DOUBLEBUF|pygame.RESIZABLE) 
pygame.display.set_caption("Demigame v0.01")

# Definimos algunos colores


#image = pygame.image.load("./data/images/roto2.gif").convert()
menu = pygame.image.load("./data/images/menu.bmp").convert()
fondo = pygame.image.load("./data/images/fondo.jpg").convert()
#El bucle se ejecuta hasta que el usuario hace click sobre el botón de cierre.
 
hecho = False
 
  
# Se usa para establecer cuan rápido se actualiza la pantalla
menu_dimensions=(0,100)
reloj = pygame.time.Clock()
click_apretat=False
# Creació del objecte
roto2 = Player(100,100,dimensiones,pygame.image.load("./data/images/roto2.gif").convert(),menu_dimensions)
#roto3 = Player(500,50,dimensiones,pygame.image.load("./data/images/roto2.gif").convert(),menu_dimensions)
  
# -------- Bucle principal del Programa -----------
while not hecho:
    # --- Bucle principal de eventos
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT: 
            hecho = True
        elif evento.type == pygame.MOUSEBUTTONDOWN: 
            click_apretat = True
            roto2.move(evento)
            #roto3.move(evento)
        elif evento.type == pygame.MOUSEBUTTONUP:
            click_apretat = False
        elif click_apretat & (evento.type == pygame.MOUSEMOTION):
            roto2.move(evento)
            #roto3.move(evento)
            

     
    # --- LA LÓGICA DEL JUEGO DEBERÍA IR AQUÍ

    # --- EL CÓDIGO DE DIBUJO DEBERÍA IR AQUÍ
     
    # Primero, limpia la pantalla con blanco. No vayas a poner otros comandos de dibujo encima 
    # de esto, de otra forma serán borrados por este comando:
    #pantalla.fill(BLANCO)
    pantalla.blit(fondo,[0,0])
    pantalla.blit(menu,(0,dimensiones[1]-100))
    pantalla.blit(roto2.sprite, (roto2.positionX,roto2.positionY))
    #pantalla.blit(roto3.sprite, (roto3.positionX,roto3.positionY))
    print str(pygame.mouse.get_pos())+"/"+str(roto2.positionX)+"-"+str(roto2.positionY)




     
    # --- Avanzamos y actualizamos la pantalla con lo que hemos dibujado.
    pygame.display.flip()
    # --- Limitamos a 60 fotogramas por segundo (frames per second)
    reloj.tick(60)

# Cerramos la ventana y salimos.
# Si te olvidas de esta última línea, el programa se 'colgará'
# al salir si lo hemos estado ejecutando desde el IDLE.
pygame.quit()
quit()