import numpy as nm
import matplotlib.pyplot as plt
import random
import math
import sys
import os
from matplotlib.patches import Polygon


# look at the colors of the k nearest neighbours and return which color the point will be classified
def defineColor(x, y, xcoords, ycoords, colors, k):
    neighbours = nearestNeighbour(x, y, xcoords, ycoords, k)

    redcount = 0
    bluecount = 0

    for (a, b, distance) in neighbours:
        if (colors[(a, b)] == "red"):
            redcount += 1
        else:
            bluecount += 1

    if (redcount > bluecount):
        return "red"
    else:
        return "blue"


# calculate the k nearest neighbours
def nearestNeighbour(x, y, xcoords, ycoords, k):
    neighbours = []
    # List of all points
    list_of_points = zip(xcoords, ycoords)
    # Makes a list of all the distances
    dists = nm.array([abs(math.hypot(x - i, y - j)) for i, j in list_of_points if abs(math.hypot(x - i, y - j)) != 0])
    # Get the indexes for the k lowest distances
    min_dist_indexes = nm.argpartition(dists, k)
    # For i < k
    for i in range(0, k):
        # Add the x, y, and distance for the k nearest neighbors to the list
        neighbours.append((xcoords[min_dist_indexes[i]], ycoords[min_dist_indexes[i]], dists[min_dist_indexes[i]]))

    return neighbours


# Count the number of mislabelled points
def count_mistakes(x, y, colors, k):
    mistakecount = 0

    # go through all the points
    for px, py in zip(x, y):
        # check color for that point, as determined by nearest neighbors
        color = defineColor(px, py, x, y, colors, k)

        # if point is within the triangle...
        if (py >= 3) and (px <= 7) and (px >= py):
            # And mislabelled red, increment the mistake counter
            if color == "red":
                mistakecount += 1
        # else if the point is outside the triangle...
        else:
            # and the point is mislabelled blue, increment the mistake counter
            if color == "blue":
                mistakecount += 1
    return mistakecount


def run_experiment(n, f, k):
    # Generate point locations randomly within the square
    x = nm.random.uniform(0.0, 10.0, n)
    y = nm.random.uniform(0.0, 10.0, n)

    colors = {}

    for i in range(0, n):
        # If the points falls within the triangle...
        if ((y[i] >= 3) and (y[i] <= 1.73*(x[i]-3) + 3) and (y[i] <= -1.73*(x[i]-6.722) + 3)) or ((y[i] <= 5.15) and (y[i] >= -1.73*(x[i] - 3) + 5.15) and (y[i] >= 1.73*(x[i] - 6.72) + 5)):
            # Point is blue by default
            if (random.uniform(0, 1) > f):
                plt.scatter(x[i], y[i], c="blue", s=10)
                colors.update({(x[i], y[i]): "blue"})
            # Unless the probability check is failed, then it's red
            else:
                plt.scatter(x[i], y[i], c="red", s=10)
                colors.update({(x[i], y[i]): "red"})
        # If the point is outside the triangle...
        else:
            # Point is red by default
            if (random.uniform(0, 1) > f):
                plt.scatter(x[i], y[i], c="red", s=10)
                colors.update({(x[i], y[i]): "red"})
            # Unless the probality check is failed, then it's blue
            else:
                plt.scatter(x[i], y[i], c="blue", s=10)
                colors.update({(x[i], y[i]): "blue"})

    # Draw triangle T
    pts = nm.array([[3, 3], [3.621, 4.075], [3, 5.15], [4.243, 5.15], [4.861, 6.22], [5.479, 5.15], [6.807, 5.15], [6.143, 4.002], [6.722, 3], [5.564, 3], [4.903, 1.857], [4.243, 3]])
    T = Polygon(pts, closed=True)
    ax = plt.gca()
    T.set_fill(False)
    T.set_edgecolor("k")
    ax.add_patch(T)
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 10)

    plt.show()

    # print the number of mistakes
    return count_mistakes(x, y, colors, k)


# Run the program
def main():
    # takes the argument from the command line for the values of n, f, and k
    args = sys.argv[1:]
    results = []

    # fills list of mistake counts
    for i in range(0, int(args[3])):
        results.append(run_experiment(int(args[0]), float(args[1]), int(args[2])))

    # creates output file if none exists
    if not os.path.exists('output.txt'):
        os.mknod('output.txt')

    # writes count to file, including header of the experiment info
    with open('output.txt', 'a+') as f:
        f.write('n = %i, f = %f, k = %i' % (int(args[0]), float(args[1]), int(args[2])))
        f.write("\n")
        for output in results:
            f.write(str(output))
            f.write("\n")

    f.close()


if __name__ == "__main__":
    main()


