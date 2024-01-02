#!/usr/bin/python

import sys
import math

import pygame

from gresource import *

class player_object :
    def __init__(self, x, y, dx = -1.0, dy = 0.0) :
        self.x = x
        self.y = y
        self.dx = dx
        self.dy = dy

        frame_time = 1 / FPS
        self.move_speed = frame_time * 0.2
        self.rot_speed = frame_time * 0.2

    def set_map(self, map) :
        self.map = map

    def set_speed(self, vel, rot_vel) :
        self.move_speed = vel
        self.rot_speed = rot_vel

    def move_forward(self) :
        next_x = self.x + self.dx * self.move_speed
        next_y = self.y + self.dy * self.move_speed

        if self.map.is_wall(int(next_x), int(self.y)) == False :
            self.x = next_x
        if self.map.is_wall(int(self.x), int(next_y)) == False :
            self.y = next_y

        print(self.x, self.y)

    def move_backward(self) :
        next_x = self.x - self.dx * self.move_speed
        next_y = self.y - self.dy * self.move_speed

        if self.map.is_wall(int(next_x), int(self.y)) == False :
            self.x = next_x
        if self.map.is_wall(int(self.x), int(next_y)) == False :
            self.y = next_y  

        print(self.x, self.y)

    def rotation_matrix(self, angle, x, y) :
        x1 = math.cos(angle) * x - math.sin(angle) * y
        y1 = math.sin(angle) * x + math.cos(angle) * y
        return x1, y1

    def turn_right(self) :
        self.dx, self.dy = self.rotation_matrix(-self.rot_speed, self.dx, self.dy)
        # plane_x, plane_y = self.rotation_matrix(-self.rot_speed, plane_x, plane_y)

        print(self.x, self.y, self.dx, self.dy)  

    def turn_left(self) :
        self.dx, self.dy = self.rotation_matrix(self.rot_speed, self.dx, self.dy)
        # plane_x, plane_y = self.rotation_matrix(self.rot_speed, plane_x, plane_y)

        print(self.x, self.y, self.dx, self.dy) 
        
    def draw(self, rect) :
        cell_width = rect.width
        cell_height = rect.height

        offset_x = int((self.x - int(self.x)) * cell_width)
        offset_y = int((self.y - int(self.y)) * cell_height)
        
        center_x = rect.left + offset_x
        center_y = rect.top + offset_y

        dir_x = int(center_x + self.dx * 10)
        dir_y = int(center_y + self.dy * 10)

        pygame.draw.circle(gctrl.surface, COLOR_RED, (center_x, center_y), 10, 0)
        pygame.draw.line(gctrl.surface, COLOR_BLACK, (center_x, center_y), (dir_x, dir_y), 1)

if __name__ == '__main__' :
    print('player object')