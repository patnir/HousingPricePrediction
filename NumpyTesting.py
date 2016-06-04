# -*- coding: utf-8 -*-
"""
Created on Mon May 30 10:46:07 2016

@author: Rahul Patni
"""
import csv
import matplotlib.pyplot as plt
import numpy as np


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

def ExtractColummnFromData(matrix, i):
    return [row[i] for row in matrix]

def Plot(x, y, xlabel, ylabel, title):
    plt.plot(x, y, 'ro')
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.title(title)
    plt.show()

def main():
    # Extracting X data, features
    X = ImportData('xData.csv')
    yData = ImportData('yData.csv')
    # Extracting y data, labels
    y = yData[0]
    # Plotting a graph for better 
    beds = ExtractColummnFromData(X, 2)
    Plot(beds, y, "regularized beds", "prices", 
         "showing relationship between number of beds and price")
    # Converting X into an array using numpy for improved matrix operations
    X_array = np.array(X)
    # Assigning zeros to theta to represent initial predictions
    theta = np.zeros(len(X[0]))
                
if __name__ == "__main__":
    main()
