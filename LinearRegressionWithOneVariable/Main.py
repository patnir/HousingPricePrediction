# -*- coding: utf-8 -*-
"""
Created on Sat Jun 04 13:20:54 2016

@author: Rahul Patni
"""
import re
import matplotlib.pyplot as plt
import numpy as np
import math
import sys

# Data contains the population of a city and the corresponding profits for a food truck

def LoadData(X, y, filename):
    fhand = open(filename)
    for line in fhand:
        line = line.rstrip()
        number = re.findall('[^,]+', line)
        X.append([float(number[0])])
        y.append([float(number[1])])
        
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
    m = float(len(X))
    predictions = np.dot(X, theta)
    errors_squared = np.subtract(predictions, y)
    #print errors_squared
    errors_squared = [round(math.pow(x, 2), 5) for x in errors_squared]
    J = (1.0 / (2.0 * m)) * sum(errors_squared)
    return J    

def ExtractColummnFromMatrix(matrix, i):
    return [row[i] for row in matrix]

def GradientDescent(X, y, theta, alpha):
    temp = theta
    m = len(X)
    errors = np.dot(X, theta)
    errors = np.subtract(errors, y)
    offset = alpha / m
    for i in range(len(theta)):
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
    X = []
    y = []
    LoadData(X, y, "data.txt")
    #Plot(X, y, "Population of city in 10,000s", "Profit in $10,000s", "Scatter plot of training data")
    # Adding an aditional row of ones to X for X0 values
    X = [[1.0] + x for x in X]
    PrintArray(y)
    theta = np.zeros((len(X[0]), 1))
    # PrintArray(theta)
    # Setting number of iterations for gradient descent
    iterations = 1500
    # Setting learning rate for gradient descent
    alpha = 0.01
#    cost = CostFunction(X, y, theta)
#    print cost
#    GradientDescent(X, y, theta, alpha)
#    print theta
    cost = []
    # Optimizing cost function
    Optimization(X, y, theta, alpha, iterations, cost)
    # Plotting how cost varies as a function of number of repetitions
    Plot(range(len(cost)), cost, "iterations", "cost", "tracking cost as repetitions increase")
    print "minimum cost = %.4g" %(min(cost))
    print "minimum theta =", theta
      
    
if __name__ == "__main__":
    main()