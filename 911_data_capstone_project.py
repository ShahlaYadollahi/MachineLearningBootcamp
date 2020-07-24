## -*- coding: utf-8 -*-
#"""
#Created on Tue Feb 25 17:23:29 2020
#
#@author: Shahla
#"""
#
#** Import numpy and pandas **
import numpy as np
import pandas as pd
#** Import visualization libraries and set %matplotlib inline. **
import seaborn as sns
import matplotlib.pyplot as plt
import cufflinks as cfl

#
#​
#** Read in the csv file as a dataframe called df **
df = pd.read_csv('911.csv')
#​
#** Check the info() of the df **
df.info()

#** Check the head of df **

df.head()

#** What are the top 5 zipcodes for 911 calls? **

df['zip'].value_counts().head(5)

#** What are the top 5 townships (twp) for 911 calls? **
df['twp'].value_counts().head(5)

#** Take a look at the 'title' column, how many unique title codes are there? **

df['title'].nunique()
#​
#
#** In the titles column there are "Reasons/Departments" specified before the title code.
#These are EMS, Fire, and Traffic. Use .apply() with a custom lambda expression to create 
#a new column called "Reason" that contains this string value.**

#*For example, if the title column value is EMS: BACK PAINS/INJURY , the Reason column value would be EMS. *
df['Reason'] = df['title'].apply(lambda x:x.split(':')[0] )
#​
#** What is the most common Reason for a 911 call based off of this new column? **
df['Reason'].value_counts().head()

#** Now use seaborn to create a countplot of 911 calls by Reason. **
sns.countplot(x='Reason',  data = df)


#** Now let us begin to focus on time information. What is the data type of the objects in the timeStamp column? **
type(df['timeStamp'][0])


#** You should have seen that these timestamps are still strings. Use pd.to_datetime
# to convert the column from strings to DateTime objects. **

df['timeStamp'] = pd.to_datetime(df['timeStamp'])


#​
#** You can now grab specific attributes from a Datetime object by calling them. For example:**
#
time = df['timeStamp'].iloc[0]
time.hour
#You can use Jupyter's tab method to explore the various attributes you can call. 
#Now that the timestamp column are actually DateTime objects, use .apply() 
#to create 3 new columns called Hour, Month, and Day of Week. You will create 
#these columns based off of the timeStamp column, reference the solutions if you get stuck on this step.

df['Hour'] = df['timeStamp'].apply(lambda x:x.hour)
df['Month'] = df['timeStamp'].apply(lambda x:x.month)
df['Day'] = df['timeStamp'].apply(lambda x:x.weekday())
#​
#** Notice how the Day of Week is an integer 0-6. Use the .map() with this dictionary to map the actual 
#string names to the day of the week: **
#
dmap = {0:'Mon',1:'Tue',2:'Wed',3:'Thu',4:'Fri',5:'Sat',6:'Sun'}
df['Day of Week'] = df['Day'].map(dmap)
#​
#​
#** Now use seaborn to create a countplot of the Day of Week column with the hue based off of the Reason column. **

sns.countplot(x = df['Day of Week'], hue = 'Reason', data = df)
plt.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)

#
#Now do the same for Month:
mmap = {12: 'Dec', 11:'Nov', 10:'Oct', 9: 'Sep', 8: 'Aug', 7:'Jul', 6: 'Jun', 5: 'May', 4: 'Apr', 3: 'Mar', 2:'Feb', 1:'Jan'}
df['Mon'] = df['Month'].map(mmap)
sns.countplot(x = df['Mon'], hue = 'Reason', data = df)
plt.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)

#
#​
#<matplotlib.legend.Legend at 0x10330ada0>
#
#Did you notice something strange about the Plot?
#
#** You should have noticed it was missing some Months, let's see if we can maybe fill in this information by plotting the information in another way, possibly a simple line plot that fills in the missing months, in order to do this, we'll need to do some work with pandas... **
#
#** Now create a gropuby object called byMonth, where you group the DataFrame by the month column and use the count() method for aggregation. Use the head() method on this returned DataFrame. **
#
#​
#lat	lng	desc	zip	title	timeStamp	twp	addr	e	Reason	Hour	Day of Week
#Month												
#1	13205	13205	13205	11527	13205	13205	13203	13096	13205	13205	13205	13205
#2	11467	11467	11467	9930	11467	11467	11465	11396	11467	11467	11467	11467
#3	11101	11101	11101	9755	11101	11101	11092	11059	11101	11101	11101	11101
#4	11326	11326	11326	9895	11326	11326	11323	11283	11326	11326	11326	11326
#5	11423	11423	11423	9946	11423	11423	11420	11378	11423	11423	11423	11423
#** Now create a simple plot off of the dataframe indicating the count of calls per month. **
#
#​
#<matplotlib.axes._subplots.AxesSubplot at 0x133a3c080>
#
#** Now see if you can use seaborn's lmplot() to create a linear fit on the number of calls per month. Keep in mind you may need to reset the index to a column. **
#
#​
#<seaborn.axisgrid.FacetGrid at 0x1342acd30>
#
#*Create a new column called 'Date' that contains the date from the timeStamp column. You'll need to use apply along with the .date() method. *
#
#​
#** Now groupby this Date column with the count() aggregate and create a plot of counts of 911 calls.**
#
#​
#
#** Now recreate this plot but create 3 separate plots with each plot representing a Reason for the 911 call**
#
#​
#
#​
#
#​
#
#** Now let's move on to creating heatmaps with seaborn and our data. We'll first need to restructure the dataframe so that the columns become the Hours and the Index becomes the Day of the Week. There are lots of ways to do this, but I would recommend trying to combine groupby with an unstack method. Reference the solutions if you get stuck on this!**
#
#​
#Hour	0	1	2	3	4	5	6	7	8	9	...	14	15	16	17	18	19	20	21	22	23
#Day of Week																					
#Fri	275	235	191	175	201	194	372	598	742	752	...	932	980	1039	980	820	696	667	559	514	474
#Mon	282	221	201	194	204	267	397	653	819	786	...	869	913	989	997	885	746	613	497	472	325
#Sat	375	301	263	260	224	231	257	391	459	640	...	789	796	848	757	778	696	628	572	506	467
#Sun	383	306	286	268	242	240	300	402	483	620	...	684	691	663	714	670	655	537	461	415	330
#Thu	278	202	233	159	182	203	362	570	777	828	...	876	969	935	1013	810	698	617	553	424	354
#5 rows × 24 columns
#
#** Now create a HeatMap using this new DataFrame. **
#
#​
#<matplotlib.axes._subplots.AxesSubplot at 0x1253fa198>
#
#** Now create a clustermap using this DataFrame. **
#
#​
#<seaborn.matrix.ClusterGrid at 0x1304fb668>
#
#** Now repeat these same plots and operations, for a DataFrame that shows the Month as the column. **
#
#​
#Month	1	2	3	4	5	6	7	8	12
#Day of Week									
#Fri	1970	1581	1525	1958	1730	1649	2045	1310	1065
#Mon	1727	1964	1535	1598	1779	1617	1692	1511	1257
#Sat	2291	1441	1266	1734	1444	1388	1695	1099	978
#Sun	1960	1229	1102	1488	1424	1333	1672	1021	907
#Thu	1584	1596	1900	1601	1590	2065	1646	1230	1266
#​
#<matplotlib.axes._subplots.AxesSubplot at 0x1304fbd30>
#
#​
#<seaborn.matrix.ClusterGrid at 0x12a1a61d0>
