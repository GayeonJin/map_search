#!/usr/bin/python

import sys
import csv

import pygame
import random
import math

from gresource import *
from map_data import *
from player import *

MAP_XOFFSET = 10
MAP_YOFFSET = 10

CELL_WIDTH = 30
CELL_HEIGHT = 30

map_color = {
    0 : COLOR_WHITE,
    1 : COLOR_BLUE,
    2 : COLOR_BLUE,
    3 : COLOR_BLUE,
    4 : COLOR_BLUE,
    5 : COLOR_BLUE,
    6 : COLOR_BLUE,
    7 : COLOR_BLUE,
    8 : COLOR_BLUE,
}

class map_object :
    def __init__(self, rows, cols, map_data) :
        self.cell = [] 

        self.rows = rows
        self.cols = cols
        
        for x in range(cols) :
            self.cell.append([])
            for y in range(rows) :
                self.cell[x].append(0)

        for y, row_data in enumerate(map_data) :
            for x, data in enumerate(row_data) :
                self.cell[x][y] = data

    def get_size(self) :
        return self.rows, self.cols

    def get_scr_size(self) :
        pad_width = 2 * MAP_XOFFSET + self.cols * CELL_WIDTH
        pad_height = 2 * MAP_YOFFSET + self.rows * CELL_HEIGHT
        return (pad_width, pad_height) 

    def is_wall(self, x, y) :
        if self.cell[x][y] != 0 :
            return True
        else :
            return False
        
    def get_wall_texture(self, x, y) :
        return self.cell[x][y] - 1

    def get_pos(self, screen_xy) :
        for y in range(self.rows) :
            for x in range(self.cols) :
                rect = self.get_rect(x, y)
                if screen_xy[0] > rect.left and screen_xy[0] < rect.right :
                    if screen_xy[1] > rect.top and screen_xy[1] < rect.bottom :      
                        return (x, y)
                    
        return (None, None)

    def get_rect(self, x, y) :
        rect = pygame.Rect(MAP_XOFFSET, MAP_YOFFSET, CELL_WIDTH, CELL_HEIGHT)

        # cell[0][0] is left and bottom
        rect.x += x * CELL_WIDTH
        # rect.y += ((self.rows - 1) - y) * CELL_HEIGHT
        rect.y += y * CELL_HEIGHT
        return rect        

    def draw(self) :
        rect = pygame.Rect(MAP_XOFFSET, MAP_YOFFSET, CELL_WIDTH, CELL_HEIGHT)

        # rect.y += (self.rows - 1) * CELL_HEIGHT
        for y in range(self.rows) :
            for x in range(self.cols) :
                pygame.draw.rect(gctrl.surface, map_color[self.cell[x][y]], rect, 0)

                rect.x += CELL_WIDTH
            #rect.y -= CELL_HEIGHT
            rect.y += CELL_HEIGHT
            rect.x = MAP_XOFFSET

if __name__ == '__main__' :
    print('map object')

    print('map width %d, height %d'%(len(world_map[0]), len(world_map)))
    map = map_object(len(world_map), len(world_map[0]), world_map)

    (scr_width, scr_height) = map.get_scr_size()
    gctrl.set_surface(pygame.display.set_mode((scr_width, scr_height)))
           
    player = player_object(22, 3, -1, 0)
    player.set_map(map)
   
    keys = {}
    keys[pygame.K_UP] = False
    keys[pygame.K_DOWN] = False
    keys[pygame.K_RIGHT] = False
    keys[pygame.K_LEFT] = False
    while True :
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.KEYDOWN :
                if event.key == pygame.K_UP or event.key == pygame.K_DOWN or event.key == pygame.K_RIGHT or event.key == pygame.K_LEFT:
                    keys[event.key] = True
            if event.type == pygame.KEYUP :
                if event.key == pygame.K_UP or event.key == pygame.K_DOWN or event.key == pygame.K_RIGHT or event.key == pygame.K_LEFT:
                    keys[event.key] = False

        # key processing
        if keys[pygame.K_UP] == True :
            player.move_forward()
        elif keys[pygame.K_DOWN] == True :
            player.move_backward()
        elif keys[pygame.K_RIGHT] == True :
            player.turn_right()      
        elif keys[pygame.K_LEFT] == True :
            player.turn_left() 

        gctrl.surface.fill(COLOR_WHITE)    
        map.draw()

        player.draw(map.get_rect(int(player.x), int(player.y)))

        pygame.display.update()



