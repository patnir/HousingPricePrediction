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
            Beds.append(int(i[0]))
            Baths.append(int(i[1]))
            Sqft.append(int(i[2]))
            LotSize.append(float(i[3]))
            IsPriceReduced.append(int(i[4]))
            RecentDate.append(int(i[5]))
            Price.append(int(i[7]))
        track += 1
        
print Labels
print Beds
print IsPriceReduced