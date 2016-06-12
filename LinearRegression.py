# -*- coding: utf-8 -*-
"""
Created on Sat Jun 11 17:09:26 2016

@author: Rahul Patni
"""
# Rework assignment using linear regression

import numpy as np
import math

def PrintArray(array):
    for i in range(len(array)):
        print array[i]
    
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
    m = float(len(X))
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
    
def UI(headings, theta, mu, sigma):    
    userI = np.zeros(len(headings))
    #try:
    for i in range(len(headings)):
        userI[i] = float(raw_input('Enter ' + headings[i] + ' for the house: '))
        userI[i] = (userI[i] - mu[i]) / sigma[i]
    price = sum(theta * userI)
    print
    print 'The prediction for this house is $', round(price[0])
#    except:
#        print 'Print appropriate inputs'
#        UI(headings, theta, mu, sigma)

def LoadData(X, y, filename):
    fhand = open(filename)
    for line in fhand:
        line = line.rstrip()
        number = line.split('\t')
        toAdd = []
        for i in range(len(number) - 1):
            toAdd.append(number[i])
        X.append(toAdd)
        y.append([number[-1]])
        
def GetDataX(X):
    newX = []
    for i in range(len(X)):
        if i == 0:
            continue
        number = X[i]
        number = [float(x) for x in number[0:-1]]
        newX.append(number)
    return newX
    
def GetDataY(y):
    newY = []
    for i in range(len(y)):
        if i == 0:
            continue
        number = y[i]
        number = [float(x) for x in number]
        newY.append(number)
    return newY

def main():
    X = []
    y = []
    filename = 'data.csv'
    LoadData(X, y, filename)
    headings = X[0]
    headings = headings[0:-1]
    print headings
    X = GetDataX(X)
    y = GetDataY(y)
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
    UI(headings, theta, mu, sigma)
    
    
if __name__ == "__main__":
    main()