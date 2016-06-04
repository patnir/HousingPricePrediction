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
    #print X   
    #print np.size(X)
    #print np.shape(X)
    #print np.size(theta)
    # print np.multiply(X, theta)
    h_x = []
    cost = []
    for i in range(len(X)):
        h_x.append(sum(X[i] * theta))
        difference = (1.0 / (2.0 * m)) * (math.pow((h_x[i] - y[i]), 2)) 
        cost.append(round(difference, 5))
    J = sum(cost)
    # print J
    return J
    
def GradientDescent(X, y, theta, alpha):
    temp = theta
    m = len(X)
    for i in range(len(theta)):
        h_x = sum(X[i] * theta)
        cost = h_x - y[i]        
        if (i == 0):
            temp[i] = temp[i] - (alpha / m) * (cost)
        else:
            temp[i] = temp[i] - (alpha / m) * (cost) * sum(X[i])
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
    X_array = np.array(X)
    # Converting y into an array
    y_array = np.array(y)
    # PrintArray(y_array)
    # Assigning zeros to theta to represent initial predictions
    theta = np.zeros(len(X[0]))
    # setting number of repetitions    
    repetitions = 10000
    # setting learning rate
    alpha = 0.0008
    # initializing costs to keep track of how cost changes with each repetition
    cost = []
    # Optimizing cost function
    Optimization(X_array, y_array, theta, alpha, repetitions, cost)
    # Plotting how cost varies as a function of number of repetitions
    Plot(range(len(cost)), cost, "repetitions", "cost", "tracking cost as repetitions increase")
    print "minimum cost = %.4g" %(min(cost))
    
if __name__ == "__main__":
    main()
