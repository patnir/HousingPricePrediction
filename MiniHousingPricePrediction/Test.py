# -*- coding: utf-8 -*-
"""
Created on Sat Jun 11 11:18:41 2016

@author: Rahul Patni
"""

# Testing individual functions from Main.py to check where gradient descent is going wrong
import re
import numpy as np
import math

def LoadData(X, y, filename):
    fhand = open(filename)
    for line in fhand:
        line = line.rstrip()
        number = re.findall('[^,]+', line)
        number = [float(x) for x in number]
        toAdd = []
        for i in range(len(number) - 1):
            toAdd.append(number[i])
        X.append(toAdd)
        y.append([number[-1]])

def PrintArray(array):
    for i in array:
        print i

def ExtractColummnFromMatrix(matrix, i):
    return [row[i] for row in matrix]

def FeatureNormalize(X):
    mu = []
    sigma = []
    for i in range(len(X[0])):
        row = ExtractColummnFromMatrix(X, i)
        mu.append(np.mean(row))
        sigma.append(np.std(row))
    X = np.subtract(X, mu)
    X = np.divide(X, sigma)
    return(mu, sigma, X)

def AppendColumnOfOnesToXNorm(Xnorm):
    X = []
    for i in range(len(Xnorm)):
        X.append(list(Xnorm[i]))
    X = [[1.0] + x for x in X]
    return X

def CostFunction(X, y, theta):
    m = float(len(X))
    predictions = np.dot(X, theta)
    errors_squared = np.subtract(predictions, y)
    #print errors_squared
    errors_squared = [round(math.pow(x, 2), 5) for x in errors_squared]
    J = (1.0 / (2.0 * m)) * sum(errors_squared)
    return J  

def GradientDescent(X, y, theta, alpha, iterations, cost):
    m = len(X)
    for k in range(iterations):
        temp = np.zeros((len(X[0]), 1))
        errors1 = np.dot(X, theta)
        errors = np.subtract(errors1, y)
        offset = alpha / m
        for i in range(len(theta)):
            temp[i] = theta[i] - offset * sum(errors * np.transpose([ExtractColummnFromMatrix(X, i)]))
        theta = temp
        cost.append(CostFunction(X, y, theta))
    return (theta, cost)
    
def UI(theta):    
    try:
        sqft = float(raw_input('Enter sqft for the house: '))
        rooms = int(raw_input('Enter number of bedrooms for the house: '))
        features = [[1], [sqft], [rooms]]
        price = sum(theta * features)
        print
        print 'The prediction for this house is $', round(price[0])
    except:
        print 'Print appropriate numbers for sqft and number of bedrooms'
        UI(theta)

def main():
    X = []
    y = []
    LoadData(X, y, "data.txt")
    mu, sigma, Xnorm = FeatureNormalize(X)  
    X = AppendColumnOfOnesToXNorm(Xnorm)
    theta = np.zeros((len(X[0]), 1))    
    cost = []
    iterations = 400
    alpha = 0.01
    theta, cost = GradientDescent(X, y, theta, alpha, iterations, cost)
    print 'Optimal parameters'  
    PrintArray(theta)
    print
    print 'Training completed'
    UI(theta)
    
    
if __name__ == "__main__":
    main()
    
    
#def printValudation():
#    LoadData(X, y, "data.txt")
#    print "X"    
#    PrintArray(X)
#    print "y"
#    PrintArray(y)
#    m = len(y)
#    print "m", m
    
    
'''
    print "X"    
    PrintArray(X)
    print "y"
    PrintArray(y)
    print "mu"
    PrintArray(mu)
    print "sigma"
    PrintArray(sigma)
    '''