# INFOMSCIP-4-9
Group Project 

f = probability the color is flipped when placed. (red instead of blue etc)

n = # of points generated in Q

k = # of nearest neighbors to be observed

Q = the square

T = the triangle inside the square

p = a single point inside Q

S = the series of points inside Q

-Generate 10k points inside square Q, with triangle T inside Q (3,3),(3,7),(7,7). points placed inside T will be blue, points outside T within Q are red.
-For probability f, each point placed will have color reversed
-For each point p within Q, determine n nearest neighbors and the color obtained from the k-NN classification. use this color to classify point p. if p is inside T but is red, it is misclassified. if p is outside T but is blue, it is misclassified.
-compute the number of misclassified points among the 10k points in Q.
-repeat 20 times for 20 values using the same settings, but different points in S (newly random points each time) and, if f > 0, different outliers

-For EXP 1: n = 100, 200, 300, 400, 500, 600, 700, 800. k = 5. f = 0.

-For EXP 2: f = 0, 0.05, 0.1, 0.15, 0.2, 0.25, 0.3. k = 5. n = 500.

-EXP 3: create an experiment where ONLY the shape is changed (not triangle propotions/area). n=500, k=5, f=0. Use a shape to answer the question "How does the number of misclassifications of k-NN (colors that are classified as the wrong color by the nearest neighbors) depend on the shape of the triangle separator?"