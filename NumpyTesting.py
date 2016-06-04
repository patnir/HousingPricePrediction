# -*- coding: utf-8 -*-
"""
Created on Mon May 30 10:46:07 2016

@author: Rahul Patni
"""
import csv
import matplotlib.pyplot as plt
import numpy as np
import math
import sys


def ImportData(filename):
    with open(filename, 'rb') as csvfile:
        spamreader = csv.reader(csvfile, delimiter = '\t')
        data = list(spamreader)
        for i in range(0, len(data)):
            data[i] = [float(x) for x in data[i]]
        return data

def PrintArray(array):
    for i in range(len(array)):
        print array[i]

def ExtractColummnFromData(matrix, i):
    return [row[i] for row in matrix]

def Plot(x, y, xlabel, ylabel, title):
    plt.plot(x, y, 'r-')
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.title(title)
    plt.show()
    
def CostFunction(X, y, theta):
    m = len(X)
    cost = np.array((np.dot(X, theta) - y))
    result = [(1.0 / (2.0 * m)) * math.pow(x, 2) for x in cost]
    return sum(result)
    
def GradientDescent(X, y, theta, alpha):
    temp = theta
    m = len(X)
    cost = np.array((np.dot(X, theta) - y))
    for i in range(len(theta)):
        if (i == 0):
            temp[i] = temp[i] - (alpha / m) * (cost[i])
        else:
            temp[i] = temp[i] - (alpha / m) * (cost[i]) * sum(X[i])
    theta = temp
    
def Optimization(X_array, y_array, theta, alpha, repetitions, cost):
    prev_cost = sys.maxint * sys.maxint
    prev_theta = theta
    for i in range(repetitions):
        GradientDescent(X_array, y_array, theta, alpha)
        #print theta
        current_cost = CostFunction(X_array, y_array, theta)
        # print "round =", i, "; cost = ", cost[i]
        if (prev_cost < current_cost):
            theta = prev_theta
            break
        cost.append(current_cost)
        prev_cost = current_cost
        prev_theta = theta
            
def main():
    # Extracting X data, features
    X = ImportData('xData.csv')
    yData = ImportData('yData.csv')
    # Extracting y data, labels
    y = yData[0]
    # Plotting a graph for better 
#    beds = ExtractColummnFromData(X, 2)
#    Plot(beds, y, "regularized beds", "prices", 
#         "showing relationship between number of beds and price")
    # Converting X into an array using numpy for improved matrix operations
    X_array = X
    # Converting y into an array
    y_array = y
    # PrintArray(y_array)
    # Assigning zeros to theta to represent initial predictions
    theta = np.zeros(len(X[0]))
    # setting number of repetitions    
    repetitions = 10000
    # setting learning rate
    alpha = 0.0003
    # initializing costs to keep track of how cost changes with each repetition
    cost = []
    # Optimizing cost function
    Optimization(X_array, y_array, theta, alpha, repetitions, cost)
    # Plotting how cost varies as a function of number of repetitions
    Plot(range(len(cost)), cost, "repetitions", "cost", "tracking cost as repetitions increase")
    print "minimum cost = %.4g" %(min(cost))
    
    
if __name__ == "__main__":
    main()
