# -*- coding: utf-8 -*-
"""
Created on Sat Jun 11 15:28:24 2016

@author: Rahul Patni
"""

# solving this problem using Normal Equation

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
    
def AppendColumnOfOnesToXNorm(Xnorm):
    X = []
    for i in range(len(Xnorm)):
        X.append(list(Xnorm[i]))
    X = [[1.0] + x for x in X]
    return X
    
# Using linear algebra to find the value for theta
def NormalEquation(X, y):    
    theta = np.linalg.inv(np.dot(np.transpose(X), X))
    theta = np.dot(theta, np.transpose(X))
    theta = np.dot(theta, y)
    return theta
    
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
    X = AppendColumnOfOnesToXNorm(X)
    theta = NormalEquation(X, y)
    print 'Optimal parameters'    
    PrintArray(theta)
    print
    print 'Training completed'
    UI(theta)
       
if __name__ == "__main__":
    main()