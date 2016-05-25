# -*- coding: utf-8 -*-
"""
Created on Tue May 24 19:59:21 2016

@author: Rahul Patni
"""
import csv
from numpy import matrix

def openingMessage():
    print("\n" + "My attempt at housing price prediction from a dataset of 50 houses" + "\n")

def importData(filename):
    with open(filename, 'rb') as csvfile:
        spamreader = csv.reader(csvfile, delimiter = '\t')
        data = list(spamreader)
        return data

def assignHeading(data):
    heading = []
    for i in range(0,len(data[0])):
        heading.append(data[0][i])    
    return heading

def print2dArray(array):
    for i in range(0, len(array)):
        print i
        print array[i]

def main():
    openingMessage()
    data = importData("data.csv")
    heading = assignHeading(data)
    print heading
    
    X = matrix(data)
    print2dArray(X)
            
if __name__ == "__main__":
    main()

