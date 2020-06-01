from mpl_toolkits import mplot3d
import matplotlib.pyplot as plt
import numpy as np
import math

ns = [5,10,20,30,40,50,60,70,80,100,200,500]
ax = plt.axes(projection='3d')


def target_func(x, y):
    t = math.pow(y,2) * math.exp(-math.pow(y,2)) + math.pow(x,4) * math.exp(-math.pow(x,2))
    d = x * math.exp(-math.pow(x,2))
    return t/d

zmax = target_func(4,1) - target_func(2,0)

def getRes(n, doDraw=0):
    xs = np.random.random(n)
    ys = np.random.random(n)
    zs = np.random.random(n)
    i = 0
    count = 0.
    
    while i < n :
        x = xs[i]*2+2
        y = ys[i]*2-1
        z = zs[i]*zmax
        if target_func(x,y) > z:
            count += 1
            if doDraw:
                ax.scatter3D(x, y, z, c=z, cmap='Greens')
        else:
            if doDraw:
                ax.scatter3D(x, y,z,c=z ,cmap='Reds')
        i += 1
    return count*1.00/n*(2*2*zmax)

if __name__ == "__main__":
    for n in ns:
        i = 0
        rdata = np.array([])
        while i < 100:
            rdata = np.append(rdata, getRes(n))
            i+=1
        print(n, "\t",np.average(rdata),"\t",np.var(rdata))