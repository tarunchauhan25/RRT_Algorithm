from rrt_algo import *
from draw import *

OBSTACLE_COUNT = 5

def create_obstacles():
    obstacles = []
    for _ in range(OBSTACLE_COUNT):
        obstacle = (random.randint(OBSTACLE_RADIUS, WIDTH - OBSTACLE_RADIUS), random.randint(OBSTACLE_RADIUS, HEIGHT - OBSTACLE_RADIUS))
        obstacles.append(obstacle)
    return obstacles

def main():
    screen, clock = initialise_map()
    obstacles = create_obstacles()
    start = None
    goal = None
    rrt = None

    setting_start = 1
    setting_background = 1
    create_ob = 1
    running = True

    while running:
        if setting_background == 1:
            screen_fill(screen)
            flip_display()
            setting_background = 0

        # Draw obstacles
        if create_ob == 1:
            for obs in obstacles:
                draw_circle(screen, obs, OBSTACLE_RADIUS)
            flip_display()
            create_ob = 0

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = pygame.mouse.get_pos()
                if not is_in_obstacle((x, y), obstacles):
                    if setting_start:
                        start = (x, y)
                        print(f"Start point set at {start}")
                        draw_circle(screen, start, 10, RED)
                        flip_display()
                        setting_start = 0
                    else:
                        goal = (x, y)
                        print(f"Goal point set at {goal}")
                        draw_circle(screen, goal, 10, RED)
                        flip_display()

                        rrt = RRT(start, goal, obstacles)
                        rrt.run(screen)
                else:
                    print("Invalid point, try again.")

    pygame.quit()

if __name__ == "__main__":
    main()
