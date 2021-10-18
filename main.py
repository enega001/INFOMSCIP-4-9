import numpy as np
from matplotlib import pyplot as plt

def plotPoints(a, b, c, n):
    xcoords = np.random.uniform(low=0, high=10, size=n);
    ycoords = np.random.uniform(low=0, high=10, size=n);
    #go thorugh each point and check which color it will get
    for x,y in zip(xcoords, ycoords):
        if inTriangle(a, b, c, [x,y]):
            plt.plot(x,y, color="red");
        else:
            plt.plot(x,y, color="blue");
  
#function credit to https://blackpawn.com/texts/pointinpoly/
def inTriangle(a, b, c, p):
    # Compute vectors        
    v0 = (c[0] - a[0], c[1] - a[1])
    v1 = (b[0] - a[0], b[1] - a[1])
    v2 = (p[0] - a[0], p[1] - a[1])
    
    # Compute dot products
    dot00 = np.dot(v0, v0)
    dot01 = np.dot(v0, v1)
    dot02 = np.dot(v0, v2)
    dot11 = np.dot(v1, v1)
    dot12 = np.dot(v1, v2)
    
    # Compute barycentric coordinates
    invDenom = 1 / (dot00 * dot11 - dot01 * dot01)
    u = (dot11 * dot02 - dot01 * dot12) * invDenom
    v = (dot00 * dot12 - dot01 * dot02) * invDenom
    
    # Check if point is in triangle
    result = ((u >= 0) and (v >= 0) and (u + v < 1))
    return result
    
def main():
    #triangle
    p1 = [3,3];
    p2 = [3,7];
    p3 = [7,7];
    p1p2x = [3,3]
    p1p2y = [3,7]
    p2p3x = [3,7]
    p2p3y = [7,7]
    p3p1x = [3,7]
    p3p1y = [3,7]
    
    plt.plot(p1p2x, p1p2y);
    plt.plot(p2p3x, p2p3y);
    plt.plot(p3p1x, p3p1y);
    
    #plt.plot([[p1[0], p2[0]], [p1[1], p2[1]]])
    #plt.plot([[p2[0], p3[0]], [p2[1], p3[1]]])
    #plt.plot([[p3[0], p1[0]], [p3[1], p1[1]]])
    
    plt.show();
    plotPoints(p1, p2, p3, 5);


if __name__ == '__main__':
    main()
    