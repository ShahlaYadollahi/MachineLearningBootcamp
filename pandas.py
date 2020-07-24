# -*- coding: utf-8 -*-
"""
Created on Thu Feb 20 18:28:48 2020

@author: Shahla
"""

import pandas as pd
import numpy as np
from numpy.random import randn


outside = ['G1','G1','G1','G2','G2','G2']
inside = [1,2,3,1,2,3]
hier_index = list(zip(outside,inside))
hier_index = pd.MultiIndex.from_tuples(hier_index)

df = pd.DataFrame(np.random.randn(6,2),index=hier_index,columns=['A','B'])

df.xs('G1')

##############################################################################

df = pd.DataFrame({'A':[1,2,np.nan],
                  'B':[5,np.nan,np.nan],
                  'C':[1,2,3]})

df.dropna()
df.dropna(axis=1)
df.fillna(value=-9999)


df.dropna(thresh=2)

df['A'].fillna(value=df['A'].mean())

#####################################################################
data = {'Company':['GOOG','GOOG','MSFT','MSFT','FB','FB'],
       'Person':['Sam','Charlie','Amy','Vanessa','Carl','Sarah'],
       'Sales':[200,120,340,124,243,350]}

df = pd.DataFrame(data)

df.groupby('Company')
#aggregate methods
df.groupby('Company').max()
df.groupby('Company').mean()
df.groupby('Company').std()
df.groupby('Company').count()
df.groupby('Company').describe()
df.groupby('Company').describe().transpose()
#######################################################################
df1 = pd.DataFrame({'A': ['A0', 'A1', 'A2', 'A3'],
                        'B': ['B0', 'B1', 'B2', 'B3'],
                        'C': ['C0', 'C1', 'C2', 'C3'],
                        'D': ['D0', 'D1', 'D2', 'D3']},
                        index=[0, 1, 2, 3])

df2 = pd.DataFrame({'A': ['A4', 'A5', 'A6', 'A7'],
                        'B': ['B4', 'B5', 'B6', 'B7'],
                        'C': ['C4', 'C5', 'C6', 'C7'],
                        'D': ['D4', 'D5', 'D6', 'D7']},
                         index=[4, 5, 6, 7]) 

df3 = pd.DataFrame({'A': ['A8', 'A9', 'A10'],
                        'B': ['B8', 'B9', 'B10'],
                        'C': ['C8', 'C9', 'C10'],
                        'D': ['D8', 'D9', 'D10']},
                        index=[8, 9, 10])
pd.concat([df1,df2,df3], axis =2)
#############################################################################
left = pd.DataFrame({'key': ['K0', 'K1', 'K2', 'K3'],
                     'A': ['A0', 'A1', 'A2', 'A3'],
                     'B': ['B0', 'B1', 'B2', 'B3']})
   
right = pd.DataFrame({'key': ['K0', 'K1', 'K2', 'K3'],
                          'C': ['C0', 'C1', 'C2', 'C3'],
                          'D': ['D0', 'D1', 'D2', 'D3']})    
pd.merge(left,right,how='right',on='key')
###########################################################################

data = {'A':['foo','foo','foo','bar','bar','bar'],
     'B':['one','one','two','two','one','one'],
       'C':['x','y','x','y','x','y'],
       'D':[1,3,2,5,4,1]}

df = pd.DataFrame(data)
df.pivot_table(values='D',index=['A', 'B'],columns=['C'])
########################################################