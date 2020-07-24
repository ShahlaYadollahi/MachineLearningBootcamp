# -*- coding: utf-8 -*-
"""
Created on Tue Feb 25 16:12:37 2020

@author: Shahla
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

print(plt.style.available)

df = pd.read_csv('df1.csv',index_col=0)

df2 = pd.read_csv('df2.csv')

plt.style.use('bmh')

df['A'].hist()

#Plot types 
df2.plot.area(alpha = 1)
df2.plot.bar(stacked = True)
#df.plot.density
#df.plot.hist
#df.plot.line
#df.plot.scatter
#df.plot.bar
#df.plot.box
#df.plot.hexbin
df2['a'].plot.kde()
df2.plot.density()
#df.plot.pie