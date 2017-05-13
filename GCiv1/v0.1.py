#!/usr/bin/env python

#chemin des images
background_image_filename = 'background/paris_carte_wow.jpg'
sprite_image_filename = 'Sprites/Indiana.png'
goal_image_filename = 'Sprites/pommier.png'
win_image_filename = 'image/win.jpg'

#librairie
import pygame
from pygame.locals import *
from sys import exit
from gameobjects.vector2 import Vector2

#initialisation
pygame.init()

#fenetre
screen = pygame.display.set_mode((1000, 665),0,32)
pygame.display.set_caption("Gciv1")

#chargement des images
background = pygame.image.load(background_image_filename).convert()
sprite = pygame.image.load(sprite_image_filename).convert_alpha()
goal = pygame.image.load(goal_image_filename).convert_alpha()
win = pygame.image.load(win_image_filename).convert()

#
clock = pygame.time.Clock()

#prosition Héros
sprite_pos = Vector2(200, 150)
sprite_speed = 300.

#position Arbre
goal_pos = Vector2(700, 330)

#boucle
while True:

    #
    for event in pygame.event.get():
        #fin si le joueur quitte la fenetre
        if event.type == QUIT :
            exit()
        #fin si le joueur arrive dans la zone de l'arbre
        if (goal_pos.x-30 < sprite_pos.x < goal_pos.x+30 and goal_pos.y-30 < sprite_pos.y < goal_pos.y+30 ):
            #afficher l'écran de fin
            screen.blit(win,(200,150))
            #rafraichir la fenetre pour afficher l'image de fin
            pygame.display.flip()
            #delai affichage et jeu en pause
            pygame.time.wait(2000)
            exit()

    #mouvement Héros
    pressed_keys = pygame.key.get_pressed()

    key_direction = Vector2(0, 0)
    if pressed_keys[K_LEFT]:
        key_direction.x = -1
    elif pressed_keys[K_RIGHT]:
        key_direction.x = +1
    if pressed_keys[K_UP]:
        key_direction.y = -1
    elif pressed_keys[K_DOWN]:
        key_direction.y = +1

    key_direction.normalize()

    screen.blit(background, (0, 0))
    screen.blit(sprite, sprite_pos)
    screen.blit(goal, goal_pos)

    time_passed = clock.tick(30)
    time_passed_seconds = time_passed / 1000.0

    #déplacement Héros
    sprite_pos += key_direction * sprite_speed * time_passed_seconds

    pygame.display.update()