import matplotlib.pyplot as plt
import numpy as np

# (0,1) random num
ns = [20, 50, 100, 200, 300, 500, 1000, 5000]

def getPiBy(n, doDraw=0):
    xs = np.random.random(n)
    ys = np.random.random(n)
    i = 0
    count = 0.
    while i < n :
        x = xs[i] 
        y = ys[i]
        if x*x + y*y <=1:
            count += 1
            if doDraw:
                plt.scatter(x, y, color='r', marker='+')
        else:
            if doDraw:
                plt.scatter(x, y, color='b', marker='*')
        i += 1
    plt.show()
    return count*4.00/n

if __name__ == "__main__":
    for n in ns:
        i = 0
        piData = np.array([])
        while i < 20:
            piData = np.append(piData, getPiBy(n))
            i+=1
        print(n, ":")
        print(piData)
        print(np.average(piData), np.var(piData))


