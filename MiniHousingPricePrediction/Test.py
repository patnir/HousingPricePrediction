# -*- coding: utf-8 -*-
"""
Created on Sat Jun 11 11:18:41 2016

@author: Rahul Patni
"""

# Testing individual functions from Main.py to check where gradient descent is going wrong
import re
import numpy as np

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

def AppendRowOfOnesToXNorm(Xnorm):
    X = []
    for i in range(len(Xnorm)):
        X.append(list(Xnorm[i]))
    X = [[1.0] + x for x in X]
    return X

def main():
    X = []
    y = []
    LoadData(X, y, "data.txt")
    # m = len(y)
    mu, sigma, Xnorm = FeatureNormalize(X)  
    X = AppendRowOfOnesToXNorm(Xnorm)
    
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