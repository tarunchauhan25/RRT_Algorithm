# import pygame
import math 
import time 
import random 
from draw import *

OBSTACLE_RADIUS = 50
STEP_SIZE = 100
MAX_ITER = 1000

def dis(point1, point2):
    x1 = point1[0]
    y1 = point1[1] 
    x2 = point2[0]
    y2 = point2[1]

    return math.sqrt((x1 - x2)**2 + (y1 - y2)**2) 

def is_in_obstacle(point, obstacles):
    for obj in obstacles:
        if dis(point, obj) <= OBSTACLE_RADIUS:
            return True 
    return False 

class RRT:
    def __init__(self, start, end, obstacles):
        self.start = start 
        self.end = end 
        self.obstacles = obstacles 
        self.nodes = [start]
        self.parent = {self.start: self.start}

    def is_in_obstacle(self, point):
        for obj in self.obstacles:
            if dis(point, obj) <= OBSTACLE_RADIUS:
                return True 
        return False 

    def get_random_point(self):
        while True:
            point = (random.randint(1, WIDTH), random.randint(1, HEIGHT))
            if not self.is_in_obstacle(point):
                return point 
            
    def find_nearest(self, point):
        nearest = self.nodes[0]
        minDist = dis(point, nearest)

        for node in self.nodes:
            if (dis(node, point) < minDist):
                minDist = dis(node, point) 
                nearest = node 

        return nearest 
    
    def step_towards(self, nearest_node, random_point):
        x1 = nearest_node[0]
        y1 = nearest_node[1]
        x2 = random_point[0]
        y2 = random_point[1]
        dist = dis(nearest_node, random_point)

        direction = ((x2 - x1) / dist, (y2 - y1) / dist)
        new_node = (int(x1 + STEP_SIZE * direction[0]), int(y1 + STEP_SIZE * direction[1]))

        return new_node
    
    def print_path(self, screen):
        curr_node = self.end
        while self.parent[curr_node] != curr_node:
            draw_line(screen, curr_node, self.parent[curr_node], GREEN)
            flip_display()
            time.sleep(0.5)
            curr_node = self.parent[curr_node]
    
    def run(self, screen): 
        for _ in range(MAX_ITER):
            random_point = self.get_random_point()
            nearest_point = self.find_nearest(random_point)
            new_node = self.step_towards(nearest_point, random_point)

            if not (self.is_in_obstacle(new_node)):
                self.nodes.append(new_node)
                self.parent[new_node] = nearest_point

                draw_circle(screen, new_node, 3)
                draw_line(screen, nearest_point, new_node)
                flip_display()

                time.sleep(0.5)

            if (dis(new_node, self.end) <= STEP_SIZE):
                self.parent[self.end] = new_node
                draw_line(screen, new_node, self.end)
                flip_display()
                print("Reached Goal!")
                self.print_path(screen)
                print("Finished process")
                return 1
        return -1
