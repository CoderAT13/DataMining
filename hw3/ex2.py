import numpy as np
import matplotlib.pyplot as plt
from prettytable import PrettyTable
import random
import math
import copy

base = 10

def readFile(filename):
    np.set_printoptions(suppress=True)
    rfile = open(filename)
    array4Lines = rfile.readlines()
    linesNum = len(array4Lines)
    matrix = np.zeros((linesNum, 7))
    index = 0
    for line in array4Lines:
        line = line.strip()             # delete \n
        listFromLine = line.split(' ')  # split space
        matrix[index, :] = listFromLine[0:7]
        index += 1
    return matrix

def p(ex):
    return 1.0/(1+math.exp(-ex))

def s_gradient_decent():
    alpha = 0.00015 # learn rate
    # init
    theta = np.zeros(7)
    
    testMat = readFile('./doc/dataForTestingLogistic.txt')

    resTable = PrettyTable(["number of iterations", "theta0", "theta1", "theta2", "theta3", "theta4", "theta5", "theta6", "t0-rate", "t1-rate"])

    training_errors = []
    iter_times = []
    testing_errors = []
    m = len(trainMat)
    n = len(testMat)
    count = 1

    for j in range(15*base):
        index = random.randint(0, m-1)
        hx = theta[0]
        for i in range(1,7):
            hx += theta[i] * trainMat[index][i-1]

        # one sample to refresh theta
        theta[0] = theta[0] + alpha*(trainMat[index][6] - p(hx))
        for i in range(1,7):
            theta[i] = theta[i] + alpha*(trainMat[index][6] - p(hx)) * trainMat[index][i-1]

        if j % (base-1) == 0 and j >= (base-1):
            iter_times.append(j + count)
            tmp = 0
            test_tmp = 0
            LCL = 0
            test_LCL = 0

            for idx in range(m):
                hx = theta[0]
                for i in range(1,7):
                    hx += theta[i] * trainMat[idx][i-1]
                LCL += math.log(p(hx)) + math.log(1-p(hx))
                if np.abs(p(hx) - trainMat[idx][6]) < 0.5:
                    tmp += 1
            trainError = 1-(1.0/m) * tmp
            training_errors.append(trainError)
            # training_errors.append(LCL)

            for idx in range(n):
                hx = theta[0]
                for i in range(1,7):
                    hx += theta[i] * testMat[idx][i-1]
                test_LCL += math.log(p(hx)) + math.log(1-p(hx))
                if np.abs(p(hx) - testMat[idx][6]) < 0.5:
                    test_tmp += 1
            testError = 1-(1.0/n) * test_tmp
            testing_errors.append(testError)
            # testing_errors.append(test_LCL)

            resTable.add_row([j + count, format(theta[0], '.4f'), format(theta[1], '.4f'), format(theta[2], '.4f'), format(theta[3], '.4f'), format(theta[4], '.4f'), format(theta[5], '.4f'), format(theta[6], '.4f'), LCL, test_LCL])
            count += 1

    print(resTable)
    plt.figure()
    plt.plot(iter_times, training_errors, '*-', c = "r", linewidth=1, label="training LCL")
    plt.plot(iter_times, testing_errors, '+-', c = "b", linewidth=1, label="testing LCL")

    plt.xlabel("iteration times")
    plt.ylabel("error")
    plt.legend()
    plt.title("Stochastic Gradient Descent")  
    plt.show() 


def gradient_decent():
    alpha = 0.00015 # learn rate
    # init
    theta = np.zeros(7)
    trainMat = readFile('./doc/dataForTrainingLogistic.txt')
    testMat = readFile('./doc/dataForTestingLogistic.txt')

    resTable = PrettyTable(["number of iterations", "theta0", "theta1", "theta2", "theta3", "theta4", "theta5", "theta6", "t0-rate", "t1-rate"])

    training_errors = []
    iter_times = []
    testing_errors = []
    m = len(trainMat)
    n = len(testMat)
    count = 1

    for j in range(15*base):
        sum = np.zeros(7)
        for index in range(m):
            hx = theta[0]
            for i in range(1,7):
                hx += theta[i] * trainMat[index][i-1]
            sum[0] += (trainMat[index][6] - p(hx))
            for i in range(1,7):
                sum[i] += (trainMat[index][6] - p(hx))*trainMat[index][i-1]

        for i in range(0,7):
            theta[i] = theta[i] + alpha * sum[i]

        if j % (base-1) == 0 and j >= (base-1):
            iter_times.append(j + count)
            tmp = 0
            test_tmp = 0
            LCL = 0
            test_LCL = 0

            for idx in range(m):
                hx = theta[0]
                for i in range(1,7):
                    hx += theta[i] * trainMat[idx][i-1]
                LCL += trainMat[idx][6]*math.log(p(hx)) + (1-trainMat[idx][6])*math.log(1-p(hx))
                if np.abs(p(hx) - trainMat[idx][6]) < 0.5:
                    tmp += 1
            trainError = 1-(1.0/m) * tmp
            # training_errors.append(trainError)
            training_errors.append(LCL)

            for idx in range(n):
                hx = theta[0]
                for i in range(1,7):
                    hx += theta[i] * testMat[idx][i-1]
                test_LCL += testMat[idx][6]*math.log(p(hx)) + (1-testMat[idx][6])*math.log(1-p(hx))
                if np.abs(p(hx) - testMat[idx][6]) < 0.5:
                    test_tmp += 1
            testError = 1-(1.0/n) * test_tmp
            # testing_errors.append(testError)
            testing_errors.append(test_LCL)

            resTable.add_row([j + count, format(theta[0], '.4f'), format(theta[1], '.4f'), format(theta[2], '.4f'), format(theta[3], '.4f'), format(theta[4], '.4f'), format(theta[5], '.4f'), format(theta[6], '.4f'), LCL, test_LCL])
            count += 1

    print(resTable)
    plt.figure()
    plt.plot(iter_times, training_errors, '*-', c = "b", linewidth=1, label="training LCL")
    plt.plot(iter_times, testing_errors, '+-', c = "r", linewidth=1, label="testing LCL")

    plt.xlabel("iteration times")
    plt.ylabel("error")
    plt.legend()
    plt.title("Stochastic Gradient Descent")  
    plt.show() 

def re_gradient_decent(trainMat):
    alpha = 0.00015 # learn rate
    # init
    theta = np.zeros(7)
    testMat = readFile('./doc/dataForTestingLogistic.txt')

    m = len(trainMat)
    n = len(testMat)
    count = 1

    for j in range(15*base):
        sum = np.zeros(7)
        for index in range(m):
            hx = theta[0]
            for i in range(1,7):
                hx += theta[i] * trainMat[index][i-1]
            sum[0] += (trainMat[index][6] - p(hx))
            for i in range(1,7):
                sum[i] += (trainMat[index][6] - p(hx))*trainMat[index][i-1]

        for i in range(0,7):
            theta[i] = theta[i] + alpha * sum[i]

    tmp = 0
    test_tmp = 0
    LCL = 0
    test_LCL = 0

    for idx in range(m):
        hx = theta[0]
        for i in range(1,7):
            hx += theta[i] * trainMat[idx][i-1]
        LCL += trainMat[idx][6]*math.log(p(hx)) + (1-trainMat[idx][6])*math.log(1-p(hx))
        if np.abs(p(hx) - trainMat[idx][6]) < 0.5:
            tmp += 1
    trainError = 1-(1.0/m) * tmp


    for idx in range(n):
        hx = theta[0]
        for i in range(1,7):
            hx += theta[i] * testMat[idx][i-1]
        test_LCL += testMat[idx][6]*math.log(p(hx)) + (1-testMat[idx][6])*math.log(1-p(hx))
        if np.abs(p(hx) - testMat[idx][6]) < 0.5:
            test_tmp += 1
    testError = 1-(1.0/n) * test_tmp
    count += 1

    return trainError, testError

def f_problem():
    trainMat = readFile('./doc/dataForTrainingLogistic.txt')

    m = len(trainMat)
    iter_times = []
    training_errors = []
    testing_errors = []

    for i in range(40):
        copy_mat = copy.deepcopy(trainMat)
        iMat = []

        for j in range((i+1)*10):
            index = random.randint(0, len(copy_mat)-1)
            iMat.append(copy_mat[index])
            np.delete(copy_mat, index)


        trainError, testError = re_gradient_decent(iMat)
        iter_times.append((i+1)*10)
        training_errors.append(trainError)
        testing_errors.append(testError)


    plt.plot(iter_times, training_errors, '*-', c = "b", linewidth=1, label="training LCL")
    plt.plot(iter_times, testing_errors, '+-', c = "r", linewidth=1, label="testing LCL")

    plt.xlabel("iteration times")
    plt.ylabel("error")
    plt.legend()
    plt.title("Stochastic Gradient Descent")  
    plt.show()

f_problem()