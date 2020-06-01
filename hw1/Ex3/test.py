import matplotlib.pyplot as plt
import numpy as np
import math

def f1(y):
    t = math.pow(y,2) * math.exp(-math.pow(y,2))
    return t

x = []
y = []

a=np.linspace(-1,1,100)
for i in a:
    x.append(i)
    y.append(f1(i))

plt.plot(x,y)
plt.show()