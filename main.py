#!/usr/bin/python

import os
import sys
import csv

import pygame
import random
import math
from time import sleep

from gresource import *
from map import *
from map_data import *

TITLE_STR = 'Map Search Algorithm'

SCREEN_WIDTH = 640
SCREEN_HEIGHT = 480

def draw_step(count) :
    font = pygame.font.SysFont(None, 25)
    text = font.render("Step : " + str(count), True, COLOR_WHITE)
    gctrl.surface.blit(text, (gctrl.width - 100, 0))

def draw_message(str) :
    gctrl.draw_string(str, 0, 0, ALIGN_CENTER, 40, COLOR_BLACK)

    pygame.display.update()
    sleep(2)

def terminate() :
    pygame.quit()
    sys.exit()

def start() :
    # Clear gamepad
    gctrl.surface.fill(COLOR_WHITE)

    gctrl.draw_string(TITLE_STR, 0, 0, ALIGN_CENTER, 40, COLOR_BLACK)

    help_str = ['d : Dijkstra',
                'a : A-star',
                'b : BFS',
                'c : DFS',
                'x : exit']

    for i, help in enumerate(help_str) :
        y_offset = 150 - i * 30
        gctrl.draw_string(help, 0, y_offset, ALIGN_CENTER | ALIGN_BOTTOM, 30, COLOR_BLUE)

    while True :
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminate()
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_ESCAPE:
                    terminate()
                elif event.key == pygame.K_d :
                    return 'Dijkstra'
                elif event.key == pygame.K_a :
                    return 'A-starx'
                elif event.key == pygame.K_b :
                    return 'BFS'
                elif event.key == pygame.K_c :
                    return 'DFS'
                elif event.key == pygame.K_x :
                    terminate()

        pygame.display.update()
        gctrl.clock.tick(FPS)    
       
def init() :
    gctrl.set_surface(pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT)))
    pygame.display.set_caption(TITLE_STR)

if __name__ == '__main__' :
    init()
    while True :
        mode = start()
        if mode == 'Dijkstra' :
            print(mode)
        elif mode == 'A-star' :
            print(mode)
        elif mode == 'BFS' :
            print(mode)
        elif mode == 'DFS' :
            print(mode)

