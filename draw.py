import pygame

WIDTH = 800
HEIGHT = 600

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
GRAY = (128, 128, 128)

def initialise_map():
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("RRT Pathfinding")
    clock = pygame.time.Clock()

    return [screen, clock]

def screen_fill(screen):
    screen.fill(BLACK)

def draw_circle(screen, obs, OBSTACLE_RADIUS, color = GRAY):
    pygame.draw.circle(screen, color, obs, OBSTACLE_RADIUS)

def draw_line(screen, nearest_point, new_node, color = BLUE):
    pygame.draw.line(screen, color, nearest_point, new_node, 1) 

def flip_display():
    pygame.display.flip()

def clock_tick(clock):
    clock.tick(30)
