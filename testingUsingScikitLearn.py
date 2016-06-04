# -*- coding: utf-8 -*-
"""
Created on Thu Jun 02 22:52:25 2016

@author: Rahul Patni
"""
from sklearn import tree

# Machine learning recipe = collect training data -> train classifier
# -> make predictions

# This is a CLASSIFICATION problem (not a regression)

# There are features which are like the 'x' of an equation
# Label is like the 'y' of the equation

# This program will predict whether something is an apple or an orange

def training(weight, texture):
    # There are 2 features - weight and texture
    # Texture - 1 corresponds to smooth while 0 corresponds to bumpy
    
    features = [[140, 1], [130, 1], [150, 0], [170, 0]]
    
    
    # Only 2 labels / outcomes - apple: 0, orange = 1
    labels = [0, 0, 1, 1]
    
    # Using a decision tree classifier
    
    clf = tree.DecisionTreeClassifier()
    clf = clf.fit(features, labels)
    prediction = clf.predict([[weight, texture]])
    
    if prediction == 0:
        print "apple"
    else:
        print "orange"
    
weight = int(raw_input("Enter the weight of the fruit in grams: "))
texture = int(raw_input("Enter the texture of the fruit - 0 for bumpy or 1 for smooth: "))

training(weight, texture)