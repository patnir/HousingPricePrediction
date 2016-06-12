# -*- coding: utf-8 -*-
"""
Created on Wed May 25 12:41:22 2016

@author: Rahul Patni
"""

import csv

Beds = [] # Use data
Baths = [] # Use data
Sqft = [] # Use data
LotSize =  [] # Use Data
IsPriceReduced = [] # Use Data
RecentDate = [] # Use Data
PropertyType = [] # Not using data = all Data is 1
Price = []
Labels = []
X = []

def LoadDataFromFile():
    with open('data.csv', 'rb') as csvfile:
        spamreader = csv.reader(csvfile, delimiter = '\t')    
        data = list(spamreader)   
        track = 0    
        for i in data:
            print i
            if (track == 0):
                for j in i:
                    Labels.append(j)
            else:
                i = [float(x) for x in i] # Convert all elements to a float
                X.append(i[0:len(i) - 1])
                Beds.append(float(i[0]))
                Baths.append(float(i[1]))
                Sqft.append(float(i[2]))
                LotSize.append(float(i[3]))
                IsPriceReduced.append(float(i[4]))
                RecentDate.append(float(i[5]))
                Price.append(float(i[7]))
            track += 1

# LoadDataFromFile()

def MeanNormalizeData(array):
    maxMinArray = max(array) -  min(array)
    meanArray = reduce(lambda x, y: x + y, array) / len(array)
    for i in range(0,len(array)):
        array[i] -= meanArray
        array[i] = array[i] / maxMinArray
        array[i] = round(array[i], 5)
    
def PrintArray(array):
    for i in range(len(array)):
        print array[i]
 
def PrintRowFromArray(array, row):
    for i in range(len(array)):
        print array[i][row]

def ExtractColummnFromData(matrix, i):
    return [row[i] for row in matrix]
    
def MeanNormalizeX():
    for i in range(len(X[0]) - 1):
        row = ExtractColummnFromData(X, i)
        MeanNormalizeData(row)
        for j in range(0, len(row)):
            X[j][i] = row[j]
        
# MeanNormalizeX()

# PrintArray(X)

# PrintArray(Price)

# print Price[0]

def LoadData(X, y, filename):
    fhand = open(filename)
    for line in fhand:
        line = line.rstrip()
        number = line.split('\t')
        toAdd = []
        for i in range(len(number) - 1):
            toAdd.append(number[i])
        X.append(toAdd)
        y.append([number[-1]])
        
def GetDataX(X):
    newX = []
    for i in range(len(X)):
        if i == 0:
            continue
        number = X[i]
        number = [float(x) for x in number[0:-1]]
        newX.append(number)
    return newX
    
def GetDataY(y):
    newY = []
    for i in range(len(y)):
        if i == 0:
            continue
        number = y[i]
        number = [float(x) for x in number]
        newY.append(number)
    return newY

X = []
y = []
filename = 'data.csv'
LoadData(X, y, filename)
X = GetDataX(X)
y = GetDataY(y)
PrintArray(X)
PrintArray(y)



        
    