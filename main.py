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

    menus = {
        pygame.K_d : ['Dijkstra', 'd : Dijkstra'],
        pygame.K_a : ['A-star', 'a : A-star'],
        pygame.K_b : ['BFS', 'b : BFS'],
        pygame.K_c : ['DFS', 'c : DFS'],
        pygame.K_x : ['exit', 'x : exit'],
    }

    for i, key in enumerate(menus) :
        y_offset = 150 - i * 25
        gctrl.draw_string(menus[key][1], 0, y_offset, ALIGN_CENTER | ALIGN_BOTTOM, 25, COLOR_BLUE)

    while True :
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminate()
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_ESCAPE:
                    terminate()
                elif event.key == pygame.K_x :
                    terminate()
                else :
                    if event.key in menus :
                        return menus[event.key][0]                    
 
        pygame.display.update()
        gctrl.clock.tick(FPS)    
       
def run(mode) :
    print(mode)

def init() :
    gctrl.set_surface(pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT)))
    pygame.display.set_caption(TITLE_STR)

if __name__ == '__main__' :
    init()
    while True :
        mode = start()
        run(mode)

