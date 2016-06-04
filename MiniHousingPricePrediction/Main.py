# -*- coding: utf-8 -*-
"""
Created on Sat Jun 04 15:51:47 2016

@author: Rahul Patni
"""

# Housing price prediction, but with only sq and number of bedrooms data

import re
import numpy as np

def LoadData(X, y, filename):
    fhand = open(filename)
    for line in fhand:
        line = line.rstrip()
        number = re.findall('[^,]+', line)
        number = [float(x) for x in number]
        X.append(number[0:len(number) - 1])
        y.append([number[-1]])
      
def PrintArray(array):
    for i in array:
        print i      
   
def ExtractColummnFromMatrix(matrix, i):
    return [row[i] for row in matrix]
   
def featureNormalize(X):
    mu = []
    sigma = []
    for i in range(len(X[0])):
        row = ExtractColummnFromMatrix(X, i)
        mu.append(np.mean(row))
        sigma.append(np.std(row))
    X = np.subtract(X, mu)
    X = np.divide(X, sigma)
    return(mu, sigma)
    
    
def main():
    X = []
    y = []
    LoadData(X, y, "data.txt")
    theta = np.zeros((len(X[0]), 1))
    mu, sigma = featureNormalize(X)
    PrintArray(mu)
    PrintArray(sigma)
    

if __name__ == "__main__":
    main()