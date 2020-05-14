# -*- coding: utf-8 -*-
"""
Created on Thu May 14 15:37:22 2020

@author: Admin
"""
#Import Libraries
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

s='State/UnionTerritory'
#Import Dataset
df = pd.read_csv("covid_19_india.csv")

#Get names of all the states
states_list = []
for a in df['State/UnionTerritory']:
    if a not in states_list:
        states_list.append(a)
    
#Get total number of cases in each state
#Is there a better way to do this? Please clone and add comments if you know any
count_cases = {}    
for a in states_list:
    b=0
    for place,con in zip(df[s],df['Confirmed']):
        if(a==place):
            b+=con    
    count_cases[a] = b
    
#Pie chart for cases per state
plt.title('Statewise COVID-19 Cases in India')
labels = [place for place in states_list]

#Get data from dict
data = [(v) for i, (k, v) in enumerate(count_cases.items())]
plt.pie(data, labels=labels, autopct='%.2f')
plt.show()

#Bar Chart for statewise cases
#How to get the labels on x-axis to not overlap with each other?
plt.bar(states_list,data, align='center')
plt.show()

#Histogram
plt.hist(df['Date'])
plt.show()


