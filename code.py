import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle
from shapely.geometry import Point, Polygon, LineString, MultiLineString
import geopandas as gpd
import numpy as np
import random
import math

# starting and ending point coordiates
x1 = [8]
x2 = [25]
y1 = [40]
y2 = [5]

# condition = True
stepSize = 5
min_dist = 100000000

abc = 1
radius = 5                      # circle for goal region
node_x = [8]                    # to store x coordinates of all nodes
node_y = [40]                   # to store y coordinates of all nodes
rand_x = []                     # to store random x coordinates
rand_y = []                     # to store random y coordinates
nearest_x = [8]                 # to store x coordinates of nearest nodes
nearest_y = [40]                # to store y coordinates of nearest nodes
new_node_x = []                 # to store x coordinates of new nodes
new_node_y = []                 # to store y coordinates of new nodes

# to store all nodes and linestring data
shape1 = [Polygon([(0, 0), (0, 50), (3, 50), (3, 0)]),
          Polygon([(0, 0), (0, 3), (50, 3), (50, 0)]),
          Polygon([(47, 0), (47, 50), (50, 50), (50, 0)]),
          Polygon([(0, 47), (0, 50), (50, 50), (50, 47)]),
          Polygon([(15, 25), (15, 35), (20, 35), (20, 25)]),
          Polygon([(20, 10), (20, 20), (40, 20), (40, 10)]),
          Point(8,40), Point(25, 5)]

# to store obstacle data
polygon_data2 = [Polygon([(0, 0), (0, 50), (3, 50), (3, 0)]),
                 Polygon([(0, 0), (0, 3), (50, 3), (50, 0)]),
                 Polygon([(47, 0), (47, 50), (50, 50), (50, 0)]),
                 Polygon([(0, 47), (0, 50), (50, 50), (50, 47)]),
                 Polygon([(15, 25), (15, 35), (20, 35), (20, 25)]),
                 Polygon([(20, 10), (20, 20), (40, 20), (40, 10)])]

class RRT:

    def __init__(self, junk):
        self.junk = junk

    # function to show the obstacles in graph
    def object_creation(self, obstacles):
        self.obstacles = obstacles
        shape = self.obstacles

        # to add multiple shapes in single graph
        ax.add_patch(shape)

    # function to create obstacles
    def Polygon_creation(self, obstacles):
        self.obstacles = obstacles
        Poly = Polygon(self.obstacles)
        RRT_11 = RRT([])
        RRT_11.random_point_sampling()

    # function to sample random point
    def random_point_sampling(self):
        x = random.uniform(3, 47)
        y = random.uniform(3, 47)
        #print(x, y)
        rand_x.append(x)
        rand_y.append(y)

        RRT_7 = RRT([])
        RRT_7.nearest_node()

    # function to find distance between two points
    def distance(self, x1, y1, x2, y2):
        self.x1 = x1
        self.x2 = x2
        self.y1 = y1
        self.y2 = y2
        dist = round(float(math.sqrt((x1 - x2)**2 + (y1 - y2)**2)), 3)
        return dist

    def cut(self):
        if abc == 1:
            pass
        else:
            pass 

    # to display final graph after finding goal
    def final_print(self):
        RRT_13 = RRT([])
        dp_shapely_10 = gpd.GeoSeries(shape1)
        dp_shapely_10.plot()
        plt.show()
        RRT_13.cut()


    # function to find the nearest node to the random point generated
    def nearest_node(self):
        RRT_1 = RRT([])
        global min_dist
        min_dist = 10000000
        for i in range(len(node_x)):
            if RRT_1.distance(rand_x[-1], rand_y[-1], node_x[i], node_y[i]) < min_dist:
                min_dist = RRT_1.distance(rand_x[-1], rand_y[-1], node_x[i], node_y[i])
                x_min = node_x[i]
                y_min = node_y[i]
        nearest_x.append(x_min)
        nearest_y.append(y_min)

        RRT_1.new_node()

    def sin(self):
        RRT_2 = RRT([])
        if rand_x[-1] - nearest_x[-1] == 0:
            rand_x.pop()
            rand_y.pop()
            nearest_x.pop()
            nearest_y.pop()
            RRT_2.random_point_sampling()

        else:
            m = (rand_y[-1] - nearest_y[-1])/(rand_x[-1] - nearest_x[-1])
            val = abs(m / (math.sqrt(1 + (m**2))))
            return val

    def cos(self):
        RRT_3 = RRT([])
        if rand_x[-1] - nearest_x[-1] == 0:
            rand_x.pop()
            rand_y.pop()
            nearest_x.pop()
            nearest_y.pop()
            RRT_3.random_point_sampling()

        else:
            m = float((rand_y[-1] - nearest_y[-1])/(rand_x[-1] - nearest_x[-1]))
            val = abs(1/(math.sqrt(1 + (m**2))))

            if m > 0:
                return val

            else:
                return -val

    # function to generate new node in the direction of the random node
    def new_node(self):
        RRT_4 = RRT([])
        if rand_y[-1] < nearest_y[-1]:
            new_step = -stepSize
        else:
            new_step = stepSize

        # using parametric equation of line
        x_new = round(float((new_step*RRT_4.cos()) + nearest_x[-1]), 3)
        y_new = round(float(((new_step*RRT_4.sin()) + nearest_y[-1])), 3)
        new_node_x.append(x_new)
        node_x.append(x_new)
        new_node_y.append(y_new)
        node_y.append(y_new)
        RRT_4.valid_node()

    # function to check if the new node is valid or not (path intersects obstacles or not)
    def valid_node(self):
        RRT_8 = RRT([])
        a = 1
        line_a = LineString([(nearest_x[-1], nearest_y[-1]), (new_node_x[-1], new_node_y[-1])])

        for i in polygon_data2:
            if line_a.intersects(i):
                a = 0
                node_x.pop()
                node_y.pop()
                rand_x.pop()
                rand_y.pop()
                nearest_x.pop()
                nearest_y.pop()
                new_node_x.pop()
                new_node_y.pop()
                # RRT_8.random_point_sampling()
                break

        if a == 1:
            P = Point(new_node_x[-1], new_node_y[-1])
            shape1.append(P)
            shape1.append(line_a)
            print(node_x)
            print(node_y)
            dp_shape = gpd.GeoSeries(shape1)
            dp_shape.plot(color = 'grey')
            plt.show()
            RRT_8.near_goal()    

        else:
            RRT_8.random_point_sampling()  

    # function to check if we have reached near the goal
    def near_goal(self):
        RRT_5 = RRT([])
        distance = RRT_5.distance(25, 5, new_node_x[-1], new_node_y[-1])
        line_A = LineString([(25, 5), (new_node_x[-1], new_node_y[-1])])
        print(distance)
        print('---------------------')
        if distance < radius or distance == radius:
            print('goal found')

            P10 = Point(25, 5)
            shape1.append(line_A)
            RRT_5.final_print()

        else:
            print("------------------")
            RRT_5.random_point_sampling()


ax = plt.gca()

# boundry and other obstacles for object_creation() function
shapes = [Rectangle((0, 0), width = 3, height = 50, facecolor = "black"),
          Rectangle((0, 0), width = 50, height = 3, facecolor = "black"),
          Rectangle((47, 0), width = 3, height = 50, facecolor = "black"),
          Rectangle((0, 47), width = 50, height = 3, facecolor = "black"),
          Rectangle((15, 25), width = 5, height = 10, facecolor = "grey"),
          Rectangle((20, 10), width = 20, height = 10, facecolor = "grey")]

# boundry and other obstacles for Polygon_creation() function
obs = [[(0, 0), (0, 50), (3, 50), (3, 0)],
       [(0, 0), (0, 3), (50, 3), (50, 0)],
       [(47, 0), (47, 100), (50, 50), (50, 0)],
       [(0, 47), (0, 50), (50, 50), (50, 47)],
       [(15, 25), (15, 35), (20, 35), (20, 25)],
       [(20, 10), (20, 20), (40, 20), (40, 10)]]

# using polymorphism to show obstacles in graph
def create_object(lists):
    for list in lists:
        a = RRT([])
        a.object_creation(list)

# using polymorphism to create obstacles in graph
def create_Polygon(lists):
    for list in lists:
        a = RRT([])
        a.Polygon_creation(list)

create_object(shapes)

plt.xticks([0, 10, 20, 30, 40 ,50])
plt.yticks([0, 10, 20, 30, 40 ,50])

plt.plot(x1, y1, marker = '.', markersize = 20)
plt.plot(x2, y2, marker = '.', markersize = 20)


plt.axis("scaled")
plt.show()
create_Polygon(obs)
