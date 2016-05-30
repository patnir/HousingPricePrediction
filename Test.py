# -*- coding: utf-8 -*-
"""
Created on Wed May 25 12:41:22 2016

@author: Rahul Patni
"""

import csv

Beds = []
Baths = []
Sqft = []
LotSize =  []
IsPriceReduced = []
RecentDate = []
PropertyType = []
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
                X.append(i[0:len(i)])
                Beds.append(float(i[0]))
                Baths.append(float(i[1]))
                Sqft.append(float(i[2]))
                LotSize.append(float(i[3]))
                IsPriceReduced.append(float(i[4]))
                RecentDate.append(float(i[5]))
                Price.append(float(i[7]))
            track += 1

LoadDataFromFile()

def MeanNormalizeData(array):
    meanBeds = reduce(lambda x, y: x + y, Beds) / len(array)
    for i in range(0,len(array)):
        Beds[i] -= meanBeds
    print round(Beds[0], 2)
    
MeanNormalizeData(Beds)

def PrintArray(array):
    for i in range(0, len(array)):
        print array[i]
 
def PrintRowFromArray(array, row):
    for i in range(0, len(array)):
        print array[i][row]

def ExtractColummnFromData(matrix, i):
    return [row[i] for row in matrix]
    