# -*- coding: utf-8 -*-
"""
Created on Mon May 30 10:46:07 2016

@author: Rahul Patni
"""
import csv
import matplotlib.pyplot as plt


def ImportData(filename):
    with open(filename, 'rb') as csvfile:
        spamreader = csv.reader(csvfile, delimiter = '\t')
        data = list(spamreader)
        for i in range(0, len(data)):
            data[i] = [float(x) for x in data[i]]
        return data

def ExtractColummnFromData(matrix, i):
    return [row[i] for row in matrix]

def main():
    xData = ImportData('xData.csv')
    yData = ImportData('yData.csv')
    beds = ExtractColummnFromData(xData, 2)
    plt.plot(beds, yData[0], 'ro')
    plt.show()
                
if __name__ == "__main__":
    main()
