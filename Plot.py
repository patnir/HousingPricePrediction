# -*- coding: utf-8 -*-
"""
Created on Mon May 30 10:46:07 2016

@author: Rahul Patni
"""
import csv
import matplotlib.pyplot as plt
from sklearn import tree

def ImportData(filename):
    with open(filename, 'rb') as csvfile:
        spamreader = csv.reader(csvfile, delimiter = '\t')
        data = list(spamreader)
        for i in range(0, len(data)):
            data[i] = [float(x) for x in data[i]]
        return data

def PrintArray(array):
    for i in range(len(array)):
        print array[i]
    print i

def ExtractColummnFromData(matrix, i):
    return [row[i] for row in matrix]

def main():
    X = ImportData('xData.csv')
    yData = ImportData('yData.csv')
    y = yData[0]
    beds = ExtractColummnFromData(X, 2)
    plt.plot(beds, y, 'ro')
    plt.show()
                
if __name__ == "__main__":
    main()
