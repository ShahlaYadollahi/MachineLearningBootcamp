# -*- coding: utf-8 -*-
"""
Created on Mon Feb 24 19:05:07 2020

@author: Shahla
"""

import seaborn as sns

tips = sns.load_dataset('tips')
sns.distplot(tips['total_bill'])
sns.distplot(tips['total_bill'],kde=True,bins=30)
sns.relplot(x="total_bill", y="tip", hue="smoker", data=tips, kind = 'scatter')
sns.relplot(x="total_bill", y="tip", hue="size", palette="ch:r=-.5,l=.75", data=tips)
sns.jointplot(x='total_bill',y='tip',data=tips,kind='scatter')
sns.jointplot(x='total_bill',y='tip',data=tips,kind='hex')
sns.jointplot(x='total_bill',y='tip',data=tips,kind='reg')
sns.pairplot(tips)
sns.pairplot(tips,hue='sex',palette='coolwarm')
sns.heatmap(tips.corr(),cmap='coolwarm',annot=True)
pivottable = tips.pivot_table(values='tip', index = 'sex', columns='smoker')
sns.lmplot(x='total_bill',y='tip',data=tips)
sns.lmplot(x='total_bill',y='tip',data=tips,hue='sex')
sns.lmplot(x='total_bill',y='tip',data=tips,col='sex')
sns.lmplot(x="total_bill", y="tip", row="sex", col="time",data=tips)
sns.lmplot(x='total_bill',y='tip',data=tips,col='day',hue='sex',palette='coolwarm',aspect=0.6,size=4)
sns.swarmplot(x='sex',y='tip',data=tips,palette='Set2')



fmri = sns.load_dataset("fmri")
sns.relplot(x="timepoint", y="signal", kind="line", ci="sd", data=fmri);
sns.relplot(x="timepoint", y="signal", hue="region", style = 'event', kind="line", data=fmri , dashes=False, markers=True);


flights = sns.load_dataset('flights')
flights.pivot_table(values='passengers',index='month',columns='year')
pvflights = flights.pivot_table(values='passengers',index='month',columns='year')
sns.heatmap(pvflights)
sns.heatmap(pvflights,cmap='magma',linecolor='white',linewidths=1)
sns.clustermap(pvflights)
# More options to get the information a little clearer like normalization
sns.clustermap(pvflights,cmap='coolwarm',standard_scale=1)
