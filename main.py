import numpy as nm
import matplotlib.pyplot as plt

n=500
x = nm.random.uniform(0.0, 10.0, n)
y = nm.random.uniform(0.0, 10.0, n)


for i in range(0 , n):
    if (y[i] >= 3) and (x[i] <= 7) and (x[i] >= y[i]):
        plt.scatter(x[i], y[i], c="blue")
    else:
        plt.scatter(x[i], y[i], c="red")


plt.show()