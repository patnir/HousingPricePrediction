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

def main():
    openingMessage()
    data = importData("data.csv")
    heading = assignHeading(data)
    print heading
    y = [[each_list[i] for i in range(len(data[0]) - 1, len(data[0]))] for each_list in data[1:len(data)]]
    printArray(y)   
    X = [[each_list[i] for i in range(0, len(data[0]) - 1)] for each_list in data[1:len(data)]]
    printArray(X)
    #printArray(y)
            
if __name__ == "__main__":
    main()

