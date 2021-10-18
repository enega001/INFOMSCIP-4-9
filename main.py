import numpy as np
import random
import matplotlib.pyplot as plt

from shapely.geometry import Polygon, Point


def main():
    #Define polygons
    q_square = Polygon([(0,0),(10,0),(0,10),(10,10)])
    t_triangle = Polygon([(3,3),(7,3),(3,7)])
    n = 500

    points = generate_rand_points(q_square, t_triangle, n)
    
    for p in points:
        print(p.x,",",p.y)

#Q = square, T = triangle, N = number of points to generate
def generate_rand_points(Q, T, n):
    #bounds of square
    min_x, min_y, max_x, max_y = Q.bounds

    #list of points
    points = []

    while len(points) < n:
        random_point = Point([random.uniform(min_x, max_x), random.uniform(min_y, max_y)])
        if (random_point.within(Q)):
            points.append(random_point)
    
    return points

if __name__ == '__main__':
    main()