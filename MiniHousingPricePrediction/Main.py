# -*- coding: utf-8 -*-
"""
Created on Sat Jun 04 15:51:47 2016

@author: Rahul Patni
"""

# Housing price prediction, but with only sq and number of bedrooms data

import re
import numpy as np
import math
import matplotlib.pyplot as plt

def LoadData(X, y, filename):
    fhand = open(filename)
    for line in fhand:
        line = line.rstrip()
        number = re.findall('[^,]+', line)
        number = [float(x) for x in number]
        m = []
        for i in range(len(number) - 1):
            m.append(number[i])
        print m
        X.append(m)
        y.append([number[-1]])
      
def PrintArray(array):
    for i in array:
        print i      
   
def Plot(x, y, xlabel, ylabel, title):
    plt.plot(x, y, 'r-')
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.title(title)
    plt.show()
    
def ExtractColummnFromMatrix(matrix, i):
    return [row[i] for row in matrix]
   
def CostFunction(X, y, theta):
    m = float(len(X))
    predictions = np.dot(X, theta)
    errors_squared = np.subtract(predictions, y)
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
        temp[i] = temp[i] - offset * sum(errors * np.transpose([ExtractColummnFromMatrix(X, i)]))
    theta = temp

def Optimization(X_array, y_array, theta, alpha, repetitions, cost):
    prev_cost = 0
    prev_theta = theta
    #print repetitions
    for i in range(repetitions):
        GradientDescent(X_array, y_array, theta, alpha)
        #PrintArray(theta)
        current_cost = CostFunction(X_array, y_array, theta)
        #print "round =", i, "; cost = ", current_cost
        if (prev_cost < current_cost and i != 0):
            theta = prev_theta
            break
        cost.append(current_cost)
        prev_cost = current_cost
        prev_theta = theta
   
def featureNormalize(X):
    mu = []
    sigma = []
    for i in range(len(X[0])):
        row = ExtractColummnFromMatrix(X, i)
        mu.append(np.mean(row))
        sigma.append(np.std(row))    
    X = np.subtract(X, mu)
    X = np.divide(X, sigma)
    return(mu, sigma, X)
    
    
def main():
    X = []
    y = []
    LoadData(X, y, "data.txt")
    mu, sigma, Xnorm = featureNormalize(X)
    print mu, sigma
    # Add intercept term to X
    X = []
    for i in range(len(Xnorm)):
        X.append(list(Xnorm[i]))
    X = [[1.0] + x for x in X]    
    # Initialize theta and run gradient descent
    theta = np.zeros((len(X[0]), 1))    
    alpha = 0.01
    iterations = 400
    cost = []
    Optimization(X, y, theta, alpha, iterations, cost)
    Plot(range(len(cost)), cost, "repetitions", "cost", "tracking cost as repetitions increase")
    print "minimum cost = %.4g" %(min(cost))
    print "minimum theta =", theta
    

        
    

if __name__ == "__main__":
    main()