# -*- coding: utf-8 -*-
"""
Created on Tue May 24 19:59:21 2016

@author: Rahul Patni
"""
import csv

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
    
def printArray(array):
    for i in range(0, len(array)):
        print i
        print array[i]

def extractYFromData(data):
    y = [[each_list[i] for i in range(len(data[0]) - 1, len(data[0]))] for each_list in data[1:len(data)]]
    return y

def extractXFromData(data):
    return [[each_list[i] for i in range(0, len(data[0]) - 1)] for each_list in data[1:len(data)]]

def extractColummnFromMatrix(matrix, i):
    return [row[i] for row in matrix]

def main():
    openingMessage()
    data = importData("data.csv")
    heading = assignHeading(data)
    print heading
    y = extractYFromData(data)
    printArray(y)
    X = extractXFromData(data)
    printArray(X)
    Beds = extractColummnFromMatrix(X, 0)
    print Beds
            
if __name__ == "__main__":
    main()

