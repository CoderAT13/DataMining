import matplotlib.pyplot as plt
import numpy as np

ns = [5,10,20,30,40,50,60,70,80,100]

def getRes(n, doDraw=0):
    xs = np.random.random(n)
    ys = np.random.random(n)
    i = 0
    count = 0.
    while i < n :
        x = xs[i] 
        y = ys[i]
        if x*x*x >= y:
            count += 1
            if doDraw:
                plt.scatter(x, y, color='r', marker='+')
        else:
            if doDraw:
                plt.scatter(x, y, color='b', marker='*')
        i += 1
    plt.show()
    return count*1.00/n

if __name__ == "__main__":
    for n in ns:
        i = 0
        rdata = np.array([])
        while i < 100:
            rdata = np.append(rdata, getRes(n))
            i+=1
        print(n, ":")
        print(np.average(rdata), np.var(rdata))