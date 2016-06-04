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

def ExtractColummnFromMatrix(matrix, i):
    return [row[i] for row in matrix]

def Plot(x, y, xlabel, ylabel, title):
    plt.plot(x, y, 'r-')
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.title(title)
    plt.show()
    
def CostFunction(X, y, theta):
    m = float(len(X))
    predictions = np.dot(X, theta)
    errors_squared = np.subtract(predictions, y)
    #print errors_squared
    errors_squared = [round(math.pow(x, 2), 5) for x in errors_squared]
    J = (1.0 / (2.0 * m)) * sum(errors_squared)
    return J
    
def GradientDescent(X, y, theta, alpha):
    temp = theta
    m = len(X)
    errors = np.dot(X, theta)
    errors = np.subtract(errors, y)
    offset = alpha / m
    for i in range(len(theta)):
        if (i == 0):
            temp[i] = temp[i] - offset * sum(errors * np.transpose([ExtractColummnFromMatrix(X, i)]))
        else:
            temp[i] = temp[i] - offset * sum(errors * np.transpose([ExtractColummnFromMatrix(X, i)]))
    theta = temp
    
def Optimization(X_array, y_array, theta, alpha, repetitions, cost):
    prev_cost = sys.maxint * sys.maxint
    prev_theta = theta
    #print repetitions
    for i in range(repetitions):
        GradientDescent(X_array, y_array, theta, alpha)
        #PrintArray(theta)
        current_cost = CostFunction(X_array, y_array, theta)
        #print "round =", i, "; cost = ", current_cost
        if (prev_cost < current_cost):
            theta = prev_theta
            break
        cost.append(current_cost)
        prev_cost = current_cost
        prev_theta = theta
            
def main():
    # Extracting X data, features
    XData = ImportData('xData.csv')
    # Adding an aditional row of ones to X for X0 values    
    X = [[1.0] + x for x in XData]
    yData = ImportData('yData.csv')
    # Extracting y data, labels
    y = []
    for i in yData[0]:
        y.append([i])
    # Plotting a graph for better 
#    beds = ExtractColummnFromData(X, 2)
#    Plot(beds, y, "regularized beds", "prices", 
#         "showing relationship between number of beds and price")
    # Assigning zeros to theta to represent initial predictions
    theta = np.zeros((len(X[0]), 1))
    # setting number of repetitions    
    repetitions = 10000
    # setting learning rate
    alpha = 0.1
    # initializing costs to keep track of how cost changes with each repetition
    cost = []
    # Optimizing cost function
    Optimization(X, y, theta, alpha, repetitions, cost)
    # Plotting how cost varies as a function of number of repetitions
    Plot(range(len(cost)), cost, "repetitions", "cost", "tracking cost as repetitions increase")
    print "minimum cost = %.4g" %(min(cost))
    print "minimum theta =", theta
        
if __name__ == "__main__":
    main()
