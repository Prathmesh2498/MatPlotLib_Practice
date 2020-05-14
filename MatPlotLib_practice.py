# -*- coding: utf-8 -*-
"""
Created on Thu May 14 15:37:22 2020

@author: Admin
"""

import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv("covid_19_india.csv")

states_list = []
for a in df['State/Union Territory']:
    if a not in states_list:
        states_list.append(a)