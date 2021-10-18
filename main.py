import numpy as nm
import matplotlib.pyplot as plt
import random
import math

#look at the colors of the k nearest neighbours and return which color the point will get
def defineColor(x, y, xcoords, ycoords, colors):
    neighbours = nearestNeighbour(x, y, xcoords, ycoords, k);
    
    redcount = 0;
    bluecount = 0;
    
    for (a, b, distance) in neighbours:
        if (colors[(a,b)] == "red"):
            redcount = redcount + 1;
        else:
            bluecount = bluecount + 1;
            
    
    if (redcount > bluecount):
        return "red";
    else:
        return "blue";


#calculate the k nearest neighbours
def nearestNeighbour(x, y, xcoords, ycoords, k):
    neighbours = [];
    furthestdistance = 100;
    
    for nx, ny in zip(xcoords, ycoords):
        if distance(x, y, nx, ny) < furthestdistance and distance(x, y, nx, ny) != 0:
            orderList(neighbours, nx, ny, distance(x, y, nx, ny), k);
        else:
            continue;
    
    return neighbours;
            
                
        
#the distancer between two points     
def distance(x, y, nx, ny):
    return math.sqrt((nx-x)*(nx-x) + (ny-y)*(ny-y))

#update the neighbours list with the new point, checking if the distance is shorter and popping the last element if the count is over k
def orderList(l, x, y, distance, k):
    index = 0;
    for (a, b, c) in l:
        if (c > distance):
            l.insert(index, [(x, y, distance)]);
    index = index + 1;
    
    if(len(l) > k):
        l.pop(k-1);
    
    return l;

n = 500
f =  0.7             
k = 5

x = nm.random.uniform(0.0, 10.0, n)
y = nm.random.uniform(0.0, 10.0, n)

colors = {};


for i in range(0 , n):
    if (y[i] >= 3) and (x[i] <= 7) and (x[i] >= y[i]):
        if (random.uniform(0,1) > f ):
            plt.scatter(x[i], y[i], c="blue")
            colors.update({(x[i],y[i]):"blue"});
        else:
            plt.scatter(x[i], y[i], c="red")
            colors.update({(x[i],y[i]):"red"});
    else:
        if (random.uniform(0,1) > f ):                                                                                                                      
            plt.scatter(x[i], y[i], c="red")
            colors.update({(x[i],y[i]):"red"});
        else:
            plt.scatter(x[i], y[i], c="blue")
            colors.update({(x[i],y[i]):"blue"});

plt.show()

mistakecount = 0;

#go through all the points and do nearest neighbour search
for px, py in zip(x, y):
    color = defineColor(px, py, x, y, colors);
    
    if (py >= 3) and (px <= 7) and (px >= py) and color =="blue":
        mistakecount = mistakecount + 1;

print(mistakecount)

                                                                                                                                    