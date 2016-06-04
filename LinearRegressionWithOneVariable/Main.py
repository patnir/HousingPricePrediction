# -*- coding: utf-8 -*-
"""
Created on Sat Jun 04 13:20:54 2016

@author: Rahul Patni
"""
import re
import matplotlib.pyplot as plt
import numpy as np
import math

# Data contains the population of a city and the corresponding profits for a food truck

def LoadData(X, y, filename):
    fhand = open(filename)
    for line in fhand:
        line = line.rstrip()
        number = re.findall('[^,]+', line)
        X.append([float(number[0])])
        y.append(float(number[1]))
        
def PrintArray(array):
    for i in array:
        print i
    
def Plot(x, y, xlabel, ylabel, title):
    plt.plot(x, y, 'ro')
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.title(title)
    plt.show()    
    
def CostFunction(X, y, theta):
    m = len(X)
    predictions = np.dot(X, theta)
    errors_squared = predictions - y
    errors_squared = [round(math.pow(x, 2), 5) for x in errors_squared[0]]
    J = (1.0 / (2.0 * m)) * sum(errors_squared)
    return J
    #result = [(1.0 / (2.0 * m)) * math.pow(x, 2) for x in cost]
    #return sum(result)    

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


def main():
    X = []
    y = []
    LoadData(X, y, "data.txt")
    #Plot(X, y, "Population of city in 10,000s", "Profit in $10,000s", "Scatter plot of training data")
    # Adding an aditional row of ones to X for X0 values
    X = [[1.0] + x for x in X]
    #PrintArray(X)
    theta = np.zeros((len(X[0]), 1))
    # PrintArray(theta)
    # Setting number of iterations for gradient descent
    iterations = 1500
    # Setting learning rate for gradient descent
    alpha = 0.01
    cost = CostFunction(X, y, theta)
    
    
    
    
if __name__ == "__main__":
    main()