# -*- coding: utf-8 -*-
"""
Created on Thu May 14 15:37:22 2020

@author: Admin
"""
#Import Libraries
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

#Import Dataset
df = pd.read_csv("covid_19_india.csv")

#Get names of all the states
states_list = []
for a in df['State/UnionTerritory']:
    if a not in states_list:
        states_list.append(a)
    

count_cases = {}    
for a in states_list:
    b=df.loc('State/UnionTerritory'==a)['Confirmed']
    total=np.sum(b[1])
    count_cases.append(a,total)
    
        

