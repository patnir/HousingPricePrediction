# -*- coding: utf-8 -*-
"""
Created on Tue May 24 19:59:21 2016

@author: Rahul Patni
"""
import csv

def OpeningMessage():
    print("\n" + "My attempt at housing price prediction from a dataset of 50 houses" + "\n")

def ImportData(filename):
    with open(filename, 'rb') as csvfile:
        spamreader = csv.reader(csvfile, delimiter = '\t')
        data = list(spamreader)
        return data

def AssignHeading(data):
    heading = []
    for i in range(0,len(data[0])):
        heading.append(data[0][i])    
    return heading

def PrintArray(array):
    for i in range(0, len(array)):
        print array[i]
    print i

def ExtractYFromData(data):
    y = [[each_list[i] for i in range(len(data[0]) - 1, len(data[0]))] for each_list in data[1:len(data)]]
    for i in range(0, len(y)):
        y[i] = float(y[i][0])
    return y

def ExtractXFromData(data):
    X = [[each_list[i] for i in range(0, len(data[0]) - 1)] for each_list in data[1:len(data)]]
    # convert all values in X to floats
    track = 0
    for i in X:
        X[track] = [float(x) for x in i]
        track += 1
    return X

def ExtractColummnFromMatrix(matrix, i):
    return [row[i] for row in matrix]

def MeanNormalizeData(array):
    maxMinArray = max(array) -  min(array)
    meanArray = reduce(lambda x, y: x + y, array) / len(array)
    for i in range(0,len(array)):
        array[i] -= meanArray
        array[i] = array[i] / maxMinArray
        array[i] = round(array[i], 5)

def MeanNormalizeX(X):
    for i in range(0, len(X[0]) - 1):
        row = ExtractColummnFromMatrix(X, i)
        MeanNormalizeData(row)
        for j in range(0, len(row)):
            X[j][i] = row[j]

def SaveXToFile(array, filename):
    with open (filename, 'wb') as csvfile:
        spamwriter = csv.writer(csvfile, delimiter = '\t')
        for i in range(0, len(array)):
            spamwriter.writerow(array[i])
            
def SaveYToFile(array, filename):
    with open (filename, 'wb') as csvfile:
        spamwriter = csv.writer(csvfile, delimiter = '\t')
        spamwriter.writerow(array)

def main():
    OpeningMessage()
    data = ImportData("data.csv")
    heading = AssignHeading(data)
    print heading
    y = ExtractYFromData(data)
    PrintArray(y)
    X = ExtractXFromData(data)
    PrintArray(X)
    MeanNormalizeX(X)
    SaveXToFile(X, 'xData.csv')
    SaveYToFile(y, 'yData.csv')
            
if __name__ == "__main__":
    main()

