#!/usr/bin/env python
# -*- coding: UTF-8 -*-
#background_image_filename = 'sushiplate.jpg'
#mouse_image_filename = 'fugu.png'
background_image_filename = 'jpg\\295541.jpg'
mouse_image_filename = "glyph-icons\\locate.png"
# 指定图像文件名称

import pygame
from pygame.locals import *
from sys import exit

pygame.init()
screen = pygame.display.set_mode((1366,768), RESIZABLE, 32)
pygame.display.set_caption("Hello, World!")

background = pygame.image.load(background_image_filename).convert()
mouse_cursor = pygame.image.load(mouse_image_filename).convert_alpha()

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            exit()
    screen.blit(background, (0,0))
    x,y = pygame.mouse.get_pos()
    x-=mouse_cursor.get_width()/2
    y-=mouse_cursor.get_height()/2
    screen.blit(mouse_cursor, (x,y))

    pygame.display.update()