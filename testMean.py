# -*- coding: utf-8 -*-
"""
Created on Fri Sep 21 13:53:47 2018

@author: pfarrell

Trying to create a dataset with given mean and standard
deviation manually, then graphing the results in a histogram.

"""

from math import factorial,sqrt
import pandas as pd
import matplotlib.pyplot as plt

#To solve for row r and n entry in Pascal's Triangle

def factorial2(x):
    '''Returns x!'''
    if x == 0: return 1
    return x*factorial(x-1)

def combin(r,k):
    '''Returns rCk'''
    return factorial(r)/(factorial(k)*factorial(r-k))

def pascal(row,entry):
    '''calculates the entry in Pascal's Triangle
    corresponding to a given row and entry'''
    return combin(row,entry)

def triangle(rows):
    '''Prints out Pascal's Triangle'''
    for i in range(rows+1):
        for j in range(i+1):
            print (int(pascal(i,j)),end= ' ')
        print()

def pascal_row(row):
    output = []
    for j in range(row+1):
        output.append(int(pascal(row,j)))

    return output

def mean(mylist):
    return sum(mylist)/len(mylist)

def std_dev(mylist):
    list_mean = mean(mylist)
    sum_of_squares = 0
    for n in mylist:
        sum_of_squares += (list_mean - n)**2
    return sqrt(sum_of_squares / len(mylist))

def generate_set(mean,stdDev,num=128):
    '''Generates a dataset of length 128
    with given mean and SDev'''
    output = []
    p = pascal_row(7)
    for ind,n in enumerate(p):
        for i in range(n):
            output.append(mean+(4-ind)*stdDev)
    return output

data = generate_set(10,3)
        
#data = pd.read_csv('testmean.csv')
df = pd.Series(data)
df.hist(bins=14)
plt.grid(axis='y', alpha=0.75)                